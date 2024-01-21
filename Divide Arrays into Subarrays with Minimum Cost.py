class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        if len(nums)==3:
            
            return sum(nums)
        
        ans=nums[0]
        
        nums.remove(ans)
        
        first_min=min(nums)
        
        nums.remove(first_min)
        
        return ans+first_min+min(nums)
        