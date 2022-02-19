from cgitb import reset
from collections import defaultdict # You might find this useful
import os

class WordMakerHuman():
    def __init__(self, words_file, debug):
        # we need to prompt the player for a word, then clear the screen so that player 2 doesn't see the word.
        self.debug = debug
        self.words = {} # Make sure to read up the documentation on dictionaries. They will be extremely useful for this project.
        with open(words_file) as wordfile:
            for line in wordfile:
                word = line.strip()
                if len(word) > 0:
                    self.words[word] = True

    def reset(self, word_length):
        question = ""
        while True:
            question = input(f"Please type in your word of length {word_length}: ")
            if question in self.words and len(question) == word_length:
                break
            print("Invalid word.")
        if not self.debug:
            os.system("clear||cls") # clear the terminal
        self.word = question

    def getValidWord(self):
        return self.word

    def getAmountOfValidWords(self):
        return 1 # the only possible word is self.word

    def guess(self, guess_letter):
        idx = self.word.find(guess_letter)
        ret = []
        while idx != -1:
            ret.append(idx)
            idx = self.word.find(guess_letter, idx + 1)
        return ret




class WordMakerAI():
    def __init__(self, words_file, debug):
        # read in the words into any data structures you see fit
        # input format is a file of words separated by newlines
        # use open() to open the file, and remember to split up words by word length!
        # DO NOT print anything unless debug is set to true

        # You can optionally save and use the `debug` parameter to control your own print statements within the game loop.

        # Use this code if you like.
        """
        with open(words_file) as file_obj:
            for line in file_obj:
                word = line.strip()
                # Use word
        """
        self.activeDictionary = {}
        self.words = {} # Make sure to read up the documentation on dictionaries. They will be extremely useful for this project.
        with open(words_file) as wordfile:
            for line in wordfile:
                word = line.strip()
                if len(word) > 0:
                    self.words[word] = True

        # while True:
        #     try:
        #         wordLength = int(input("What shoud the word length be"))
        #     except ValueError:
        #         print('Invalid input')

    def reset(self, word_length):
        # start a new game with a word length of `word_length`. 
        # This will always be called before guess() or getValidWord() are called.
        # this function should be O(1). 
        # That is, you shouldn't have to process over the entire dictionary here 
        # (find somewhere else to preprocess it)
        # DO NOT print anything unless debug is set to true on object initialization

        newDictionary = self.new_dictionary(word_length)
        print(newDictionary)
        return newDictionary
        
        
        # pass # TODO: implement this

    def getValidWord(self):
        
        # get a valid word in the active dictionary, to return when you lose
        # can return any word, as long as it satisfies the previous guesses
        # DO NOT print anything unless debug is set to true on object initialization
        self.word = 'there'
        activeDictionary = self.updatedDictionary
        if (self.word in activeDictionary):
            return self.word
            
        else:
            pass

            
    def getAmountOfValidWords(self):
        # get the total amount of words that satisfy all the guesses since self.reset was called
        # should be O(1)
        # Note: This is used extensively in the autograder! Make sure this works! Here's an example input to verify:
            # With a word length of 5, after guessing "a, e, i, o, u", you should see 301 remaining words.
            # You can see this number by running with the debug flag, i.e. `python3 evil_hangman.py --debug`
        # DO NOT print anything unless debug is set to true on object initialization

        remaining_words = len(self.updatedDictionary)
        print(remaining_words)
        
        return remaining_words
        

    def guess(self, guess_letter):
        
        # update your data structures and find the longest set of words with the given guess
        # should return the list of positions in which the letter was found
        #  That is, if the guess is "a" and the words left are ["ah", "ai", "bo"], then we should return [0], because
        #  we are picking the family of words with an "a" in the 0th position. If this function decides that the biggest family
        #  has no a's, then we'd return [].

        # in the case of a tie (multiple families have the same amount of words), should pick the set of words with fewer guess_letter's
        #  That is, if the guess is "a" and the words left are ["ah", "hi"], we should return [] (picking the set ["hi"]), 
        #  since ["hi"] and ["ah"] are equal length and "hi" has fewer a's than "ah".
        # if both sets have an equal number of guess_letter's, then it is ok to pick either.
        #  For example, if the guess is "a" and the words left are ["aha", "haa"], you can return either [0, 2] or [1, 2].

        # The order of the returned list does not matter. You can assume that 'guess_letter' has not been seen yet since the last call to self.reset(),
        #  and that guess_letter has len of 1 and is a lowercase a-z letter.
        # DO NOT print anything unless debug is set to true on object initialization
        
        letter_positions = []
        
        dictionary_with_letter = {word: True for word in self.activeDictionary if guess_letter in word}
        dictionary_without_letter = {word: True for word in self.activeDictionary if guess_letter not in word}
        
        if len(dictionary_with_letter) > len(dictionary_without_letter):
            return dictionary_with_letter
        else:
            return dictionary_without_letter
        
        
        
        pass # TODO: implement this

    def new_dictionary(self, word_length):
        self.updatedDictionary = {x: True for x in self.words if len(x) == int(word_length)}
        
        self.activeDictionary = self.updatedDictionary
        
        return self.updatedDictionary
    
    # def active_dictionary(self, words):
    #     self.activeDictionary = self.updatedDictionary
        
    #     return self.activeDictionary    