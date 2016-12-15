###206 Reverse Linked List
Reverse a singly linked list.
click to show more hints.
Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
Reverse a singly linked list.click to show more hints.A linked list can be reversed either iteratively or recursively. Could you implement both?Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode reverseList(ListNode head) {
        
        if(head == null || head.next == null)
            return head;
        
        ListNode p = head.next;  
        ListNode n = reverseList(p);  
          
        head.next = null;  
        p.next = head;  
        return n;

        
    }
}