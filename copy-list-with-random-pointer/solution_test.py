import unittest
import solution

class TestSolution(unittest.TestCase):
    def equal_list(self, list1, list2):
        ptr1 = list1
        ptr2 = list2

        while True:
            if ptr1 == None and ptr2 == None:
                return True # no more
            if ptr1 == None or ptr2 == None:
                return False # at least one side contains data
            if ptr1.label != ptr2.label:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

    def test_case0(self):
        head = solution.RandomListNode('head')
        node1 = solution.RandomListNode('1')
        node2 = solution.RandomListNode('2')
        node3 = solution.RandomListNode('3')

        # next: head -> 1 -> 2 -> 3
        head.next = node1
        node1.next = node2
        node2.next = node3

        # randon: head-> 3 -> 2 -> 1 -> head
        head.random = node3
        node3.random = node2
        node2.random = node1
        node1.random = head

        sol = solution.Solution()
        copied = sol.copyRandomList(head)

        self.assertTrue(self.equal_list(head, copied))

    def test_case1(self):
        head = solution.RandomListNode('')
        sol = solution.Solution()
        copied = sol.copyRandomList(head)

        self.assertTrue(self.equal_list(head, copied))

    def test_case2(self):
        head = solution.RandomListNode('-1')
        node1 = solution.RandomListNode('1')
        node2 = solution.RandomListNode('#')
        node3 = solution.RandomListNode('#')

        # next: head -> 1 -> 2 -> 3
        head.next = node1
        node1.next = node2
        node2.next = node3

        sol = solution.Solution()
        copied = sol.copyRandomList(head)

        self.assertTrue(self.equal_list(head, copied))

if __name__ == '__main__':
    unittest.main()
