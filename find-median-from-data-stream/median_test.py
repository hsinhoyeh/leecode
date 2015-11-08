import unittest
import median

class TestMedianestCase(unittest.TestCase):
    def test_case0(self):
        mf = median.MedianFinder()
        mf.addNum(0)
        mf.addNum(0)
        self.assertEqual(0, mf.findMedian())

    def test_case1(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        self.assertEqual(1, mf.findMedian())

    def test_case2(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        self.assertEqual(1.5, mf.findMedian())

    def test_case3(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())

    def test_case4(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        mf.addNum(3)
        mf.addNum(1)
        mf.addNum(1)
        self.assertEqual(1, mf.findMedian())

    def test_case5(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        mf.addNum(3)
        mf.addNum(3)
        mf.addNum(3)
        self.assertEqual(3, mf.findMedian())

    def test_case6(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())
        mf.addNum(3)
        mf.addNum(3)
        self.assertEqual(3, mf.findMedian())

    def test_case7(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        mf.addNum(2)
        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())
        mf.addNum(3)
        mf.addNum(3)
        self.assertEqual(3, mf.findMedian())
        mf.addNum(1)
        mf.addNum(1)
        mf.addNum(1)
        mf.addNum(1)
        self.assertEqual(1, mf.findMedian())


    def test_case8(self):
        mf = median.MedianFinder()
        mf.addNum(-1)
        self.assertEqual(-1, mf.findMedian())
        mf.addNum(-2)
        self.assertEqual(-1.5, mf.findMedian())
        mf.addNum(-3)
        self.assertEqual(-2, mf.findMedian())
        mf.addNum(-4)
        self.assertEqual(-2.5, mf.findMedian())
        mf.addNum(-5)
        self.assertEqual(-3, mf.findMedian())


    def test_case9(self):
        mf = median.MedianFinder()
        mf.addNum(1)
        self.assertEqual(1, mf.findMedian())
        mf.addNum(2)
        self.assertEqual(1.5, mf.findMedian())
        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())
        mf.addNum(4)
        self.assertEqual(2.5, mf.findMedian())
        mf.addNum(5)
        self.assertEqual(3, mf.findMedian())



if __name__ == '__main__':
        unittest.main()
