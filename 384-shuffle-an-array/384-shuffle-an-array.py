import copy
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.original = copy.deepcopy(nums)
        
    def reset(self) -> List[int]:
        return self.original
        
    def shuffle(self) -> List[int]:
        shuffled = copy.deepcopy(self.original)
        random.shuffle(shuffled)
        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()