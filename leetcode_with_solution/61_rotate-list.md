###61 Rotate List
Given a list, rotate the list to the right by k places, where k is non-negative.
For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.Given a list, rotate the list to the right by k places, where k is non-negative.For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null)
            return head;
        if(head.next == null)
            return head;
        
        ListNode l = head;
        int count = 0;
        while(l!=null){
            count++;
            l = l.next;
        }
        
        if(k >= count)
            k = k%count;
            
        if(k == 0)
            return head;
        
        
        System.out.println("count="+count+"\tk= "+k);
        ListNode l1 = head;
        ListNode l2 = head;
        for(int i = 0 ; i < count - k ; i ++){
            l1 = l1.next;
        }
        
        for(int i = 0; i < count - k - 1; i ++){
            l2 = l2.next;
        }
        l2.next = null;
        
        
        
        ListNode l3 = l1;
            
        while(l3.next != null){
            l3 = l3.next;
        }
        
        l3.next = head;
        
        
        return l1;
        
    }
}