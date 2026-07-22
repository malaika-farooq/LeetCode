class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.arr = {}
        self.need = 0
        for i , num in enumerate(nums):
            self.need = target - num
            if self.need in self.arr:
                return [self.arr[self.need], i]
            self.arr[num] = i
        


        