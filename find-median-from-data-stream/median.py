class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []
        self.right = []
        self.count = 0 # total number of elements
        self.last_update_count = 0
        self.median = 0


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        self.count += 1
        if num > self.median:
            self.right.append(num)
            return
        self.left.append(num)
        return

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """

        if self.count == 0:
            return 0
        if self.count == 1:
            if not self.left:
                return self.right[0]
            return self.left[0]

        medpos = 0
        tested_even = (self.count % 2) != 1

        if not tested_even:
            medpos = (self.count+1) / 2
        else:
            medpos = int(self.count / 2)
        #print "medpos:%d, tested:%d" %(medpos, tested_even)
        results = self.check_median(medpos, tested_even)
        #print "results"
        #print results
        median = self.gen_median(results)
        self.redistribute(median)
        #print "left"
        #print self.left
        #print "right"
        #print self.right
        return median

    def redistribute(self, median):
        if self.idx_or_notfound(self.left, -1) < median:
            # move data from right to left
            while self.idx_or_notfound(self.right, 0) < median:
                self.left.append(self.right.pop(0))
            return
        while self.idx_or_notfound(self.left, -1) > median:
            self.right.append(self.left.pop())

    def idx_or_notfound(self, lst, idx):
        if not lst:
            return -1
        return lst[idx]

    def gen_median(self, candidates):
        if len(candidates) == 1:
            return candidates[0]
        return float(candidates[0] + candidates[1]) / 2

    def check_median(self, medpos, tested_even):
        # check the left side
        # if medpos = 2, len(left) == 0
        # we only need to check right
        len_left = len(self.left)
        len_right = len(self.right)

        #print "left"
        #print self.left
        #print "right"
        #print self.right


        if  len_left == 0 or len_left < medpos:
            #print "case1"
            self.right.sort(key=lambda x: x)  # aesc
            offset = medpos - len_left - 1
            #print "offset:%d" %offset
            #print "tested_even:%s" %tested_even
            #print "right: %s" %self.right
            if tested_even:
                #print "ret1"
                return self.right[offset:offset+2]
            else:
                #print "ret2"
                return [self.right[offset]]

        elif len_right == 0 or len_right < medpos:
            #print "case2"
            self.left.sort(key=lambda x: -x)  # desc
            offset = medpos - 1
            #print "offset:%d" %offset
            #print "tested_even:%s" %tested_even
            #print "right: %s" %self.left
            if tested_even:
            #    print "ret1"
                return self.left[offset:offset+2]
            else:
            #    print "ret2"
                return [self.left[offset]]

        else: # median is in between
            self.right.sort(key=lambda x: x)  # aesc
            self.left.sort(key=lambda x: -x)  # desc
            return [self.left[-1], self.right[0]]

        return None

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
