###21 Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    	ListNode result = new ListNode(0);
		ListNode r = result;

		while (l1 != null && l2 != null) {
			int v1 = l1.val;
			int v2 = l2.val;

			if (v1 < v2) {
				r.next = l1;
				l1 = l1.next;
			}else{
				r.next = l2;
				l2 = l2.next;
			}
			r = r.next;
		}
		if(l1!=null)
			r.next = l1;
		if(l2!=null)
			r.next = l2;
		
		

		return result.next;
    }

}