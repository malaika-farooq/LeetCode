class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #need to do this again
        self.answer = [0] * len(temperatures)  
        self.stack = []
                               
        for i, temp in enumerate(temperatures):
        
            while self.stack and temperatures[self.stack[-1]] < temp:
                #print(temperatures[self.stack[-1]])
                prev = self.stack.pop()
                self.answer[prev] = i - prev    
            self.stack.append(i)

        return self.answer

        
        #commenting because solutionis correct but not efficint so I will come up with something efficient
        # self.stack = []
        # for i in range(len(temperatures)):
        #     count = 0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             count = j - i
        #             break
        #         else:
        #             continue
        #     self.stack.append(count)
        # return self.stack