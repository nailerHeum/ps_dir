# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search_node(self, head, value, depth):
        if not head.left and not head.right:
            return (False, False)
        depth += 1
        if not head.left:
            if head.right.val == value:
                return (depth, head.val)
            return self.search_node(head.right, value, depth)
        if not head.right:
            if head.left.val == value:
                return (depth, head.val)
            return self.search_node(head.left, value, depth)
        if head.left.val == value or head.right.val == value:
            return (depth, head.val)
        d, p = self.search_node(head.left, value, depth)
        if not d:
            return self.search_node(head.right, value, depth)
        return (d, p)
        
            
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        x_depth, x_parent = self.search_node(root, x, 0)
        y_depth, y_parent = self.search_node(root, y, 0)
        if x_depth == y_depth and x_parent != y_parent:
            return True
        return False
