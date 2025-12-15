class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        i = 0

        start = 0

        cnt = 0
        
        while i < len(prices):

            if i > 0 :

                if prices[i-1] - prices[i] != 1:

                    start = i

            cnt = cnt + (- start + i) + 1

            i += 1

        return cnt

                
