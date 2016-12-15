###101 Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3



But the following [1,2,2,null,3,null,3]  is not:

    1
   / \
  2   2
   \   \
   3    3



Note:
Bonus points if you could solve it both recursively and iteratively.
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3]  is not:

    1
   / \
  2   2
   \   \
   3    3


    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public boolean isSymmetric(TreeNode root) {
        
        if(root == null)
            return true;
            
        TreeNode tl = root.left;
        TreeNode tr = root.right;
        
        if(tl == null && tr == null)
            return true;
        if(tl == null || tr == null)
            return false;
            
        Stack<TreeNode> s1 = new Stack<TreeNode>();
        Stack<TreeNode> s2 = new Stack<TreeNode>();
        
        s1.push(tl);
        s2.push(tr);
        
        while(!s1.isEmpty() && !s2.isEmpty()){
            TreeNode t1 = s1.pop();
            TreeNode t2 = s2.pop();
            if(t1.val != t2.val)
                return false;
            
            if(t1.right != null){
                s1.push(t1.right);
                if(t2.left==null)
                    return false;
                else
                    s2.push(t2.left);
            }
            else{
                if(t2.left!=null)
                    return false;
            }
            if(t1.left != null){
                s1.push(t1.left);
                if(t2.right == null)
                    return false;
                else
                    s2.push(t2.right);
            }
            else{
                 if(t2.right!=null)
                    return false;
            }
        }
        
        return true;
        
    }
}