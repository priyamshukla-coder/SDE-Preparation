class Solution:
    def sumCounts(self, nums: List[int]) -> int:

        res=0

        # cnt=0

        for i in range(len(nums)):

            d1=defaultdict(int)

            cnt=0

            for j in range(i,len(nums)):

                d1[nums[j]]=d1[nums[j]]+1

                if d1[nums[j]]==1:

                    cnt=cnt+1

                res=res+cnt*cnt

        return res


        