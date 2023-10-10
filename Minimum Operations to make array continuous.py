class Solution:
    def minOperations(self, nums: List[int]) -> int:

        res=len(nums)

        # nums.sort()

        set_nums=sorted(set(nums))

        for i in range(len(set_nums)):

            r=set_nums[i]+len(nums)-1

            idx=bisect_right(set_nums,r)

            res=min(res,(len(nums)-idx+i))

        return res

