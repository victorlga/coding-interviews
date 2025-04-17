def place_queens(n: int) -> list[list[int]]:
    def is_valid(queens: list[int], row: int, col: int) -> bool:
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row: int, queens: list[int]):
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_valid(queens, row, col):
                queens[row] = col
                backtrack(row + 1, queens)

    solutions = []
    queens = [-1] * n
    backtrack(0, queens)
    return solutions


