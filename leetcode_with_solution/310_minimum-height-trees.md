###310 Minimum Height Trees

    For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs).
    Given such a graph, write a function to find all the MHTs and return a list of their root labels.


Format
    The graph contains n nodes which are labeled from 0 to n - 1.
    You will be given the number n and a list of undirected edges (each edge is a pair of labels).

 
You can assume that no duplicate edges will appear in edges. Since all edges are
    undirected, [0, 1] is the same as [1, 0] and thus will not appear together in
    edges.


Example 1:


    Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]


        0
        |
        1
       / \
      2   3


    return  [1]


Example 2:


    Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]


     0  1  2
      \ | /
        3
        |
        4
        |
        5


    return  [3, 4]


How many MHTs can a graph have at most?


Note:


    (1) According to the definition
    of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by
    exactly one path. In other words, any connected graph without simple cycles is a tree.”


    (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a
    leaf.

Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.
    For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs).
    Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
    The graph contains n nodes which are labeled from 0 to n - 1.
    You will be given the number n and a list of undirected edges (each edge is a pair of labels).
 
You can assume that no duplicate edges will appear in edges. Since all edges are
    undirected, [0, 1] is the same as [1, 0] and thus will not appear together in
    edges.

Example 1:

    Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

    return  [1]

Example 2:

    Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

    return  [3, 4]

Note:

    (1) According to the definition
    of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by
    exactly one path. In other words, any connected graph without simple cycles is a tree.”

    (2) The height of a rooted tree is the number of edges on the longest downward path between the root and a
    leaf.
Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
// public class Solution {
//     public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        
//         int[][] lap = new int[n][n];
        
//         for(int i = 0 ;i < edges.length; i ++){
//             lap[edges[i][0]][edges[i][1]] = 1;
//             lap[edges[i][1]][edges[i][0]] = 1;
//         }
        
//         int [] in = new int[n];
        
//         HashSet<Integer> hs = new HashSet<Integer>();

//         for(int i = 0; i < n; i ++){
//             in[i] = sumArray(lap[i]);
//             hs.add(i);
//         }

        
        
//         int nodes = n;
        
//         while( nodes > 2){
//             ArrayList<Integer> temp = new ArrayList<Integer>();
//             for(int i = 0; i < n; i ++){
//                 if(in[i]==1){
//                     in[i] = 0;
//                     nodes--;
//                     temp.add(i);
//                     hs.remove(i);
//                 }
//             }
         
//             remove(temp,in,lap);
//         }
       
//         List<Integer> ret = new ArrayList<Integer>();
//         for(int x: hs){
//             ret.add(x);
// 		}
       
//         return ret;
//     }
    
//     private static void remove(ArrayList<Integer> t, int[] in, int[][]lap){
//         for(int k = 0; k < t.size(); k ++ ){
//             int i = t.get(k);
//             for(int j = 0; j < in.length; j ++){
//                 if(lap[i][j]==1){
//                     in[j]--;
//                     lap[i][j] = lap[j][i] = 0;
//                 }
//             }
//         }
//     }
    
//     private static int sumArray(int [] nums){
//         int ret = 0;
//         for(int i = 0 ;i < nums.length; i ++){
//             ret += nums[i];
//         }
//         return ret;
//     }
// }

 //Memory Limit Exceeded



public class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 0) return new ArrayList<>();
        else if (n == 1) {
            List<Integer> ret = new ArrayList<>();
            ret.add(0);
            return ret;
        }
        List<Integer>[] lists = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            lists[i] = new ArrayList<>();
        }
        for (int i = 0; i < edges.length; i++) {
            int v1 = edges[i][0];
            int v2 = edges[i][1];
            lists[v1].add(v2);
            lists[v2].add(v1);
        }
        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (lists[i].size() == 1) {
                leaves.add(i);
            }
        }
        int count = n;
        while (count > 2) {
            int size = leaves.size();
            count -= size;
            List<Integer> newLeaves = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                int leaf = leaves.get(i);
                for (int j = 0; j < lists[leaf].size(); j++) {
                    int toRemove = lists[leaf].get(j);
                    lists[toRemove].remove(Integer.valueOf(leaf));
                    if (lists[toRemove].size() == 1)
                        newLeaves.add(toRemove);
                }
            }
            leaves = newLeaves;
        }
        return leaves;
    }
}