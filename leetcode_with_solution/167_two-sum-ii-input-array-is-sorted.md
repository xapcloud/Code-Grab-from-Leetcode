###167 Two Sum II - Input array is sorted
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.You may assume that each input would have exactly one solution.
Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int[] twoSum(int[] numbers, int target) {
        //å¯ä»¥ç¨äºåæ³è¿ä¸æ­¥ä¼å
        
        int l = numbers.length;
        int index1 = 0;
        int index2 = l-1;
        
        int sum = numbers[index1]+numbers[index2];
        while(sum!=target && index1<index2){
            if(sum>target){
                index2--;
                sum = numbers[index1]+numbers[index2];
            }else{
                index1++;
                sum = numbers[index1]+numbers[index2];
            }
                
        }
        int []result = new int[2];
        result[0] = index1+1;
        result[1] = index2+1;
        
        return result;
        
    }
}