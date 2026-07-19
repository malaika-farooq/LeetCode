class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        self.result = 0
        if len(tokens) ==1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*', '/']:
                self.stack.append(tokens[i])
            else:
                self.pop1 = int(self.stack.pop())
                self.pop2 = int(self.stack.pop())
                if tokens[i] == '+':
                    self.result = self.pop1 + self.pop2
                    self.stack.append(self.result)

                if tokens[i] == '-':
                    self.result = self.pop2 - self.pop1
                    self.stack.append(self.result)

                if tokens[i] == '*':
                    self.result = self.pop2 * self.pop1
                    self.stack.append(self.result)
                
                if tokens[i] == '/':
                    self.result = int(self.pop2 / self.pop1)
                    self.stack.append(self.result)

        return self.result

        