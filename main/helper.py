from rich import print
import sys


def translate_coordinate(coordinate: str) -> int:
    # Check if the coordinate is valid
    if check_coordinate(coordinate) is not True:
        raise ValueError("Coordinate invalid")
    # Change the coordinate to lower case
    coordinate = coordinate.lower()

    # Perform calculation to get the position
    position: int = ((ord(coordinate[0]) - 97) * 3) + int(coordinate[1]) - 1

    return position


def print_board(board: list) -> None:
    # Check if the board is correct
    if check_board(board) is not True:
        raise ValueError("Invalid board given")

    # Prepare position anchor
    print("[bold black]  1   2   3[/bold black]")
    row_character_ascii: int = ord("A")

    # Print the board
    for row in [1, 2, 3]:
        printed_divider_count = 0
        print(f"[bold black]{chr(row_character_ascii)}[/bold black] ", end="")
        for cell in board[row * 3 - 3 : row * 3]:
            # Print the cell
            match cell:
                case "o":
                    print("[bold blue]O[/bold blue]", end="")
                case "x":
                    print("[bold red]X[/bold red]", end="")
                case "-":
                    print("-", end="")

            # Print divider
            if printed_divider_count < 2:
                print("[black] | [/black]", end="")
                printed_divider_count += 1
        print()
        row_character_ascii += 1


# Checks if the given board is correct, if so returns True else False
def check_board(board: list) -> bool:
    # Check if the size of the board is correct
    if len(board) != 9:
        return False

    # Check if all cell in board is correct
    for cell in board:
        if not isinstance(cell, str):
            return False
        elif not cell in ["o", "x", "-"]:
            return False

    # Indicate valid board
    return True


def empty_board() -> list:
    return ["-", "-", "-", "-", "-", "-", "-", "-", "-"]


def check_coordinate(coordinate: str) -> bool:
    # If the length of the coordinate is invalid
    if len(coordinate) != 2:
        return False

    # Validate coordinate
    for index in range(2):
        # If the character is out of range
        if coordinate[index].lower() not in ["a", "b", "c", "1", "2", "3"]:
            return False
        # If the first index is not a character
        if index == 0 and not isinstance(coordinate[index], str):
            return False
        # If the second index is not an integer
        elif index == 1:
            # try:
            int(coordinate[index])
            # except ValueError:
            # return False

    # All tests passed
    return True


# Clear host terminal screen instantly using ANSI escape codes
def clear_host() -> None:
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()


# Place a mark on the board made by a play
def place_play(board: list, coordinate: str, player: str) -> None:
    # Check if the coordinate is valid
    if check_coordinate(coordinate) is False:
        raise ValueError("Coordinate invalid")

    # Check if the board is valid
    if check_board(board) is False:
        raise ValueError("Board invalid")

    # Check if the player is valid
    if len(player) != 1 or player.lower() not in ["o", "x"]:
        raise ValueError("Player invalid")

    # Check if a play have been already made in the respective cell
    if board[translate_coordinate(coordinate)] != "-":
        raise ReferenceError("Play have been already made in the according cell")

    # Place the play on board
    board[translate_coordinate(coordinate)] = player.lower()


# Give part of a board by it's row
def board_row(board: list, row: int) -> list:
    # Check if the board is correct
    if check_board(board) is not True:
        raise ValueError("Board inavlid")

    # Check if the row is correct
    if row not in [1, 2, 3]:
        raise ValueError(f"Row invalid, accessing invalid row at {row}")

    # Give the sliced row
    return board[row * 3 - 3 : row * 3]


# Give part of a board by it's column
def board_column(board: list, column: int) -> list:
    # Check if the board is correct
    "Error check handled by board_row() called later"

    # Check if the column is correct
    if column not in [1, 2, 3]:
        raise ValueError(f"Row invalid, accessing invalid column at {column}")

    # Get the sliced column
    sliced_column: list = []
    for i in range(3):
        sliced_column.append(board_row(board, i)[column - 1])

    # Return the sliced column
    return sliced_column
