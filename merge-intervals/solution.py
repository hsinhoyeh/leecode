class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution(object):
    def max(self, v1, v2):
        if v1 > v2:
            return v1
        return v2

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        # sort first and then merge
        if not len(intervals):
            return []

        s_intervals = sorted(intervals, key=lambda interval: interval.start)

        results = []
        current_interval = s_intervals[0]

        for i in range(1, len(s_intervals)):
            next_interval = s_intervals[i]

            if next_interval.start <= current_interval.end:
                # should be merged
                current_interval.end = self.max(current_interval.end, next_interval.end)
            else:
                # stash the current one and move on
                results.append(current_interval)
                current_interval = next_interval

        # append the last one
        results.append(current_interval)
        return results

