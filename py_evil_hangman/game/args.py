import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f", "--dictionary-file", type=str, default="dictionary.txt", help="Path to the dictionary file."
    )
    parser.add_argument(
        "-g", "--guesses", type=int, default="10", help="How many guesses you get."
    )
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug info (words left).")

    return parser.parse_args()
