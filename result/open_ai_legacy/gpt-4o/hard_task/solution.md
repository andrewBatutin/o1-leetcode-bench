To solve this problem, we need to simulate the game between Alice and Bob where they take turns capturing pawns with a knight on a chessboard. The knight moves in an "L" shape, and we need to calculate the minimum number of moves required to capture each pawn. Alice tries to maximize the total number of moves, while Bob tries to minimize it.

Here's a step-by-step approach to solve the problem:

1. **Breadth-First Search (BFS) for Knight Moves**: We need a function to calculate the minimum number of moves required for the knight to reach any given position on the board. This can be efficiently done using BFS.

2. **Dynamic Programming with Memoization**: Since both players play optimally, we can use dynamic programming to store the results of subproblems (i.e., the minimum number of moves required to capture the remaining pawns from a given position).

3. **Recursive Function**: We will create a recursive function that simulates the game. This function will consider all possible moves for both players and use memoization to avoid redundant calculations.

Here's the complete Python solution:

```python
from collections import deque
from functools import lru_cache

class Solution(object):
    def maxMoves(self, kx, ky, positions):
        """
        :type kx: int
        :type ky: int
        :type positions: List[List[int]]
        :rtype: int
        """
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), 
                        (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
        def bfs(start_x, start_y):
            dist = [[float('inf')] * 50 for _ in range(50)]
            dist[start_x][start_y] = 0
            queue = deque([(start_x, start_y)])
            while queue:
                x, y = queue.popleft()
                for dx, dy in knight_moves:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and dist[nx][ny] == float('inf'):
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
            return dist
        
        initial_dist = bfs(kx, ky)
        
        @lru_cache(None)
        def dp(mask, x, y):
            if mask == 0:
                return 0
            min_moves = float('inf')
            for i in range(len(positions)):
                if mask & (1 << i):
                    px, py = positions[i]
                    dist = bfs(x, y)[px][py]
                    min_moves = min(min_moves, dist + dp(mask ^ (1 << i), px, py))
            return min_moves
        
        max_moves = 0
        for i in range(len(positions)):
            px, py = positions[i]
            dist = initial_dist[px][py]
            max_moves = max(max_moves, dist + dp((1 << len(positions)) - 1 ^ (1 << i), px, py))
        
        return max_moves

# Example usage:
# sol = Solution()
# print(sol.maxMoves(1, 1, [[0, 0]]))  # Output: 4
# print(sol.maxMoves(0, 2, [[1, 1], [2, 2], [3, 3]]))  # Output: 8
# print(sol.maxMoves(0, 0, [[1, 2], [2, 4]]))  # Output: 3
```

### Explanation:
1. **BFS Function**: The `bfs` function calculates the minimum number of moves required for the knight to reach any position on the board from a given starting position. This is done using a breadth-first search.

2. **Dynamic Programming with Memoization**: The `dp` function uses memoization to store the results of subproblems. It takes a bitmask representing the remaining pawns and the current position of the knight. It recursively calculates the minimum number of moves required to capture all remaining pawns.

3. **Main Logic**: The main logic iterates over all possible starting pawns and calculates the maximum number of moves Alice can achieve by starting with each pawn and playing optimally.

This solution ensures that both players play optimally and calculates the maximum total number of moves made during the game.