# Leet Code 101
# https://leetcode.com/problems/symmetric-tree/submissions/1760548278/

# 101. Symmetric Tree
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true


# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.rec_tree(root.left,root.right)

    def rec_tree(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.rec_tree(left.left,right.right) and self.rec_tree(left.right,right.left)

        
            
