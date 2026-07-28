from collections import Counter
class Solution:
    #use the counter function and sort it with function, 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        self.result = []
        self.dic = list(Counter(nums).items())
        self.dic.sort(key=lambda pair: pair[1], reverse=True)
        print(self.dic)

        for i in range(k):
            self.result.append(self.dic[i][0])

        return self.result
            



        