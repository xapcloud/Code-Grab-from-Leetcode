###232 Implement Queue using Stacks

Implement the following operations of a queue using stacks.


push(x) -- Push element x to the back of queue.


pop() -- Removes the element from in front of queue.


peek() -- Get the front element.


empty() -- Return whether the queue is empty.


Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).


Implement the following operations of a queue using stacks.


push(x) -- Push element x to the back of queue.


pop() -- Removes the element from in front of queue.


peek() -- Get the front element.


empty() -- Return whether the queue is empty.


Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

Subscribe to see which companies asked this question
###Solution
```java
class MyQueue {
    
    private Stack<Integer> in = new Stack<>();
    private Stack<Integer> out = new Stack<>();
    
    // Push element x to the back of queue.
    public void push(int x) {
        in.push(x);
    }

    // Removes the element from in front of queue.
    public void pop() {
        if(!out.isEmpty())
            out.pop();
        else{
            while(!in.isEmpty()){
                out.push(in.pop());
            }
            out.pop();
        }
        
    }

    // Get the front element.
    public int peek() {
         if(!out.isEmpty())
            return out.peek();
        else{
            while(!in.isEmpty()){
                out.push(in.pop());
            }
            return out.peek();
        }
    }

    // Return whether the queue is empty.
    public boolean empty() {
        return in.isEmpty()&&out.isEmpty();
    }
}