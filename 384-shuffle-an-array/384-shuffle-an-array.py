import copy
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.shuffled = []
        self.shuffled.extend(nums)
        
    def reset(self) -> List[int]:
        return self.original
        
    def shuffle(self) -> List[int]:
        random.shuffle(self.shuffled)
        return self.shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()