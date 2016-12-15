###227 Basic Calculator II
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
You may assume that the given expression is always valid.
Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5



Note: Do not use the eval built-in library function.

Credits:Special thanks to @ts for adding this problem and creating all test cases.Implement a basic calculator to evaluate a simple expression string.The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.You may assume that the given expression is always valid.Some examples:

"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5


"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.
Credits:Special thanks to @ts for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int calculate(String s) {
        if(s == null || s.length() == 0) 
            return 0;
        
        Stack<Integer> stack = new Stack<Integer>();
        int curNum = 0;
        char op = '+';
        int l = s.length();
        
        for(int i = 0; i < l ; i++){
            if(Character.isDigit(s.charAt(i)))
                curNum = curNum * 10 + (s.charAt(i) - '0');
            if ((!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ')||i == l -1){
                switch(op){
                    case '+':stack.push(curNum);
                        break;
                    case '-':stack.push(-curNum);
                        break;
                    case '*':stack.push(stack.pop()*curNum);
                        break;
                    case '/':stack.push(stack.pop()/curNum);
                        break;
                }
                op = s.charAt(i);
                curNum = 0;
            }
        }
        int result = 0;
        for(int n: stack){
            result+=n;
        }
        
        return result;
    }
}