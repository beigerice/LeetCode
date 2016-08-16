from random import randint
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            self.dic[val] = []
            flag = 1
        else:
            flag = 0
        self.dic[val].append(len(self.arr))
        self.arr.append(val)
        if flag: return True
        return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        if self.dic[val][-1] == len(self.arr)-1:
            self.dic[val].pop()
            if len(self.dic[val]) == 0:
                del self.dic[val]
            self.arr.pop()
        else:
            idx = self.dic[val][-1]
            self.dic[val].pop()
            if len(self.dic[val]) == 0:
                del self.dic[val]            
            self.dic[self.arr[-1]][-1] = idx
            self.arr[idx] = self.arr[-1]
            self.arr.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.arr[randint(0,len(self.arr)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
