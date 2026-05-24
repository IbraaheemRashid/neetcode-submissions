class Node:

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # store capacity
        self.cap = capacity
        # store each value
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
        prv, nxt = self.right.prev, self.right
        node.prev, node.next = prv, nxt
        prv.next, nxt.prev = node, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if len(self.cache) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]
