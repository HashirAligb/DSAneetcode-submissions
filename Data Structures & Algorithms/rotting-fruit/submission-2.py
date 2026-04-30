class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        def rot(r, c) -> None:
            nonlocal fresh
            if (r < 0 or r == R or c < 0 or c == C or grid[r][c] != 1 ): 
                return 
            grid[r][c] = 2
            fresh -= 1
            q.append((r, c))

        minutes = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                rot(r + 1, c)
                rot(r - 1, c)
                rot(r, c + 1)
                rot(r, c - 1)
            minutes += 1

        return minutes if fresh == 0 else -1
