###401 Binary Watch
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.
Example:
Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:

The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).Each LED represents a zero or one, with the least significant bit on the right.For example, the above binary watch reads "3:25".Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.Example:
Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]Note:

The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".

Subscribe to see which companies asked this question
###Solution
```java
import java.util.*;
public class Solution {
    public List<String> readBinaryWatch(int num) {
        
        Hashtable<Integer,Integer> ht1 = new Hashtable<Integer,Integer>();
        for(int i = 0; i < 60; i ++){
            ht1.put(i,BitCount(i));
        }
        
        Hashtable<Integer,List<String>> ht2 = new Hashtable<Integer,List<String>>();
        for(int i = 0;i < 720; i ++){
            int h = i/60;
            int min = i%60;
            String temp = h+":";
            
            if(min < 10)
                temp = temp+"0"+min;
            else
                temp = temp+min;
                
            int n = ht1.get(h)+ht1.get(min);
            
            if(ht2.containsKey(n))
                ht2.get(n).add(temp);
            else{
                List<String> l = new ArrayList<String>();
                l.add(temp);
                ht2.put(n,l);
            }
            
        }
        if(ht2.containsKey(num))
            return ht2.get(num);
        else
            return new ArrayList<String>();
        
    }
    
    private int BitCount(int n) {
        int tmp = n - ((n >>1) &033333333333) - ((n >>2) &011111111111);
        return ((tmp + (tmp >>3)) &030707070707) %63;
    }
}