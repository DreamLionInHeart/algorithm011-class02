"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack,ans=[root],[]
        while stack:
            cur=stack.pop(-1)
            ans.append(cur.val)
            stack.extend(cur.children[::-1])
            # print(stack.extend(cur.children[::-1]))
        return ans