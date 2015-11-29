class WordDictionary(object):

    char_to_word_set = {}
    key_matched_all = '.'

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.char_to_word_set = {}
        self.char_to_word_set[self.key_matched_all] = set()

    def char_index_keyed(self, char, index):
        return "%c:%d"%(char,index)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """

        # keyed $char:$index to $word
        for char_index in range(0, len(word)):
            char = word[char_index]
            key = self.char_index_keyed(char, char_index)
            if key not in self.char_to_word_set:
                self.char_to_word_set[key] = set()
            self.char_to_word_set[key].add(word)

        # keyed word itself
        key = word
        if key not in self.char_to_word_set:
            self.char_to_word_set[key] = set()
        self.char_to_word_set[key].add(word)

        # keyed len(word) and wildcard
        key = self.char_index_keyed(self.key_matched_all, len(word))
        if key not in self.char_to_word_set:
            self.char_to_word_set[key] = set()
        self.char_to_word_set[key].add(word)

    def contain_wildcard(self, word):
        return -1 != word.find(self.key_matched_all)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        if not self.contain_wildcard(word):
            if word not in self.char_to_word_set:
                return False
            return True

        # if contain wildcard, we start from join
        intsect = None
        for char_index in range(0, len(word)):
            char = word[char_index]
            if char == self.key_matched_all:
                key = self.char_index_keyed(self.key_matched_all, len(word))
            else:
                key = self.char_index_keyed(char, char_index)

            if key not in self.char_to_word_set:
                return False

            if intsect == None:
                intsect = self.char_to_word_set[key]
            else:
                intsect = intsect.intersection(self.char_to_word_set[key])
            if len(intsect) == 0:
                return False
        return True
