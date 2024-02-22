class OrderedStream(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.data = [None for x in range(n)]
        self.p = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.data[idKey - 1] = value
        result = []
        while self.p < len(self.data) and self.data[self.p] != None:
            result.append(self.data[self.p])
            self.p += 1
        return result
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)