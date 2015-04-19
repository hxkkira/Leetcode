# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        flag=0;
        result=l1;
        while True:
            l1.val=l1.val+l2.val+flag;
            flag=l1.val/10;
            l1.val=l1.val%10;
            prel1=l1;
            prel2=l2;
            l1=l1.next;
            l2=l2.next;
            if l1==None:
                if l2==None:
                    if flag==0:
                        return result;
                    else:
                        l1=ListNode(flag);
                        flag=0;
                        prel1.next=l1;
                        return result;
                else:
                    l1=ListNode(flag);
                    flag=0;
                    prel1.next=l1;
                    
            if l2==None:
                l2=ListNode(flag);
                flag=0;
                prel2.next=l2;