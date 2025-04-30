from collections import deque

def compute_pond_sizes(land: list[list[int]]) -> list[int]:
    rows, cols = len(land), len(land[0])
    visited = set()
    result = []

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1),          ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1)]

    for i in range(rows):
        for j in range(cols):
            if land[i][j] != 0 or (i, j) in visited:
                continue

            counter = 0
            stack = deque([(i, j)])
            visited.add((i, j))

            while stack:
                r, c = stack.pop()
                counter += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and
                        0 <= nc < cols and
                        land[nr][nc] == 0 and
                        (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        stack.append((nr, nc))

            result.append(counter)

    return result
