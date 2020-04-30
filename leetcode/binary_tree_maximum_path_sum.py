# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_path = None
    def search_down(self, node):
        left_search, right_search = -float('inf'), -float('inf')
        if node.left:
            left_search = self.search_down(node.left)
        if node.right:
            right_search = self.search_down(node.right)
        max_path = max(left_search, right_search)
        self.max_path = max(self.max_path, max_path, node.val + left_search + right_search)
        return max(node.val, node.val + left_search, node.val + right_search)
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = root.val
        root_path = self.search_down(root)
        return max(self.max_path, root_path)