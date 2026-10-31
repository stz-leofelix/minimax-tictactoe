import main.helper as helper, main.brain as brain, sys


def main():
    # If the given argument is incorrect
    if len(sys.argv) != 1:
        print("Usage: py tictactoe.py", file=sys.stderr)
