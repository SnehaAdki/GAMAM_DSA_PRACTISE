# Leet code 21
# DP
# https://leetcode.com/problems/merge-two-sorted-lists/

# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        t1 = list1
        t2 = list2
        temp = final_node = ListNode()

        while t1:
            if (t2 is None) or t1.val <= t2.val:
                new_node = ListNode(t1.val)
                temp.next = new_node
                temp = new_node
                t1 = t1.next
            elif t1.val > t2.val:
                new_node = ListNode(t2.val)
                temp.next = new_node
                temp = new_node
                t2 = t2.next

        while t2:
            new_node = ListNode(t2.val)
            temp.next = new_node
            temp = new_node
            t2 = t2.next

        return final_node.next
        
