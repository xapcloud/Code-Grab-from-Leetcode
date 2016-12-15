###111 Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.Given a binary tree, find its minimum depth.The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public int minDepth(TreeNode root) {
        if(root == null)
            return 0;
        HashMap<TreeNode,Integer> hm = new HashMap<TreeNode,Integer>();
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        hm.put(root,1);
        q.offer(root);
        
        while(!q.isEmpty()){
            TreeNode t = q.poll();
            int a = hm.get(t);
            
            if(t.left == null && t.right == null)
                return a;
            if(t.left != null){
                q.offer(t.left);
                hm.put(t.left,a+1);
            }
            if(t.right != null){
                q.offer(t.right);
                hm.put(t.right,a+1);
            }
            
        }
        
        return -1;
    }
}