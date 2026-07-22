class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.arr = set()
        for i in range(len(nums)):
            if nums[i] in self.arr:
                return True
            self.arr.add(nums[i])
        return False
        

        