class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        d1=Counter(chars)

        res=0

        for i in words:

            curr=Counter(i)

            status=True

            for j in curr:

                if curr[j]>d1[j]:

                    status=False

                    break

            if status:

                # print(i)

                res=res+len(i)

        return res
        