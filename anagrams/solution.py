class Solution(object):

    def signature(self, astr):
        return ''.join(sorted(astr))

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sigtowords = {}
        for astr in strs:
            sig = self.signature(astr)
            if sig not in sigtowords:
                sigtowords[sig] = []
            sigtowords[sig].append(astr)

        ret = []
        # sort each inner list
        for k in sigtowords.keys():
            ret.append(sorted(sigtowords[k]))
        return ret
