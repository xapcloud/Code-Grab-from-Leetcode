###83 Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.


For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        
        ListNode l = head;
        
        while(l != null && l.next != null){
            if(l.val == l.next.val){
                l.next = l.next.next;
            }else{
                l = l.next;
            }
        }
        return head;
    }
}