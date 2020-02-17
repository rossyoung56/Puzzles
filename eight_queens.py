board = []
board_size = 0
solutions = 0


def solve():
    global solutions
    for y in range(board_size):
        if 'Q' in board[y]:
            continue
        for x in range(board_size):
            if valid(x, y):
                board[y][x] = 'Q'
                solve()
                board[y][x] = 0
        return
    if validate():
        solutions += 1
        print_board()


def valid(x, y):
    for i in range(board_size):
        row = board[i]
        if i == y and 'Q' in row:
            return False
        diff = y - i
        if 0 <= x - diff < board_size and row[x - diff] == 'Q':
            return False
        if row[x] == 'Q':
            return False
        if 0 <= x + diff < board_size and row[x + diff] == 'Q':
            return False

    return True


def validate():
    for y in range(board_size):
        if 'Q' not in board[y]:
            return False
        for x in range(board_size):
            if board[y][x] == 'Q':
                board[y][x] = 0
                if not valid(x, y):
                    return False
                board[y][x] = 'Q'

    return True


def print_board():
    for row in board:
        for col in row:
            print(" ", col, sep="", end="")
        print()
    print()


if __name__ == '__main__':
    board_size = int(input("Enter board size: "))
    for r in range(board_size):
        board.append([])
        for _ in range(board_size):
            board[r].append(0)
    solve()
    print("Total solutions:", solutions)
