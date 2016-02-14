import heapq

class MaxQueue:
    queue = []

    def __init__(self):
        self.queue= []

    def push(self, item):
        heapq.heappush(self.queue, -item)

    def pop(self):
        return -heapq.heappop(self.queue)

    def getN(self, n):
        # NOTE: nsmallest will be buttleneck in OJ.
        # if we want to access the smallest element, use queue[0] instead
        if n ==1:
            l = self.queue[:1]
        else:
            l = heapq.nsmallest(n, self.queue)
        return [-e for e in l]

    def capacity(self):
        return len(self.queue)

class MinQueue:
    queue = []

    def __init__(self):
        self.queue= []

    def push(self, item):
        heapq.heappush(self.queue, item)

    def pop(self):
        return heapq.heappop(self.queue)

    def getN(self, n):
        if n ==1:
            return self.queue[:1]
        else:
            return heapq.nsmallest(n, self.queue)

    def capacity(self):
        return len(self.queue)

class MedianFinder:

    min_q = None
    max_q = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.min_q = MinQueue()
        self.max_q = MaxQueue()

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """

        # balance two heap structure
        self.max_q.push(num)
        self.min_q.push(self.max_q.pop())
        while self.max_q.capacity() < self.min_q.capacity():
            self.max_q.push(self.min_q.pop())

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return self._findMedian()

    def _findMedian(self):
        if self.max_q.capacity() == self.min_q.capacity():
            return (self.max_q.getN(1)[0] + self.min_q.getN(1)[0]) / float(2.0)
        return self.max_q.getN(1)[0]



# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
