###110 Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.


For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public boolean isBalanced(TreeNode root) {
        
        return isBal(root,0)!=-1;
    }
    
    
    private int isBal(TreeNode root, int depth){
        if(root == null)
            return depth;
        int left = isBal(root.left, depth+1);
        if(left == -1)
            return left;
            
        int right = isBal(root.right, depth+1);
        if(right == -1)
            return right;
            
        if(Math.abs(left-right)>1)
            return -1;
        else
            return Math.max(left,right);
        
    }
}