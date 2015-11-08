class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList:
    # head -> None
    # tail -> Head
    # list: least used(front) -> ... -> ... -> the most recent used(back)
    def __init__(self):
        self.head = LinkedNode()
        self.tail = self.head

    def push_back(self, node):
        self.tail.next = node
        self.tail = self.tail.next

    def pop_front(self):
        # if no elements in the list, return None
        if self.head.next is None:
            return None
        # drop_ele is the element to be dropped
        drop_ele = self.head.next

        # from: head -> dropped_ele -> next element
        # to: head -> next element or head -> None
        if self.head.next.next is not None:
            self.head.next = self.head.next.next
        else:
            self.head.next = None
        return drop_ele

    # dump is a debug function used to list the whole linkedlist
    def dump(self, node=None):
        p = node
        if p is None:
            p = self.head

        while p is not None:
            p = p.next

    # ls_last_ele tests prev.next is the last element in the list
    def is_last_ele(self, prev=None):
        if prev.next.next is None:
            return True
        return False

    # prev is previous node
    def move_back(self, prev=None):
        # from: head -> a -> b -> c
        # to: head -> a -> c -> b
        # where prev = a

        if self.is_last_ele(prev):
            return 

        node = prev.next
        prev.next = prev.next.next
        node.next = None
        self.push_back(node)
        return 

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # keped with node.key, valus is one step before the element
        # i.e. hash[$key].next.value = $value
        self.hash = {}
        self.llist = LinkedList()
        self.capacity = capacity

    def push_back(self, node):
        self.hash[node.key] = self.llist.tail
        self.llist.push_back(node)

    def pop_front(self):
        head = self.llist.pop_front()
        if head is None:
            return

        del self.hash[head.key]
        # update hash map of the next element of head,
        # since it depends on me to refer its value
        self.hash[head.next.key] = self.llist.head

    def move_back(self, prev):
        # if we are going to move the last element to back
        # do nothing
        if self.llist.is_last_ele(prev):
            return

        # handle myself since it's hash contains my data
        self.hash[prev.next.key] = self.llist.tail
        # update next one
        if prev.next.next is not None:
            self.hash[prev.next.next.key] = prev

        # move myself to back
        self.llist.move_back(prev)

    # dumphash is a debug tool to list all elements in the hashmap
    def dumphash(self):
        print "====start dumphsah ======"
        for k in self.hash.keys():
            print "k:%s, v:%s" %(k, self.hash[k].next.value)
        print "====end dumphsah ======"

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.hash:
            return -1

        prev = self.hash[key]
        val = prev.next.value
        self.move_back(prev)
        return val

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """

        if key in self.hash:
            prev = self.hash[key]
            prev.next.value = value # only update value
            self.move_back(prev)
            return

        node = LinkedNode(key, value)
        self.push_back(node)
        if len(self.hash) > self.capacity:
            self.pop_front()

