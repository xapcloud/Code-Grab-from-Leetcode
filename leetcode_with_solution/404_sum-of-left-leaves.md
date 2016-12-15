###404 Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

Find the sum of all left leaves in a given binary tree.Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        if(root == null)
            return 0;
        List<Integer> leftLeaves = new ArrayList<Integer>();
        find(root,leftLeaves,0);
        
        int result = 0;
        for(int i:leftLeaves){
            result+=i;
        }
        
        return result;
    }
    
    private void find(TreeNode root, List<Integer> ll, int flag){
        if(root.left == null && root.right == null){
            if(flag == 1)
                ll.add(root.val);
        }else{
            if(root.left!=null)
                find(root.left,ll,1);
            if(root.right!=null)
                find(root.right,ll,2);
        }
    }
}