###23 Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
   public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0)
			return null;

		if (lists.length == 1) {
			return lists[0];
		}
		if (lists.length == 2) {
			return mergeTwoLists(lists[0], lists[1]);
		}

		int len = lists.length;
		int l1 = len / 2;

		ListNode[] list1 = Arrays.copyOfRange(lists, 0, l1);
		ListNode[] list2 = Arrays.copyOfRange(lists, l1, len);

		return mergeTwoLists(mergeKLists(list1), mergeKLists(list2));
	}

	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

		ListNode result = new ListNode(0);
		ListNode r = result;

		while (l1 != null && l2 != null) {
			int v1 = l1.val;
			int v2 = l2.val;

			if (v1 < v2) {
				r.next = l1;
				l1 = l1.next;
			} else {
				r.next = l2;
				l2 = l2.next;
			}
			r = r.next;
		}
		if (l1 != null)
			r.next = l1;
		if (l2 != null)
			r.next = l2;

		return result.next;

	}
}