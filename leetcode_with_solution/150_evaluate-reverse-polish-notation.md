###150 Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.


Valid operators are +, -, *, /. Each operand may be an integer or another expression.


Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public int evalRPN(String[] tokens) {
        HashSet<String> op = new HashSet<String>();
        op.add("+");
        op.add("-");
        op.add("*");
        op.add("/");
        
        Stack<Integer> s = new Stack<Integer>();
        
        for(int i = 0;i < tokens.length; i ++){
            if(!op.contains(tokens[i]))
                s.push(Integer.parseInt(tokens[i]));
            else{
                int r = s.pop();
                int l = s.pop();
                s.push(eval(r,l,tokens[i].charAt(0)));
            }
        }
        return s.pop();
    }
    
    private int eval(int r, int l, char op){
        int ret = 0;
        switch(op){
            case '+':
                ret = r+l;
                break;
            case '-':
                ret = l - r;
                break;
            case '*':
                ret = l*r;
                break;
            case '/':
                ret = l/r;
                break;
        }   
        return ret;
    }
    
}