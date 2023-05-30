from modules import wordlist, logger

logger = logger.initialize_logger()


class TypingModule:
    '''The core typing module for all typing activities.
    '''
    _TERMINAL_LINE_COUNT = 60

    # line navigation items
    _lines = []

    _wl = []

    def __init__(self):
        wl = wordlist.WordList()
        self._wl = wl.generate_words(400)
        self._lines = self._split_lines()

    def _split_lines(self):
        '''Split words in the wordlist into terminal friendly limits.
        '''

        temp_wl = self._wl.copy()
        count = self._TERMINAL_LINE_COUNT

        lines = []
        line = []

        while len(temp_wl) > 0:
            word = temp_wl.pop()

            if count < len(word):
                lines.append(line.copy())
                line.clear()
                count = self._TERMINAL_LINE_COUNT

            line.append(word)
            count -= len(word)

        return lines

    def _validate_word(
        self,
        usr_input: str,
        line_cur: int,
        word_cur: int
    ) -> bool:
        '''Validation against the specified word in the list.
        Args:
            usr_input: Current user input
            line_cur: Index of line in the line list to compare against
            word_cur: Index of word in the line list to compare against
        Returns:
            Boolean indicating whether the word matches.
        '''
        return self._lines[line_cur][word_cur] == usr_input
