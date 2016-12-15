###141 Linked List Cycle

Given a linked list, determine if it has a cycle in it.


Follow up:
Can you solve it without using extra space?

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null)
            return false;
        ListNode fast = head;
        ListNode low = head;
        
        
        while(fast!=null && low !=null){
              
            fast = fast.next;
            if(fast!=null)
                fast = fast.next;
            low = low.next;
            
            if(fast == low&& fast != null)
                return true;
                
          
        }
        
        return false;
    }
}