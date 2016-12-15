###98 Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).


Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Binary tree [2,1,3], return true.

Example 2:

    1
   / \
  2   3

Binary tree [1,2,3], return false.

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Binary tree [2,1,3], return true.

    2
   / \
  1   3
Example 2:

    1
   / \
  2   3

Binary tree [1,2,3], return false.

    1
   / \
  2   3
Subscribe to see which companies asked this question
###Solution
```java

 import java.util.*;
 
public class Solution {
    public boolean isValidBST(TreeNode root) {
        
        if(root == null)
            return true;
        
	    ArrayList<Integer>s = new ArrayList<>();
	    
	    dfs(root,s);
	    
	    if(s.size() < 2)
	        return true;
	    
	    for(int i = 0; i < s.size() - 1; i ++){
	        if(s.get(i)>=s.get(i+1))
	            return false;
	    }
        
        return true;
    }
    
    private static void dfs(TreeNode root, ArrayList<Integer> s){
        if(root.left!=null)
            dfs(root.left, s);
        s.add(root.val);
        if(root.right!=null)
            dfs(root.right,s);
    }
}