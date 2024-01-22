class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        res=[i for i in range(1,len(nums)+1)]

        ans=[]

        for i in res:

            if nums.count(i)>1:

                ans.append(i)

                break

        for i in res:

            if i not in nums:

                ans.append(i)

        return ans
        