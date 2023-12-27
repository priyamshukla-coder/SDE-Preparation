class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        if len(set(colors))==len(colors):

            return 0

        prev,curr=0,0

        for i in range(1,len(colors)):

            if colors[i]==colors[prev]:

                if neededTime[i]<neededTime[prev]:

                    curr=curr+neededTime[i]

                else:

                    curr=curr+neededTime[prev]

                    prev=i

            else:

                prev=i

        return curr
