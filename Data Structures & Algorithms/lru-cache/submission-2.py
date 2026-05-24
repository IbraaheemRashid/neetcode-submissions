class Node:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

        self.prev, self.next = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, prv
        prv.next, nxt.prev = node, node
        
    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if self.cap < len(self.cache):
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]

