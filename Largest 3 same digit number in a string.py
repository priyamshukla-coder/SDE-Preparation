class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        mx=float("-inf")

        for i in range(len(num)-2):

            if num[i]==num[i+1]==num[i+2]:

                mx=max(mx,int(num[i]+num[i+1]+num[i+2]))

        if mx==float("-inf"):

            return ""

        elif len(str(mx))<3:

            return "0"*(3-len(str(mx)))+str(mx)

        else:

            return str(mx)