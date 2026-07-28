class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # you could divide, you'd compute the total product of the array, then for each index just do total / nums[i]
        self.prefix = []
        self.suffix = []
        self.result = []
        self.total = 0

        for i in range(len(nums)):
            if i == 0:
                total = 1
            else:
                total = total * nums[i-1]
            self.prefix.append(total)
        
        for i in range(len(nums)-1, -1,-1):
            if i == len(nums) -1:
                total = 1
            else:
                total = total * nums[i+1]
            self.suffix.append(total)
        print(self.prefix)
        print(self.suffix)
        self.suffix.reverse()
        for i in range(len(nums)):
            self.result.append(self.prefix[i] * self.suffix[i])
        return self.result

     

           

        
        