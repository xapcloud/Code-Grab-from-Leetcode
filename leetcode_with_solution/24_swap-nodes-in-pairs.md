###24 Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.


For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.


Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode swapPairs(ListNode head) {
      if(head == null || head.next ==null)
			return head;


		ListNode l = head;

		while (l != null && l.next != null) {
			int t1 = l.val;
			l.val = l.next.val;
			l.next.val = t1;
			l = l.next.next;
		}

		return head;
    }
}