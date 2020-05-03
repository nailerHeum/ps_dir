# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = None
        
    def go_deep(self, node, idx):
        if idx == len(self.arr) - 1:
            print(idx, node)
            if node.val == self.arr[idx] and not node.left and not node.right:
                return True
            return False
        if node.left and node.left.val == self.arr[idx + 1]:
            if self.go_deep(node.left, idx + 1):
                return True
        if node.right and node.right.val == self.arr[idx + 1]:
            if self.go_deep(node.right, idx + 1):
                return True
        return False
        
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        self.arr = arr
        if root.val != arr[0]:
            return False
        return self.go_deep(root, 0)
        