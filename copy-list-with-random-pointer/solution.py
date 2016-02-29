# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def dump(self, head):
        prev = head
        while prev is not None:
            print "label:%s, addr:%s"%(prev.label, prev)

            prev = prev.next
    def dumpRandom(self, head):
        prev = head
        while prev is not None:
            print "[R] label:%s, addr:%s"%(prev.label, prev)
            prev = prev.random

    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        # append each element after a node
        # from: head -> A -> B -> C
        #   to: head -> head' -> A -> A' -> B -> B' -> C -> C'
        if head is None:
            return None

        prev = head
        while prev != None:
            jump_next = prev.next
            newnode = RandomListNode(prev.label)
            newnode.next = prev.next
            prev.next = newnode
            prev = jump_next

        # copy random pointers
        prev = head
        while prev != None:
            newnode = prev.next # newnode should not be nil since #head right now is even number
            if prev.random is not None:
                newnode.random = prev.random.next
            prev = prev.next.next
        # separate two lists
        newhead = head.next # keep track the new head
        prev = head
        while prev != None:
            jump_next = prev.next
            if jump_next is None:
                break
            if prev.next.next is not None:
                prev.next = prev.next.next
            else:
                prev.next = None
            prev = jump_next

        return newhead
