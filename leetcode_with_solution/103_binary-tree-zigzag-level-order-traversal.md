###103 Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7


    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]


[
  [3],
  [20,9],
  [15,7]
]
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        if(root == null)
            return result;
        
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        List<TreeNode> l = new ArrayList<TreeNode>();
        HashMap<TreeNode,Integer> hm = new HashMap<TreeNode,Integer>();
        
        
        
        q.offer(root);
        hm.put(root,0);
        
        int curDepth = 0;
        
        List<Integer> re = new ArrayList<Integer>();
        
        while(!q.isEmpty()){
            TreeNode t = q.poll();
            l.add(t);
            
            if(hm.get(t) == curDepth){
                re.add(t.val);
            }else{
                result.add(re);
                System.out.println(re);
                re = new ArrayList<Integer>();
                
                curDepth = hm.get(t);
                re.add(t.val);
            }
            
            if(t.left!=null){
                q.offer(t.left);
                hm.put(t.left, hm.get(t)+1);
            }
            if(t.right!=null){
                q.offer(t.right);
                hm.put(t.right, hm.get(t)+1);
            }
        }
        result.add(re);
        
        
        List<List<Integer>> resulttttt = new ArrayList<List<Integer>>();
        
        for(int i = 0; i < result.size(); i ++){
            List<Integer> temp = result.get(i);
            
            if(i%2==1)
                Collections.reverse(temp);  
            
            
            resulttttt.add(temp);
        }
        
        return result;
    }
}