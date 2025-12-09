class Solution:
    def specialTriplets(self, nums: List[int]) -> int:

        mp_right = Counter(nums)

        mp_left = defaultdict(int)

        res = 0

        mod = int(1e9+7)

        for i in nums:

            mp_right[i] -= 1

            val = i*2

            if val in mp_left and val in mp_right:

                res += (mp_left[val] * mp_right[val])

            res = res % mod

            mp_left[i] += 1

        return res
        
