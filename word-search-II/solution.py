class Trace(object):
    lst = []
    hash = {}

    def __init__(self, trace=None, lst=None):
        if not trace and not lst:
            self.lst = []
            self.hash = {}

        if trace:
            self.lst = list(trace.lst)
            self.hash = dict(trace.hash)
            return

        # else generate hash from lst
        self.lst = []
        self.hash = {}
        self.lst = lst
        for tpos in lst:
            key = self.key(tpos)
            self.hash[key] = True

    def key(self, element):
        return "r:%dc:%d"%(element['r'], element['c'])

    def append(self, element):
        self.lst.append(element)
        self.hash[self.key(element)] = True

    def contains(self, element):
        return self.key(element) in self.hash

class Solution(object):

    # return map['c'] = [(row, col)]
    def char_position(self, board, chars):
        char_pos = {}
        for c in chars:
            char_pos[c] = []

        for row_index in range(0, len(board)):
            for col_index in range(0, len(board[0])):
                c = board[row_index][col_index]
                if c in char_pos.keys():
                    char_pos[c].append({'r': row_index, 'c': col_index})
        return char_pos

    # remove current_pos if it occurs in any point of trace
    def remove_cycle(self, trace, candidates):
        ret = []
        for pos in candidates:
            if not trace.contains(pos):
                ret.append(pos)
        return ret

    def test_continueous_position(self, word, char_map):
        word_root_pos = char_map[word[0]]
        traces = []
        next_traces = []
        for pos in word_root_pos:
            traces.append(Trace(lst=[pos]))

        for char_index in range(1, len(word)):
            next_pos = char_map[word[char_index]]
            if not traces:
                return False

            for trace in traces:
                last_position = trace.lst[len(trace.lst)-1]
                candidate_next_moves = self.test_next_move(last_position, next_pos)
                candidates = self.remove_cycle(trace, candidate_next_moves)
                if not candidates:
                    continue
                # generate multiple traces
                for can in candidates:
                    next_trace = Trace(trace=trace)
                    next_trace.append(can)
                    next_traces.append(next_trace)

            traces = next_traces
            next_traces = []
        if not traces:
            return False
        return True

    def test_next_move(self, ppos, my_poss):
        matched = []
        for mpos in my_poss:
            if ppos['c'] == mpos['c']: # same col
                left, right = ppos['r'] -1, ppos['r']+1
                if left == mpos['r'] or right == mpos['r']:
                    matched.append(mpos)
            if ppos['r'] == mpos['r']: # same row
                up, down = ppos['c'] -1, ppos['c']+1
                if up == mpos['c'] or down == mpos['c']:
                    matched.append(mpos)

        #return {prefix: matched}
        return matched

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        # append all words, then we only need to generate char position once
        universal_word = ""
        for word in words:
            universal_word += word

        char_map = self.char_position(board, universal_word)

        ret = []
        for word_index in range(0, len(words)):
            word = words[word_index]
            for char in char_map:
                if not char_map[char]:
                    break
            if not self.test_continueous_position(word, char_map):
                continue
            ret.append(word)
        return ret
