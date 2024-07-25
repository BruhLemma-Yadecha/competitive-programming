# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.removed = set()
        

    def popSmallest(self) -> int:
        current_smallest = self.smallest
        self.removed.add(self.smallest)
        next_smallest = self.smallest
        while next_smallest in self.removed:
            next_smallest += 1
        self.smallest = next_smallest
        return current_smallest

    def addBack(self, num: int) -> None:
        if num < self.smallest:
            self.smallest = num
        if num in self.removed:
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)