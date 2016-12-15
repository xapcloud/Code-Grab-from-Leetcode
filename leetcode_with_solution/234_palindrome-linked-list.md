###234 Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.
Follow up:
Could you do it in O(n) time and O(1) space?Given a singly linked list, determine if it is a palindrome.Follow up:
Could you do it in O(n) time and O(1) space?Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public boolean isPalindrome(ListNode head) {
        if(head==null||head.next ==null)
            return true;
        
        
        ListNode temp = head;
        ListNode h = new ListNode(-1);
        ListNode te = h;
        while(temp!=null){
            te.next = new ListNode(temp.val);
            te = te.next;
            temp = temp.next;
        }
        h = h.next;
  
        ListNode reverse = null;
        
        while(h != null){
            ListNode t = h.next;
            h.next = reverse;
            reverse = h;
            h = t;
        }
        
        while(head != null){
            if(head.val == reverse.val){
                head = head.next;
                reverse = reverse.next;
            }else
                return false;
            
        }
        
        return true;
        
    }
}