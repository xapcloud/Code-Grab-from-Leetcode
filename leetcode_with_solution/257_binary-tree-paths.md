###257 Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.


For example, given the following binary tree:



   1
 /   \
2     3
 \
  5



All root-to-leaf paths are:
["1->2->5", "1->3"]

Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:


   1
 /   \
2     3
 \
  5


   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:
["1->2->5", "1->3"]
["1->2->5", "1->3"]Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> ret = new ArrayList<String>();
        if(root == null)
            return ret;
            
        allPath(root,"",ret);
        
        return ret;
    }
    
    private void allPath(TreeNode root,String s,  List<String> ret){
        if(s.length()==0)
            s = root.val+"";
        else
            s = s + "->" + root.val;
            
        if(root.left == null && root.right == null){
            ret.add(s);
        }

        if(root.left != null)
            allPath(root.left,s, ret);
        if(root.right != null)
            allPath(root.right, s, ret);
    }
}