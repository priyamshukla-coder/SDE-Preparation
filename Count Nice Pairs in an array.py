class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def reverse(num):

            rev=0

            while num>0:

                rev=rev*10+num%10

                num=num//10

            return rev

        rev_arr=[]

        for i in range(len(nums)):

            rev_arr.append(nums[i]-reverse(nums[i]))

        result=0

        count_map=defaultdict(int)

        mod=int(1e9+7)

        for i in rev_arr:

            result=result+(count_map[i])

            result=result%mod

            count_map[i]+=1

        return result