class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        res = 1

        mod = int(1e9+7)

        for i in range(1, len(complexity)):

            if complexity[i] <= complexity[0]:

                return 0

            res = (res * i) % mod

        return res
