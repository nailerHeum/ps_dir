# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.recur(node.left)
        self.recur(node.right)
        return
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.recur(root)
        return root

# trivia
# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
