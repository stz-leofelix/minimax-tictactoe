import sys, helper


def board_win_condition(board: list) -> int:
    # Check for horizontal and vertical wins
    for i in [1, 2, 3]:
        if (
            "".join(helper.board_row(board, i)) == "xxx"
            or "".join(helper.board_column(board, i)) == "xxx"
        ):
            return 10
        elif (
            "".join(helper.board_row(board, i)) == "ooo"
            or "".join(helper.board_column(board, i)) == "ooo"
        ):
            return -10

    # Check for diagonal wins
    for i in range(2):
        # Check for top left to bottom right win
        diagonal_board: list = []
        diagonal_board.append(helper.board_row(board, 1)[0])
        diagonal_board.append(helper.board_row(board, 2)[1])
        diagonal_board.append(helper.board_row(board, 3)[2])
        if "".join(diagonal_board) == "xxx":
            return 10
        elif "".join(diagonal_board) == "ooo":
            return -10

        # Check for top right to botoom left win
        diagonal_board: list = []
        diagonal_board.append(helper.board_row(board, 1)[2])
        diagonal_board.append(helper.board_row(board, 2)[1])
        diagonal_board.append(helper.board_row(board, 3)[0])
        if "".join(diagonal_board) == "xxx":
            return 10
        elif "".join(diagonal_board) == "ooo":
            return -10

    # Check for ties
    if "-" not in board:
        return 0

    return 99999999999999999999999999999999999999999


def make_turn():
    pass
