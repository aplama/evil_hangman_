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
        with open(words_file) as wordfile: # Load a dictionary from 'words_file'
            for line in wordfile:
                word = line.strip() # Strip new line escape after each word
                if len(word) > 0:
                    self.words[word] = True # Add each word to 'self.words' dictionary

    
    def reset(self, word_length):
        # start a new game with a word length of `word_length`. 
        # This will always be called before guess() or getValidWord() are called.
        # this function should be O(1). 
        # That is, you shouldn't have to process over the entire dictionary here 
        # (find somewhere else to preprocess it)
        # DO NOT print anything unless debug is set to true on object initialization

        self.new_dictionary(word_length) # Create a new dictionary of word length 'word_length' via 'new_dictionary()' function
        

    def getValidWord(self):
        
        # get a valid word in the active dictionary, to return when you lose
        # can return any word, as long as it satisfies the previous guesses
        # DO NOT print anything unless debug is set to true on object initialization
        
        correct_word = ''
        
        for word in self.activeDictionary:
            if self.activeDictionary[word] == True: # Take a first word that matches value True
                correct_word = word # Update correct word
                break # Exit loop
        
        return correct_word

            
    def getAmountOfValidWords(self):
        # get the total amount of words that satisfy all the guesses since self.reset was called
        # should be O(1)
        # Note: This is used extensively in the autograder! Make sure this works! Here's an example input to verify:
            # With a word length of 5, after guessing "a, e, i, o, u", you should see 301 remaining words.
            # You can see this number by running with the debug flag, i.e. `python3 evil_hangman.py --debug`
        # DO NOT print anything unless debug is set to true on object initialization

        remaining_words = len(self.activeDictionary) # Get a length of the 'active_dictionary' and return it
        
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
        
        # Initialize helper lists and dictionaries
        reduced_sample = {}
        letter_positions = {}
        postions_list = []
        no_duplicates_list = []
        positions_occurances = {}
        max_positions_occurance = 0
        
        with_letter_dict = {word:True for word in self.activeDictionary if guess_letter in word} # Create a dictionary of words that contain the 'guess_letter'
        without_letter_dict = {word:True for word in self.activeDictionary if guess_letter not in word} # Create a dictionary of words that do not contain the 'guess_letter'
        
        for word in with_letter_dict:
            letter_positions[word] = [pos for pos, char in enumerate(word) if char == guess_letter] # Check position of the letter in each word
        
        for i in letter_positions:
            postions_list.append(letter_positions[i]) # Create a list of all positions
            
        for i in postions_list:
            if i not in no_duplicates_list:
                no_duplicates_list.append(i) # Convert list of all positions into a set
                
        for i in no_duplicates_list:
            positions_occurances[tuple(i)] = postions_list.count(i) # Create a dict of all postions and occurances
            

        max_positions_occurance = max(positions_occurances.values(), default=0) # Get the max occurance
        
        if len(without_letter_dict) >= max_positions_occurance: # Will continue with words that do not contain letter
            self.activeDictionary = without_letter_dict # Update active_dictionary with remaining words
            return [] # Also return empty set.      
        
        else: # Will continue with words that do contain letter
            postion_set = [] # Initialize empty set
            
            for i in positions_occurances:
                if positions_occurances[i] == max_positions_occurance:
                    postion_set += i
                
                    reduced_sample = {word: True for word in letter_positions if letter_positions[word] == postion_set}
                    self.activeDictionary = reduced_sample # Update active_dictionary with remaining words
                    break
                
            return postion_set # Return list of positions

    
    def new_dictionary(self, word_length):
        updatedDictionary = {x: True for x in self.words if len(x) == int(word_length)}
        
        self.activeDictionary = updatedDictionary
        