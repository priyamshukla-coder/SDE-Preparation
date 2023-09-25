class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

      s1=Counter(s)

      t1=Counter(t)

      for i in t:

        if i not in s1 or t1[i]!=s1[i]:

          return i