###226 Invert Binary Tree
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9

to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.     4
   /   \
  2     7
 / \   / \
1   3 6   9     4
   /   \
  7     2
 / \   / \
9   6 3   1Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if(root == null)
            return root;
        
        TreeNode l = root.left;
        TreeNode r = root.right;
        
        root.left = invertTree(r);
        root.right = invertTree(l);
        
        return root;
    }
}