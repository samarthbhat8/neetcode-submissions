class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {} # key : node
        

        self.lru, self.mru = Node(0, 0), Node(0, 0)
        
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def get(self, key: int) -> int:
        if key in self.hashmap:
            
            self.remove(self.hashmap[key])
            self.add(self.hashmap[key])
            
            return self.hashmap[key].val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        
        node = Node(key, value)
            
        self.hashmap[key] = node
        self.add(node)
        
        if len(self.hashmap) > self.capacity:
            LRU = self.lru.next
            self.remove(LRU)
            del self.hashmap[LRU.key]

    def remove(self, node):
        previous = node.prev
        nxt = node.next

        node.next.prev = previous
        previous.next = nxt

    def add(self, node):
        MRU = self.mru.prev
        MRU.next = node
        node.prev = MRU
        self.mru.prev = node
        node.next = self.mru
