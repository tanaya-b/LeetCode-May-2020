from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    pass

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = OrderedCounter(s)
        for k, v in count.items():
            if v==1:
                return(s.index(k))
        return -1
