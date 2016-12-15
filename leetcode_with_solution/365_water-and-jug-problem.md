###365 Water and Jug Problem
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available.
You need to determine whether it is possible to measure exactly z litres using these two jugs.
If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.


Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True


Example 2:

Input: x = 2, y = 6, z = 5
Output: False


Credits:Special thanks to @vinod23 for adding this problem and creating all test cases.You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available.
You need to determine whether it is possible to measure exactly z litres using these two jugs.If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.
Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.

Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True


Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False


Input: x = 2, y = 6, z = 5
Output: False
Credits:Special thanks to @vinod23 for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean canMeasureWater(int x, int y, int z) {
        
        // int a = Math.max(x,y);
        // int b = Math.min(x,y);
        
        // if(z > a+b)
        //     return false;
        
        // List<Integer> l = new ArrayList<Integer>();
        
        // l.add(a);
        // l.add(b);
        // l.add(a-b);
        // l.add()
        
        return z == 0 || (x+y >= z && z%gcd(x,y)==0);
        
    }
    
    public int gcd(int a, int b) {
        if (b==0) return a;
        return gcd(b,a%b);
    }
}