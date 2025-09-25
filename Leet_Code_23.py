# https://leetcode.com/problems/merge-k-sorted-lists/submissions/1782407495/
# 23. Merge k Sorted Lists
# Hard
# Topics
# premium lock icon
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.


# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6

# Example 2:
# Input: lists = []
# Output: []

# Example 3:
# Input: lists = [[]]
# Output: []




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if (lists == None) or len(lists) ==0 :
            return None
        
        l1 = ListNode('dummy')
        temp = l1

        for each_list in lists:
            temp_each = each_list
            while temp_each:
                
                t = ListNode(temp_each.val)
                temp.next = t
                temp = temp.next
                temp_each = temp_each.next
        

        final = ListNode('dummy')
        temp = l1.next

        while temp:
            ft = final
            t1 = ListNode(temp.val)
            if ft == None:
                ft = t1
            else:
                while ft != None:
                    if(ft.next and ft.next.val> t1.val):
                        t1.next = ft.next
                        ft.next = t1
                        break;
                    elif(ft.next == None):
                        t1.next = ft.next
                        ft.next = t1
                        break;
                    ft = ft.next
            temp = temp.next

        print(final.next)
        return final.next
        
