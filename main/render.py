import helper, os
import subprocess
from rich import print


# Starts rendering process
def start() -> None:
    # Prepare host for rendering process
    helper.clear_host()

    # Initialize an empty new board
    board: list = helper.empty_board()
    if helper.check_board(board) == False:
        raise ValueError("Empty board from helper invalid inside renderer start")
    helper.print_board(board)

    # Get who starts first
    while True:
        print("[bold cyan]\nWho starts first?[/bold cyan]")
        print("[bold red]X[/bold red]: Minimax (AI Algorithm)")
        print("[bold blue]O[/bold blue]: Human (You)")
        game_starter: str = input("")

        if len(game_starter) != 1 or game_starter.lower() not in ["o", "x"]:
            print("Type [bold red]'X'[/bold red] for Minimax or [bold blue]'O'[/bold blue] for Human (Case insensitive)")
            print("Press [bold]Enter[/bold] to try again")
            tmp_input_buffer = input("")
            helper.clear_host()
            helper.print_board(helper.empty_board())
        else:
            helper.clear_host()
            break
            

    # Get input and execute acoordingly
    while True:
        # Prepare host for new frame
        helper.clear_host()
        helper.print_board(board)

start()
