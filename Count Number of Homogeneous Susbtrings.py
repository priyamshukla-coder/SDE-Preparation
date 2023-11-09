class Solution:
    def countHomogenous(self, s: str) -> int:

        curr=1

        res=0

        mod=int(1e9+7)
        
        for i in range(len(s)-1):

            if s[i]==s[i+1]:

                curr=curr+1

            else:

                curr=1

            res=res+curr

            res=res%mod

        return res+1