from py_evil_hangman.game.args import parse_args
from py_evil_hangman.game.game_manager import GameManager

if __name__ == "__main__":
    cfg = parse_args()
    GameManager(True, cfg.dictionary_file, cfg.guesses, cfg.debug).control_loop()
