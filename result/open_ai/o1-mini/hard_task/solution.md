To solve the problem of determining the maximum total number of moves Alice can achieve when she and Bob take turns capturing pawns with a knight on a 50x50 chessboard, we can use a dynamic programming (DP) approach with memoization. Here's a step-by-step explanation of the solution:

### Step-by-Step Explanation

1. **Understanding the Problem:**
   - We have a knight starting at position `(kx, ky)` on a 50x50 chessboard.
   - There are up to 15 pawns placed on the board.
   - Alice and Bob take turns to capture pawns. Alice aims to maximize the total number of moves, while Bob aims to minimize it.
   - The knight can move in an "L" shape: two cells in one direction and then one cell perpendicular to that.

2. **Dynamic Programming Approach:**
   - We need to consider all possible states where:
     - The knight is at a certain position.
     - A subset of pawns remains to be captured.
     - It's either Alice's or Bob's turn.
   - Each state can be represented by:
     - `last_pos_index`: The index of the knight's current position (starting position is index 0, and pawns are indexed from 1 to n).
     - `mask`: A bitmask representing which pawns are still on the board.
   - We use memoization to store the results of subproblems to avoid redundant calculations.

3. **Precomputing Distances:**
   - We precompute the minimum number of moves required for the knight to reach each pawn from every other pawn (including the starting position).
   - This is done using Breadth-First Search (BFS) for each position to compute the shortest path to all other relevant positions.

4. **Recursive DP Function:**
   - The `dp` function calculates the maximum total number of moves based on the current state `(last_pos, mask)`.
   - If it's Alice's turn, she will choose the move that maximizes the total number of moves.
   - If it's Bob's turn, he will choose the move that minimizes the total number of moves.
   - The function recursively explores all possible moves and uses memoization to store intermediate results.

5. **Handling the Game Turns:**
   - The turn alternates between Alice and Bob based on the number of pawns captured so far.
   - Alice starts the game, so if the number of pawns captured is even, it's Alice's turn; otherwise, it's Bob's.

6. **Final Calculation:**
   - We start the DP from the initial position with all pawns on the board.
   - The DP function explores all possible sequences of capturing pawns, considering both Alice's and Bob's optimal strategies.

### Python Implementation

Below is the Python implementation of the above approach:

```python
from collections import deque
import sys
sys.setrecursionlimit(1 << 25)

class Solution(object):
    def maxMoves(self, kx, ky, positions):
        """
        :type kx: int
        :type ky: int
        :type positions: List[List[int]]
        :rtype: int
        """
        n = len(positions)
        positions_list = [(kx, ky)] + [tuple(p) for p in positions]  # index 0 is start
        # Precompute distances between all positions using BFS
        distances = [ [0]*(n+1) for _ in range(n+1) ]

        # Possible knight moves
        moves = [ (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1) ]

        # Precompute BFS distances
        for i in range(n+1):
            start_x, start_y = positions_list[i]
            # BFS from (start_x, start_y)
            visited = [[-1 for _ in range(50)] for _ in range(50)]
            q = deque()
            q.append( (start_x, start_y) )
            visited[start_x][start_y] = 0
            targets = set(range(n+1))
            targets.remove(i)
            while q and targets:
                x, y = q.popleft()
                d = visited[x][y]
                for dx, dy in moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and visited[nx][ny] == -1:
                        visited[nx][ny] = d + 1
                        q.append( (nx, ny) )
                        # Check if this position is one of the targets
                        for j in targets.copy():
                            if positions_list[j] == (nx, ny):
                                distances[i][j] = d + 1
                                targets.remove(j)
                                break  # To speed up
            # At this point, distances[i][j] is filled for all j
        # Now implement DP with memoization
        memo_size = (n+1) * (1 << n)
        memo = [-1] * memo_size

        def dp(last_pos, mask):
            index = last_pos * (1 << n) + mask
            if memo[index] != -1:
                return memo[index]
            if mask == 0:
                memo[index] = 0
                return 0
            # Determine whose turn it is
            bits_set = bin(mask).count('1')
            captured = n - bits_set
            if captured % 2 == 0:
                # Alice's turn: maximize the sum
                max_sum = -float('inf')
                for p in range(n):
                    if mask & (1 << p):
                        move = distances[last_pos][p+1]
                        total = move + dp(p+1, mask ^ (1 << p))
                        if total > max_sum:
                            max_sum = total
                memo[index] = max_sum
            else:
                # Bob's turn: minimize the sum
                min_sum = float('inf')
                for p in range(n):
                    if mask & (1 << p):
                        move = distances[last_pos][p+1]
                        total = move + dp(p+1, mask ^ (1 << p))
                        if total < min_sum:
                            min_sum = total
                memo[index] = min_sum
            return memo[index]

        full_mask = (1 << n) -1
        return dp(0, full_mask)
```

### Explanation of the Code

1. **Precompute Distances:**
   - We first compute the shortest path (minimum number of knight moves) from the starting position to each pawn and between all pairs of pawns using BFS. This information is stored in the `distances` matrix.

2. **Dynamic Programming with Memoization:**
   - We initialize a memoization list `memo` to store the results of subproblems. Each state is uniquely identified by the current knight position (`last_pos`) and the set of remaining pawns (`mask`).
   - The `dp` function recursively calculates the maximum total number of moves from the current state.
   - Depending on whose turn it is (Alice or Bob), the function either maximizes or minimizes the total number of moves by exploring all possible pawn captures.

3. **Final Result:**
   - We start the DP with the knight at the initial position (`last_pos = 0`) and all pawns present (`mask = full_mask`).
   - The result returned by `dp(0, full_mask)` is the maximum total number of moves Alice can achieve when both players play optimally.

### Example Walkthrough

Let's consider **Example 1** from the problem statement:

- **Input:** `kx = 1, ky = 1, positions = [[0,0]]`
- **Output:** `4`

**Explanation:**

- There's only one pawn at `(0,0)`.
- The knight starts at `(1,1)`.
- It takes 4 moves for the knight to reach `(0,0)`.
- Since Alice captures the only pawn, the total number of moves is 4.

The provided solution correctly computes this result by precomputing the distance and using the DP approach to accumulate the total number of moves.

### Conclusion

This DP approach efficiently solves the problem by leveraging memoization and precomputing necessary distances. It ensures that all possible game states are considered while optimizing for both Alice's and Bob's strategies.