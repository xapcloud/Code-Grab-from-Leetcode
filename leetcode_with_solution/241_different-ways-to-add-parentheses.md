###241 Different Ways to Add Parentheses
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".
((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]

Example 2
Input: "2*3-4*5"
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.Input: "2-1-1".((2-1)-1) = 0
(2-(1-1)) = 2Output: [0, 2]Input: "2*3-4*5"(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10Output: [-34, -14, -10, -10, 10]Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> result = new ArrayList<Integer>();

        // if(input.length() == 1){
        //     result.add(input.charAt(0)-'0');
        //     return result;
        // }
        // if(input.length() == 3){
        //     result.add(operate(input.charAt(0)-'0',input.charAt(2)-'0',input.charAt(1)));   
        //     return result;
        // }
        
        // int len = (input.length() - 1)/2;
        
        // for(int i = 0; i < len ; i ++){
        //     String s1 = input.substring(0,1+i*2);
        //     char op = input.charAt(1+i*2);
        //     String s2 = input.substring(1+i*2 + 1);
        //     result = setOp(diffWaysToCompute(s1),diffWaysToCompute(s2),op);
        // }
        
        List<Integer> opList = new ArrayList<Integer>();
        for(int i = 0; i < input.length(); i ++){
            if(input.charAt(i)<='9'&&input.charAt(i)>='0'){
                
            }else{
                opList.add(i);
            }
        }
        
        if(opList.size() == 0){
            int temp = 0;
            for(int i = 0; i < input.length(); i++){
                temp = temp*10+(input.charAt(i)-'0');
            }
            result.add(temp);
            //return result;
        }else{
            for(int x : opList){
                String s1 = input.substring(0,x);
                char op = input.charAt(x);
                String s2 = input.substring(x+1);
                List<Integer> tempResult = setOp(diffWaysToCompute(s1),diffWaysToCompute(s2),op);
                
                for(int y:tempResult){
                    result.add(y);
                }
                
                System.out.println(s1+"\t"+op+"\t"+s2);
               // return result;
            }
        }
        
        
        return result;
    }
    
    private List<Integer> setOp(List<Integer> l1, List<Integer> l2, char op){
        List<Integer> l = new ArrayList<Integer>();
        
        for(int a: l1){
            for(int b: l2){
                l.add(operate(a,b,op));
            }
        }
        
//         List<Integer> l = new ArrayList<Integer>();
        
//         Iterator<Integer> iterator=hs.iterator();
// 		while(iterator.hasNext()){
// 			l.add(iterator.next());
// 		}
        
        return l;
    }
    
    
    private int operate(int a, int b, char op){
        switch (op){
            case '+':
                return a+b;
            case '-':
                return a-b;
            case '*':
                return a*b;
            default:
                return 0;
        }
    }
    
}