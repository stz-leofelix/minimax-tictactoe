from rich import print
import sys


def translate_coordinate(coordinate: str) -> int:
    # If the length of the coordinate is invalid
    if len(coordinate) != 2:
        raise ValueError("Coordinate length invalid")

    # Change the coordinate to lower case
    coordinate = coordinate.lower()

    # Validate coordinate
    for index in range(len(coordinate)):
        # If the character is out of range
        if coordinate[index] not in ["a", "b", "c", 1, 2, 3]:
            raise IndexError("Coordinate index out of range")
        # If the first index is not a character
        if index == 0 and not isinstance(coordinate[index], str):
            raise ValueError("Coordinate invalid at index 0")
        # If the second index is not an integer
        elif index == 1:
            try:
                int(coordinate[index])
            except ValueError:
                raise ValueError("Coordinate invalid at index 1")

    # Perform calculation to get the position
    position: int = (ord(coordinate[0]) * 3) + int(coordinate[1])

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


# Clear host terminal screen instantly using ANSI escape codes
def clear_host() -> None:
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()
