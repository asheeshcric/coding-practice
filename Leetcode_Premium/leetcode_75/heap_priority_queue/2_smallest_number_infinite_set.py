"""
You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
"""
from heapq import heapify, heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.inf_list = list(range(1, 1001))
        heapify(self.inf_list)
        self.removed = set()

    def popSmallest(self) -> int:
        num = heappop(self.inf_list)
        self.removed.add(num)
        return num

    def addBack(self, num: int) -> None:
        if num in self.removed:
            heappush(self.inf_list, num)
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
