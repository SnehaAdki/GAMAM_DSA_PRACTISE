# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = l1
        t2 = l2
        final = ListNode()

        rem = 0

        while t1 != None and t2!= None:
            print(t1)
            print(t2)
            val_added = t1.val + t2.val + rem
            val = val_added % 10
            print(val)
            rem =  int(val_added / 10)
            print(rem)
            new_node = ListNode(val)
            if final.next == None:
                final.next = new_node
            else:
                temp = final.next
                while temp.next != None:
                    temp = temp.next
                temp.next = new_node

            t1 = t1.next
            t2 = t2.next

        if t1 != None:
            temp = t1 
            fl = final

            while temp != None:
                val_added = temp.val + rem
                val = val_added % 10
                rem =  int(val_added / 10)
                new_node = ListNode(val)
                if final.next == None:
                    final.next = new_node
                else:
                    temp_final = final.next
                    while temp_final.next != None:
                        temp_final = temp_final.next
                    temp_final.next = new_node
                temp = temp.next
        elif t2 != None:
            temp = t2
            fl = final
            while temp != None:
                val_added = temp.val + rem
                val = val_added % 10
                rem =  int(val_added / 10)
                new_node = ListNode(val)
                if final.next == None:
                    final.next = new_node
                else:
                    temp_final = final.next
                    while temp_final.next != None:
                        temp_final = temp_final.next
                    temp_final.next = new_node
                temp = temp.next

        if rem != 0:
            temp_final = final.next
            while temp_final.next != None:
                temp_final = temp_final.next
            rem_node = ListNode(rem)
            temp_final.next = rem_node
        
        return final.next   
