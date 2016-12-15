###93 Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",


return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<String> restoreIpAddresses(String s) {
        
        String[]fragment = new String[4];
        List<String> result = new ArrayList<String>();
        
        if(s.length()>12){
            return result;
        }
        
        helpFunc(s,fragment,0,result);
        return result;
    }
    
    private void helpFunc(String reminder, String[] fragment, int numFragment, List<String> result){
        if(numFragment == 3){
            fragment[3] = reminder;
            check(fragment,result);  
        }else{
            for(int i = 0; i <= (reminder.length()-(4-numFragment)); i ++){
                String temp = reminder.substring(0,i+1);
                fragment[numFragment] = temp;
                helpFunc(reminder.substring(i+1),fragment,numFragment+1,result);
            }
        }
    }
    
    private void check(String[] fragment, List<String> result){
        
        boolean isValid = true;
        String re = "";
        for(int i = 0; i< fragment.length; i ++){
            if(fragment[i].length() >3){
                isValid = false;
                break;
            }
            int temp = Integer.parseInt(fragment[i]);
            if(temp<=255&&temp>=0 && (temp+"").equals(fragment[i])){
                re+=(fragment[i]+".");
            }else{
                isValid = false;
                break;
            }
        }   
        if(isValid){
            result.add(re.substring(0,re.length()-1));
        }
    }
}