###49 Group Anagrams
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.Given an array of strings, group anagrams together.
For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]Note: All inputs will be in lower-case.Subscribe to see which companies asked this question
###Solution
```java
import java.util.*;
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Hashtable<String,List<String>> ht = new Hashtable<String,List<String>>();
        for(int i = 0;i < strs.length; i ++){
            char[] temp = strs[i].toCharArray();
            Arrays.sort(temp);
            String s = new String(temp);
            
            if(ht.containsKey(s)){
                ht.get(s).add(strs[i]);
            }else{
                List<String> ls = new ArrayList<String>();
                ls.add(strs[i]);
                ht.put(s,ls);
            }
        }
        
        List<List<String>> result = new ArrayList<List<String>>();
        Iterator<String> it = ht.keySet().iterator();
        while(it.hasNext()){
            result.add(ht.get(it.next()));
        }
        
        return result;
    }
}