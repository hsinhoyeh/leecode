class Solution(object):

    def word_count(self, words):
        word_hash = {}
        for word in words:
            self.word_count_to(word_hash, word)
        return word_hash

    def word_count_to(self, word_hash, word):
        if word not in word_hash:
            word_hash[word] = 1
        else:
            word_hash[word] = word_hash[word] + 1

    def word_count_sub(self, word_hash, word):
        if word not in word_hash:
            return
        if word_hash[word] == 1:
            del word_hash[word]
        else:
            word_hash[word] = word_hash[word] - 1

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        word_hash = self.word_count(words)

        results = []
        num_words = len(words)
        len_word = len(words[0])
        window_size = num_words * len(words[0])
        if window_size > len(s):
            return []

        # aligned_offset let you shift a certain offset to get incremental update words
        # ex: len_word = 4, s=10
        # you will get the following offset
        # 0, 4, 8
        # 1, 5, 9
        # 2, 6, 10
        # 3, 7
        for aligned_offset in range(0, len_word):
            aligned_end = aligned_offset + len_word * int((len(s) - aligned_offset ) / len_word)

            project_words = []
            projected_s = s[aligned_offset:aligned_end]

            # generate all words
            for idx in range(0, len(projected_s), len_word):
                key = projected_s[idx: idx + len_word]
                project_words.append(key)

            is_inited = False
            pw_hash = {}
            for pw_idx in range(0,len(project_words)-num_words+1):
                if not is_inited:
                    is_inited = True
                    pw_hash = self.word_count(project_words[0: num_words]) # build init set
                else:
                    # incremental update by adding the last one
                    self.word_count_to(
                            pw_hash,
                            project_words[pw_idx + num_words-1])

                # if both hash are matched, output the offset
                if word_hash == pw_hash:
                    results.append(pw_idx * len_word + aligned_offset)
                # incremental update by deleting current one
                self.word_count_sub(pw_hash, project_words[pw_idx])

        return sorted(results)
