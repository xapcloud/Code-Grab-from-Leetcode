###112 Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.


For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1


return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        
        if(root == null)
            return false;
        
        List<Integer> l = new ArrayList<Integer>();
        
        pathSum(root, l , root.val);
        
        return l.contains(sum);
        
        
    }
    
    private void pathSum(TreeNode t, List<Integer> l, int v){
        
        if(t.left == null && t.right == null)
            l.add(v);
        if(t.left != null)
            pathSum(t.left, l, v+t.left.val);
        if(t.right != null)
            pathSum(t.right, l, v+t.right.val);
        
        
    }
}