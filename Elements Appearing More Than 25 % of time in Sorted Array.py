class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        l=len(arr)

        req_limit=(l*25)//100

        # print(req_limit)

        cnt=Counter(arr)

        for i in cnt:

           if cnt[i]>req_limit:

               return i