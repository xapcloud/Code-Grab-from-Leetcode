###328 Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.


Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

Subscribe to see which companies asked this question


Show Tags

Linked List


Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.


Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.

Subscribe to see which companies asked this question


Show Tags

Linked List




Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.


Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public ListNode oddEvenList(ListNode head) {
        List<Integer> list = new ArrayList<Integer>();
        
        while(head!=null){
            list.add(head.val);
            head = head.next;
        }
        
        ListNode o = new ListNode(-1) ;
        ListNode p1 = o;
        ListNode e = new ListNode(-1) ;
        ListNode p2 = e;

        for(int i = 0; i< list.size(); i ++){
            //åååï¼å ä¸ºiæ¯ä»0å¼å§çï¼ææå¥æ°å¶æ°ç¸åäº
            if(i%2==0){
                p2.next = new ListNode(list.get(i));
                p2 = p2.next;
            }else{
                p1.next = new ListNode(list.get(i));
                p1 = p1.next;
            }
        }
        
        p2.next = o.next;
        
        return e.next;
        
    }
}