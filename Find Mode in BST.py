# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        def traverse(root,l1):

            if root is None:

                return 

            traverse(root.left,l1)

            l1.append(root.val)

            traverse(root.right,l1)

            return l1

        l1=[]

        res=traverse(root,l1)

        cnt=Counter(res)

        # print(cnt)

        mx_cnt=max(cnt.values())

        result=[]

        for i in cnt:

            if cnt[i]==mx_cnt:

                result.append(i)

        return result

        

