class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            self._remove(self.dic[key])
        node = Node(key, value)
        self._add(node)
        self.dic[node.key] = node
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
        
    def _add(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p