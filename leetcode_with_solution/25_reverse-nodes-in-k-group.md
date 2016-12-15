###25 Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.


If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5


For k = 2, you should return: 2->1->4->3->5


For k = 3, you should return: 3->2->1->4->5

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.You may not alter the values in the nodes, only nodes itself may be changed.Only constant memory is allowed.
For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
   public ListNode reverseKGroup(ListNode head, int k) {

		if (countNode(head) < k)
			return head;

		int[] n = new int[k];

		ListNode l = head;
		ListNode l1 = head;

		while (countNode(l) >= k) {
			for (int i = 0; i < k; i++) {
				n[i] = l.val;
				l = l.next;
			}
		    for (int i = k - 1; i >= 0; i--) {
				l1.val = n[i];
				l1 = l1.next;
			}
		}

		return head;
	}

	private int countNode(ListNode head) {

		int count = 0;
		while (head != null) {
			count++;
			head = head.next;
		}

		return count;
	}
}