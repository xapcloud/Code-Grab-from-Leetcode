###102 Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7



return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
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

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]


[
  [3],
  [9,20],
  [15,7]
]
Subscribe to see which companies asked this question
###Solution
```java

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
       List<List<Integer>>result = new ArrayList<List<Integer>>();

       if(root == null)
            return result;

		Queue<TreeNode> q = new LinkedList<TreeNode>();
		HashMap<TreeNode, Integer> h = new HashMap<TreeNode, Integer>();
		q.offer(root);
		h.put(root, 1);
		int[][] i = new int[2][10000];
		i[0][0] = root.val;
		i[1][0] = 1;
		int count = 1;
		int lastDepth = 1;
		while (!q.isEmpty()) {
			TreeNode t = q.poll();
			if (t.left != null) {
				q.offer(t.left);
				h.put(t.left, h.get(t) + 1);
				i[0][count] = t.left.val;
				i[1][count++] = h.get(t) + 1;
			}
			if (t.right != null) {
				q.offer(t.right);
				h.put(t.right, h.get(t) + 1);
				i[0][count] = t.right.val;
				i[1][count++] = h.get(t) + 1;
			}
			lastDepth = h.get(t);
		}

		List<List<Integer>> s = new ArrayList<List<Integer>>();

		int point = 0;
		for (int m = 1; m <= lastDepth; m++) {
			List<Integer> l = new ArrayList<Integer>();
			for (int n = point; n < count; n++) {
				if (i[1][n] == m)
					l.add(i[0][n]);
				else {
					point = n;
					break;
				}
			}
			s.add(l);
		}
		

		return s;
        
    }
}