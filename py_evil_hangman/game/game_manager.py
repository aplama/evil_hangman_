from py_evil_hangman.word_maker import WordMakerAI, WordMakerHuman
from py_evil_hangman.word_guesser import WordGuesserHuman

MIN_WORD_LEN = 2
MAX_WORD_LEN = 20

class GameManager():
    def __init__(self, ai, words_file, guesses, debug):
        self.starting = guesses
        if ai:
            self.word_maker = WordMakerAI(words_file, debug)
        else:
            self.word_maker = WordMakerHuman(words_file, debug)
        self.word_guesser = WordGuesserHuman(guesses, words_file, debug)
        self.ai = ai
        self.debug = debug
    def check_implementations(self):
        # test_adv = WordMakerAI("py_evil_hangman/game/init_dict.txt", True)
        test_adv = WordMakerAI("dictionary.txt", True)
        test_adv.reset(5)
        wordAttempt = test_adv.getValidWord()
        if type(wordAttempt) is not str or len(wordAttempt) != 5:
            print("WARNING: WordMakerAI.getValidWord() is not implemented yet. Don't forget to implement this!")
        lengthAttempt = test_adv.getAmountOfValidWords()
        if type(lengthAttempt) is not int or lengthAttempt <= 0:
            print("WARNING: WordMakerAI.getAmountOfValidWords() is not implemented yet. Don't forget to implement this!")
        guessAttempt = test_adv.guess("-")
        if type(guessAttempt) is not list or guessAttempt != []:
            print("WARNING: WordMakerAI.guess() doesn't seem to be implemented yet. The game will likely crash.")

    def control_loop(self):
        if self.ai:
            self.check_implementations()
        while True:
            print("Let's play hangman!")
            while True:
                numS = input(f"How many characters should my word be? ({MIN_WORD_LEN}-{MAX_WORD_LEN}): ")
                try:
                    num = int(numS)
                    if num >= MIN_WORD_LEN and num <= MAX_WORD_LEN: break
                except:
                    pass
            self.run_game(num)
            ans = input("Would you like to play again? (y/n):")
            while ans not in ["y", "n"]:
                ans = input("Would you like to play again? (y/n):")
            if ans == "n": break

    def run_game(self, word_length):
        self.word_maker.reset(word_length)
        self.word_guesser.reset(word_length)

        while True:
            if self.word_guesser.state.guesses == 0:
                print(f"You lose! The word was {self.word_maker.getValidWord()}.")
                break
            self.word_guesser.state.print_state(self.word_maker.getAmountOfValidWords())
            inp = self.word_guesser.getGuess()
            letter_positions = self.word_maker.guess(inp)
            letter_count = len(letter_positions)
            s = "s" if letter_count != 1 else ""
            print(f"Found {letter_count} '{inp}'{s}")

            self.word_guesser.state.guesses -= 1 if letter_count == 0 else 0
            self.word_guesser.state.guessed.append(inp)
            for i in letter_positions:
                self.word_guesser.state.word[i] = inp

            self.word_guesser.state.done_letters += letter_count
            if self.word_guesser.state.done_letters == word_length:
                left = self.starting - self.word_guesser.state.guesses
                es = "es" if left != 1 else ""
                print(f"You win in {left} incorrect guess{es}!")
                print("The word was {}".format("".join(self.word_guesser.state.word)))
                break
