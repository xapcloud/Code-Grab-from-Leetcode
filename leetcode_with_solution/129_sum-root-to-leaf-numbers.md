###129 Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
For example,

    1
   / \
  2   3



The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.


Return the sum = 12 + 13 = 25.
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.An example is the root-to-leaf path 1->2->3 which represents the number 123.Find the total sum of all root-to-leaf numbers.For example,

    1
   / \
  2   3


    1
   / \
  2   3

The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public int sumNumbers(TreeNode root) {
        if(root == null)
            return 0;
        return sumTree(root,0);
    }
    
    
    private int sumTree(TreeNode r, int preValue){
        if(r.left == null && r.right == null){
            return preValue*10+r.val;
        }else if(r.left == null){
           return sumTree(r.right, preValue*10+r.val);
        }else if(r.right == null){
            return sumTree(r.left, preValue*10+r.val);
        }else{
            return sumTree(r.right, preValue*10+r.val)+sumTree(r.left, preValue*10+r.val);
        }
    }
}