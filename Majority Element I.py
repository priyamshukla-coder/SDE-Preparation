class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)

        for i in cnt:

            if cnt[i] > len(nums) // 2:

                return i
