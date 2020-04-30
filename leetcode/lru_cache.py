class LRUCache:
    def __init__(self, capacity: int):
        self.valdict = {}
        self.capacity = capacity
        self.count = 0
        self.history = {}
        self.head = 0
        self.tail = 0
    # recode = (value, head)
    def get(self, key: int) -> int:
        if key in self.valdict:
            del self.history[self.valdict[key][1]]
            self.head += 1
            self.valdict[key] = (self.valdict[key][0], self.head)
            self.history[self.head] = key
            return self.valdict[key][0]
        return -1
    def put(self, key: int, value: int) -> None:
        if self.count == self.capacity:
            if key in self.valdict:
                del self.history[self.valdict[key][1]]
            else:
                while not self.tail in self.history:
                    self.tail += 1
                delkey = self.history[self.tail]
                del self.valdict[delkey]
                del self.history[self.tail]
        else:
            if key in self.valdict:
                del self.history[self.valdict[key][1]]
            else:
                self.count += 1
        self.head += 1
        self.valdict[key] = (value, self.head)
        self.history[self.head] = key
        return
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)