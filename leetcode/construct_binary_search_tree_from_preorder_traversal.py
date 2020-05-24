# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.preorder = None
        self.root = None
        
    def set_child(self, idx):
        if idx == len(self.preorder):
            return
        head = self.root
        while True:
            if self.preorder[idx] > head.val:
                if head.right is None:
                    head.right = TreeNode(self.preorder[idx])
                    return self.set_child(idx + 1)
                else:
                    head = head.right
            else:
                if head.left is None:
                    head.left = TreeNode(self.preorder[idx])
                    return self.set_child(idx + 1)
                else:
                    head = head.left
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.preorder = preorder
        root = TreeNode(preorder[0])
        self.root = root
        self.set_child(1)
        return self.root
            
        
