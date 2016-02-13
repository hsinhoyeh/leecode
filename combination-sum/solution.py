class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # so candidates are well ordered, like 1,2,3,4,...
        candidates = sorted(candidates)
        result_set = set()

        # do a quick pruning, if candidate > target, it won't go any further
        index = 0
        for index in range(0, len(candidates)):
            candidate = candidates[index]
            if candidate == target:
                result_set.add((candidate,))
            if candidate > target: # pruning starts from here
                break
        self.dfs(candidates[:index+1], target, [], result_set)

        ret = []
        for result in result_set:
            ret.append(list(result))
        return ret


    def dfs(self, candidates, target, path, result_set):
        if not candidates:
            return
        if target < candidates[0]: # no need to go further
            return
        self.pick(candidates, target, list(path), result_set)
        self.drop(candidates, target, list(path), result_set)

    # pick the first element
    def pick(self, candidates, target, path, result_set):
        first = candidates[0]
        target = target - first
        path.append(first)
        if target == 0:
            result_set.add(tuple(path))

        self.dfs(candidates, target, path, result_set)

    # drop the first element
    def drop(self, candidates, target, path, result_set):
        self.dfs(candidates[1:], target, path, result_set)

