class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.temp = []
        self.idx = 0
        def flat(element):
            if isinstance(element,int):
                self.temp.append(element)
            elif isinstance(element,list):
                for e in element:
                    flat(e)
            elif element.isInteger():
                self.temp.append(element.getInteger())
            else:
                flat(element.getList())
        flat(nestedList)
        
    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.temp[self.idx-1]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx < len(self.temp):
            return True
        else:
            return False
