import datetime
import os
import random

DICTIONARY_901_COMMON = 'wordlist901'

class WordList:
    _dict = {}

    def __init__(self):
        '''Loads the wordlist if it's not loaded yet.
        '''

        if len(self._dict) == 0:
            script_dir = os.path.dirname(os.path.realpath(__file__))

            # set an arbitrary path for the dictionaries for different dicts in the future
            dict_dir = os.path.join(script_dir, 'dictionaries', DICTIONARY_901_COMMON)

            with open(dict_dir, 'r') as f:
                self._dict = set(f.read().splitlines())

    def generate_words(
        self, 
        num_words: int
    ) -> list[str]:
        '''Generate a set number of words from the internal dictionary
        based off the current timestamp as a seed.
        Args: 
            num_words: Number of words to generate.
        Returns:
            A list of <num_words> strings.
        '''

        random.seed(str(datetime.datetime.now()))
        word_list = []

        for _ in range(num_words):
            word_list.append(random.choice(list(self._dict)))
        
        return word_list