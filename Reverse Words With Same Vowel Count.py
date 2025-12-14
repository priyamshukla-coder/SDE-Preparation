class Solution:
    def reverseWords(self, s: str) -> str:

        def calculate(s):

            cnt  = 0

            for i in range(len(s)):

                if s[i] in ["a", "e" , "i" , "o" ,"u"]:

                    cnt += 1

            return cnt

        d1 = {}

        new = ""

        s = s.split(" ")

        for i in s:

            d1[i] = calculate(i)

        # print(d1)

        val = d1[s[0]]

        i = 1

        while i < len(s):

            if val == d1[s[i]]:

                s[i] = s[i][::-1]

            i += 1

        # print(s)

        return " ".join(s)

        # for i in range(len(s) - 1):

        #     if d1[s[0]] == d1[s[i+1]]:

        #         new += s[i]

        #         new += s[i+1][::-1]

        #     else:

        #         new += s[i]
        #         new += s[i+1]

        #         i += 2
        # print(new)

        # return new©leetcode
