###86 Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.


You should preserve the original relative order of the nodes in each of the two partitions.


For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode partition(ListNode head, int x) {
        
        if(head == null)
            return null;
        
        List<Integer> ll = new ArrayList<Integer>();
        List<Integer> lb = new ArrayList<Integer>();
        while(head!=null){
            if(head.val < x){
                ll.add(head.val);
            }else{
                lb.add(head.val);
            }
            
            head = head.next;
        }
        
        ListNode result = new ListNode(-1);
        
        ListNode re = result;
        
        for(int i = 0; i < ll.size(); i ++){
            re.next = new ListNode(ll.get(i));
            re = re.next;
        }
        for(int i = 0; i < lb.size(); i ++){
            re.next = new ListNode(lb.get(i));
            re = re.next;
        }
        
        return result.next;
        
    }
}