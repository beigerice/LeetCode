class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.i = iterator
        self.n = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.n:
            self.n = self.i.next()
        return self.n

    def next(self):
        """
        :rtype: int
        """
        if not self.n:
            self.n = self.i.next()
        tmp = self.n
        self.n = None
        return tmp

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.n:
            return True
        return self.i.hasNext()
