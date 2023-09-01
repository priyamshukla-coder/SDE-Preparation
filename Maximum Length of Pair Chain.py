class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs=sorted(pairs,key=lambda val:val[1])

        cnt=0

        mn=float("-inf")

        for i in pairs:

            curr_val=i[0]

            if curr_val>mn:

                cnt=cnt+1

                mn=i[1]

        return cnt