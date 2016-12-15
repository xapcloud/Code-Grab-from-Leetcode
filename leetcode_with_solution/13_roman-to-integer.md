###13 Roman to Integer
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.Given a roman numeral, convert it to an integer.Input is guaranteed to be within the range from 1 to 3999.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int romanToInt(String s) {
        String[] str = new String[] { "M", "CM", "D", "CD", "C", "XC", "L",
				"XL", "X", "IX", "V", "IV", "I" };
		int[] val = new int[] { 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5,
				4, 1 };
		
		HashMap<String, Integer> map = new HashMap<String, Integer>();
		
		int result=0;
		
		for(int i = 0; i < str.length; i ++){
			map.put(str[i], val[i]);
		}
		while(s.length()>0){
			if(s.length() > 1 && map.get(s.substring(s.length()-2, s.length()))!=null){
				result+=map.get(s.substring(s.length()-2, s.length()));
				s = s.substring(0, s.length()-2);
			}else{
				result+=map.get(s.substring(s.length()-1, s.length()));
				s = s.substring(0, s.length()-1);
			}			
		}
		return result;
    }
}