To solve this problem, we apply a minimax algorithm with memoization, adapting it to the specific game mechanics and constraints described in the problem:

1. **Game Modeling**:
   - **State**: Represented by a bitmask `s` of remaining pawns, the knight's position `pos`, and the `turn` (Alice or Bob).
   - **Goal**: Alice wants to maximize the total number of moves, while Bob wants to minimize it.

2. **Precompute Knight Moves**:
   - Since the knight moves in an unimpeded manner (it can pass over other pawns without capturing them), we precompute the minimum number of moves required for the knight to reach any pawn from any other position.
   - We only need to calculate distances between the unique positions involved (starting position and pawn positions), reducing the computational load.

3. **Minimax with Memoization**:
   - **Recursion**: At each state, the player chooses a pawn to capture next, considering future consequences. Alice aims to maximize, while Bob aims to minimize the total moves.
   - **Memoization**: We store results of subproblems to avoid redundant calculations, speeding up the computation.

Below is the Python code implementing the solution:

```python
class Solution(object):
    def maxMoves(self, kx, ky, positions):
        """
        :type kx: int
        :type ky: int
        :type positions: List[List[int]]
        :rtype: int
        """
        from collections import deque

        # Initialize positions with the starting knight position
        positions = [(kx, ky)] + [tuple(pos) for pos in positions]
        n = len(positions) - 1  # number of pawns

        # Map positions to indices
        pos_to_index = {pos: idx for idx, pos in enumerate(positions)}

        # Precompute distances between all pairs of positions
        N = n + 1
        distances = [[0] * N for _ in range(N)]

        for i in range(N):
            start_pos = positions[i]
            queue = deque()
            visited = [[-1]*50 for _ in range(50)]
            x, y = start_pos
            visited[x][y] = 0
            queue.append((x, y))

            needed_positions = set(positions)
            remaining = set(positions)
            remaining.remove(start_pos)

            while queue and remaining:
                x, y = queue.popleft()
                d = visited[x][y]
                if (x, y) in remaining:
                    j = pos_to_index[(x, y)]
                    distances[i][j] = d
                    remaining.remove((x, y))
                for dx, dy in [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 50 and 0 <= ny < 50 and visited[nx][ny] == -1:
                        visited[nx][ny] = d + 1
                        queue.append((nx, ny))

        from functools import lru_cache
        # Turn constants for clarity
        ALICE_TURN = True
        BOB_TURN = False

        @lru_cache(None)
        def dfs(s, pos, turn):
            if s == 0:
                return 0
            if turn == ALICE_TURN:
                max_total_moves = 0
                for i in range(1, N):   # Pawns are indexed from 1 to N-1
                    if s & (1 << (i -1)):
                        dist = distances[pos][i]
                        new_s = s ^ (1 << (i -1))
                        total_moves = dist + dfs(new_s, i, not turn)
                        max_total_moves = max(max_total_moves, total_moves)
                return max_total_moves
            else:
                min_total_moves = float('inf')
                for i in range(1, N):
                    if s & (1 << (i -1)):
                        dist = distances[pos][i]
                        new_s = s ^ (1 << (i -1))
                        total_moves = dist + dfs(new_s, i, not turn)
                        min_total_moves = min(min_total_moves, total_moves)
                return min_total_moves

        initial_s = (1 << n) -1  # All pawns are initially on the board
        result = dfs(initial_s, 0, ALICE_TURN)
        return result
```