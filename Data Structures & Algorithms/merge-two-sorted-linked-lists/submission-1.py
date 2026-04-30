# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        dummy = ListNode()         # make the sorted list add a dummy for edge cases 
        tail = dummy 
         
        while list1 and list2:       # compare both calues in lists ad thenincrement based off that 
            if list1.val < list2.val: 
                tail.next = list1 
                list1 = list1.next 
            else: 
                tail.next = list2 
                list2 = list2.next 
            tail = tail.next 
                                    # check if theres still vals left in either or list 
                                    #if there is than simply insert the rest of it since th elist is alreafy sorted 
        if list1: 
            tail.next = list1 
        elif list2: 
            tail.next = list2 

        return dummy.next 