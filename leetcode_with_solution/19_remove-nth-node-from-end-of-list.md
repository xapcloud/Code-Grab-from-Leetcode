###19 Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.


Note:
Given n will always be valid.
Try to do this in one pass.
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
if (head == null)
			return null;

		int count = 1;
		ListNode l = head;

		while (l.next != null) {
			count++;
			l = l.next;
		}
		int[] a = new int[count];

		for (int i = 0; i < count; i++) {
			a[i] = head.val;
			head = head.next;
		}

		ListNode result = null;
		for (int i = count - 1; i >= 0; i--) {
			if (i == count - n)
				continue;
			else {
				ListNode temp = new ListNode(a[i]);
				temp.next= result;
				result = temp;
			}

		}

		return result;
    }
}