###203 Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Remove all elements from a linked list of integers that have value val.
Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6,  val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode pre = new ListNode(0);
        pre.next = head;
        ListNode t = pre;

        while(t.next != null){
            if(t.next.val == val){
                t.next = t.next.next;
            }else{
                t = t.next;
            }
        }
        
        return pre.next;
        
    }
}