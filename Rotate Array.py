class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        arr = nums[:]

        for i in range(len(nums)):

            nums[i] = arr[(len(nums) -k + i) % len(nums)]
