###65 Valid Number
Validate if a given string is numeric.

Some examples:
"0" => true
"   0.1  " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.


Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
Validate if a given string is numeric.
Some examples:
"0" => true
"   0.1  " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
    public boolean isNumber(String s) {

        boolean dotFlag = false;
        boolean expFlag = false;

        s = s.trim();
        if (s == null || s.isEmpty()){
            return false;
        }
        if(s.length() == 1 && (s.charAt(0) == '.' || s.charAt(0) == 'e' || s.charAt(0) == '+' || s.charAt(0) == '-')){
            return false;
        }
        for (int i = 0 ; i < s.length() ; i++){
            int c = s.charAt(i) - '0';

            if (c >= 0 && c <= 9){
                continue;
            }
            else if (s.charAt(i) == '.'){
                if (!expFlag){
                    if (i == 0 && i+1 <= s.length() - 1 && s.charAt(i+1) == 'e'){
                        return false;
                    }
                    if(i > 0 && i+1 > s.length() -1  && (s.charAt(i - 1) == '-' || s.charAt(i - 1) == '+')){
                        return false;
                    }
                    if (dotFlag == false){
                        dotFlag = true;
                        continue;
                    }
                    else {
                        return false;
                    }
                }
                return false;
            }
            else if (i > 0 && s.charAt(i) == 'e'){
                if (expFlag == false && i+1 <= s.length() - 1 && s.charAt(i+1) != '.'){
                    expFlag = true;
                    continue;
                }
                else {
                    return false;
                }
            }
            else if (i > 0 && (s.charAt(i) == '+' || s.charAt(i) == '-')){
                if (i+1 <= s.length() - 1 && s.charAt(i - 1) == 'e'){
                    continue;
                }
                else {
                    return false;
                }
            }
            else if (i == 0 && (s.charAt(i) == '+' || s.charAt(i) == '-')){
                if(i+1 <= s.length() - 1 && s.charAt(i+1) == 'e'){
                    return false;
                }
                continue;
            }
            else if(s.charAt(i) == ' '){
                return false;
            }
            else {
                return false;
            }
        }
        return true;
    }
}