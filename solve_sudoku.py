
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    
    if num in [board[i][col] for i in range(9)]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False    
    return True

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True

    row, col = empty_loc

    for num in range(1, 10):
        if is_valid(board, row, col, num):   # 세가지 규칙이 맞을 때 숫자를 넣어야 하므로 is_valid 확인!
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False  