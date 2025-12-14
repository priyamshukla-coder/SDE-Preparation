class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:

        nums.sort()

        sum_largest , sum_smallest = 0 , 0

        l = len(nums)

        i = 0

        while k > 0:

            sum_largest += nums[i]

            sum_smallest += nums[l - i - 1]

            k -= 1

            i += 1

        return abs(sum_largest - sum_smallest)©leetcode
