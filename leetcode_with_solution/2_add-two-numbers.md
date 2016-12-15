###2 Add Two Numbers
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        return add(l1,l2,false);
    }
	
	public  ListNode add(ListNode l1, ListNode l2, boolean carry) {

		if(l1!=null&&l2!=null){
			int temp = carry ? (l1.val + l2.val + 1) : (l1.val + l2.val); 
			if (temp >= 10)
				carry = true;
			else
				carry = false;
			ListNode l = new ListNode(temp%10);
			l.next = add(l1.next,l2.next,carry);
			return l;
			
		}
		if(l1==null && l2==null & carry == true)
			return new ListNode(1);
		else if (l1==null && l2==null)
			return null;
		else if(l1 == null&&carry ==false)
			return l2;
		else if (l1 == null){
			int temp = l2.val + 1;
			l2.val = temp%10;
			l2.next = temp>=10?add(l1,l2.next,true):l2.next;
			return l2;
		}
		else if (l2 == null&&carry == false)
			return l1;
		else if (l2 == null){
			int temp = l1.val+1;
			l1.val = temp%10;
			l1.next = temp>=10?add(l1.next,l2,true):l1.next;
			return l1;
		}	
		return null;
		
	}
	
}