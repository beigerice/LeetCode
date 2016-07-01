class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.lru = []
        self.cnt = 0
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            self.lru.remove(key)
            self.lru.append(key)
            return self.dic[key]
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.cnt < self.capacity:
            if key in self.dic:
                self.lru.remove(key)
            else:
                self.cnt += 1
            self.lru.append(key)
            self.dic[key] = value
        else:
            if key not in self.dic:
                del self.dic[self.lru[0]]
                self.lru = self.lru[1:]
            else:
                self.lru.remove(key)
            self.lru.append(key)
            self.dic[key] = value
            
a = LRUCache(1)
a.set(2,1)
print a.get(2)
a.set(3,2)
print a.get(2)
print a.get(3)


