###282 Expression Add Operators

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.


Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

Credits:Special thanks to @davidtan1890 for adding this problem and creating all test cases.

Subscribe to see which companies asked this question


Show Tags

Divide and Conquer



Show Similar Problems

 (M) Evaluate Reverse Polish Notation
 (H) Basic Calculator
 (M) Basic Calculator II
 (M) Different Ways to Add Parentheses



Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples: 
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

Credits:Special thanks to @davidtan1890 for adding this problem and creating all test cases."123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
Credits:Special thanks to @davidtan1890 for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    // public List<String> addOperators(String num, int target) {
    //     List<String> result = new ArrayList<String>();
    //     if(num.length() == 0 || num.length() == 1 && Integer.parseInt(num) != target)
    //         return result;
    //     if(num.length() == 1 && Integer.parseInt(num) == target){
    //         result.add(num);
    //         return result;
    //     }
        
    //     for(int i = 0; i < num.length(); i ++){
            
    //         int temp = 0;
    //         String pre = num.substring(0,i+1);
    //         if(pre.length()>=10 && (Integer.parseInt(pre.substring(0,i))>214748364||Integer.parseInt(pre.substring(0,i))==214748364 && Integer.parseInt(pre.substring(i,i+1))>7)){
    //             break;
    //         }else{
    //             temp = Integer.parseInt(pre);   
    //         }
            
            
    //         String sub = num.substring(i+1,num.length());
            
    //         if(i == num.length() - 1 ){
    //             if(temp == target&&(pre.charAt(0)!='0'||pre.length()==1)){
    //                 result.add(temp+"");
    //             }
                
    //         }else{
    //             //å æ³
    //             List<String> plus = addOperators(sub, target-temp);
    //             if(!plus.isEmpty()){
    //                 for(String s: plus)
    //                     result.add(temp+"+"+s);
    //             }
    //             //åæ³
    //             List<String> minus = addOperators(sub, temp-target);
    //               if(!minus.isEmpty()){
    //                 for(String s: minus)
    //                     result.add(temp+"-"+s);
    //             }
    //             if(temp!=0 && target%temp == 0 || (temp ==0 &&  target == 0)){
	   //             	List<String> multi = new ArrayList<String>();
	   //             	if(temp ==0)
	   //             		multi = addOperators(sub, 0);
	   //             	else
	   //             		multi = addOperators(sub, target/temp);
	   //                 if(!multi.isEmpty()){
	   //                     for(String s: multi)
	   //                     result.add(temp+"*"+s);
		  //                 // System.out.println(sss+result+"******"+depth);

	   //                 }
	   //         }
    //         }
    //     }
    //     return result;
    // }
    
    public List<String> addOperators(String num, int target) {
    List<String> res = new LinkedList<>();
    backtrack(num.toCharArray(), res, "", 0, target, 0);
    return res;
}

private void backtrack(char[] nums, List<String> res, String str, int pos, long rem, long prevNum) {
    if(rem == prevNum && pos == nums.length) {
        res.add(str);
        return;
    }
    long val = 0;
    for(int i=pos; i<nums.length; i++) {
        val = val*10 + (nums[i]-'0');
        if(i>pos && nums[pos]=='0') break;
        if(pos==0) backtrack(nums, res, ""+val, i+1, rem, val);
        else {
            backtrack(nums, res, str+"+"+val, i+1, rem-prevNum, val);
            backtrack(nums, res, str+"-"+val, i+1, rem-prevNum, -val);
            backtrack(nums, res, str+"*"+val, i+1, rem, prevNum*val);
        }
    }
}
}