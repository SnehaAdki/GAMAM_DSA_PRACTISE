# https://leetcode.com/problems/reverse-linked-list/submissions/1752506173/
# Leet Code 206 
# 206. Reverse Linked List
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given the head of a singly linked list, reverse the list, and return the reversed list.

 

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        t1 = head
        while t1 != None:
            temp = t1.next
            if t1 == head:
                t1.next=None
            else:
                t1.next = head
                head = t1
            t1=temp
        return head

