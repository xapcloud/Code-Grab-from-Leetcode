###160 Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
Write a program to find the node at which the intersection of two singly linked lists begins.
###Solution
```java

public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null)
            return null;
        
        ListNode l1 = headA;
        ListNode l2 = headB;
        int c1 = 1;
        int c2 = 1;
        
        while(l1.next != null){
            c1 ++;
            l1 = l1.next;
        }
        while(l2.next != null){
            c2 ++;
            l2 = l2.next;
        }
        
        if(l1 != l2)
            return null;
        
        l1 = headA;
        l2 = headB;
        
        if(c1 > c2){
            while((c1-c2)>0){
                l1 = l1.next;
                c1 --;
            }
        }else{
            while((c2-c1)>0){
                l2 = l2.next;
                c2--;
            }
        }
        
        while(l1 != null && l1 != l2){
            l1 = l1.next;
            l2 = l2.next;
            
        }
        
        return l1;
        
    }
}