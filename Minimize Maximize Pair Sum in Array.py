class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        mx=0

        nums.sort()

        for i in range(len(nums)//2):

            mx=max(mx,nums[i]+nums[len(nums)-i-1])

        return mx