###144 Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3



return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


   1
    \
     2
    /
   3

return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        
        Stack<TreeNode> s = new Stack<TreeNode>();
        List<Integer> l = new ArrayList<Integer>();
        
        if(root == null)
            return l;
        
        s.push(root);
        
        while(!s.isEmpty()){
            TreeNode t = s.pop();
            l.add(t.val);
            if(t.right!=null)
                s.push(t.right);
            if(t.left!=null)
                s.push(t.left);
        }
        return l;
    }
}