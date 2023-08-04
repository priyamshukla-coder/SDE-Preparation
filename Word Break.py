class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict=set(wordDict)

        q1=deque([0])

        visited=set()

        while len(q1)>0:

            start_index=q1.popleft()

            if start_index==len(s):

                return True

            for index in range(start_index+1,len(s)+1):

                if index in visited:

                    continue

                if s[start_index:index] in wordDict:

                    q1.append(index)

                    visited.add(index)

        return False   