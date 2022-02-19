import unittest
import os
from word_maker import WordMakerAI

path_to_file = "C:\\Users\\andre\\dev\\Python Projects\\evil_hangman_\\dictionary.txt"
path_to_test = "C:\\Users\\andre\\dev\\Python Projects\\evil_hangman_\\py_evil_hangman\\game\\init_dict.txt"

class TestWordMakerAI(unittest.TestCase):
  
  def test_dict(self):
    words_list = WordMakerAI(path_to_file, False).words
    self.assertTrue('aa' in words_list and '45678' not in words_list)
  
  def test_reset(self):
    word_maker = WordMakerAI(path_to_test, False)
    words = word_maker.new_dictionary(5)
    self.assertTrue('there' in words)
    
if __name__ == '__main__':
  unittest.main()

 