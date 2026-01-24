class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        dictName =  defaultdict(list)
        invalid = set()

        for i, trans in enumerate(transactions):
            name, time, amount, city = trans.split(",")
            amount = int(amount)
            time = int(time)

            if amount > 1000:
                invalid.add(i)

            dictName[name].append((time, city, i))
        
        for name in dictName:
            tran = dictName[name]
            for i in range(len(dictName[name])):
                for j in range(i+1, len(dictName[name])):
                    time1, city1, trans1 = tran[i]
                    time2, city2, trans2 = tran[j]

                    if abs(time2 - time1) <= 60 and city1 != city2:
                        invalid.add(trans1)
                        invalid.add(trans2)

        return [transactions[i] for i in invalid]


        