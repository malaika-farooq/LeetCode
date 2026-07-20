from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #formula remember, depends on time
        # time=(target−position)​/speed
        self.sortpos = defaultdict(int)
        self.value  = []
        self.result = 1


        for i in range(len(position)):
            self.value.append((target - position[i]) / speed[i])

        for i in range(len(position)):
            self.sortpos[position[i]] = self.value[i]

        sorted_dict = dict(sorted(self.sortpos.items(), key=lambda x: x[0], reverse=True))

        self.times = [t for pos, t in sorted_dict.items()]
        self.max_time = self.times[0]
        for i in range(1, len(self.times)):
            if self.times[i] > self.max_time:
                self.result +=1
                self.max_time = self.times[i]


        return self.result