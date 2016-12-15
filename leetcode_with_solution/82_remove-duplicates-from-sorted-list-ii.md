###82 Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.


For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        
        ListNode h = head;
        
        if(h == null || h.next == null)
            return h;
        
        
        boolean f = false;
        int repeat = 0;
        while(h != null && h.next != null){
            if(h.val == h.next.val){
                f = true;
                repeat = h.val;
                h.next = h.next.next;
                
                //System.out.println(head.val+"\t"+head.next.next);
            }else{
                if(f && h.val == repeat){
                    ListNode temp = h.next;
                    h.val = temp.val;
                    h.next = temp.next;
                }else{
                    h = h.next;
                }
                
                f = false;
            }
            
        }
        if(f && h.val == repeat){
            // System.out.println(h.val+"\t"+h.next);
            // h = h.next;
            // //è¿ä¸æ­¥æ²¡ææ¹åheadçå¼ï¼ä¸æä¸ºä»ä¹  ã
            //æäº ï¼è¿ä¸æ­¥åªæ¯ä¸ä¸ªèµå¼ ï¼å¹¶æ²¡ææ¹ååæ¥çé¾è¡¨ 
            // System.out.println(head.val+"\t"+head.next);
            if(head == h)
                return null;
            else{
                h = head;
                while(h.next!=null){
                    if(h.next.val == repeat){
                        h.next = h.next.next;
                    }else{
                        h = h.next;
                    }
                    
                }
            }
            
        }
        
        
        return head;
    }
}