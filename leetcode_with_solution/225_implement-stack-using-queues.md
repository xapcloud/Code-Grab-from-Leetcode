###225 Implement Stack using Queues

Implement the following operations of a stack using queues.


push(x) -- Push element x onto stack.


pop() -- Removes the element on top of the stack.


top() -- Get the top element.


empty() -- Return whether the stack is empty.


Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).



Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.

Credits:Special thanks to @jianchao.li.fighter for adding this problem and all test cases.
Implement the following operations of a stack using queues.


push(x) -- Push element x onto stack.


pop() -- Removes the element on top of the stack.


top() -- Get the top element.


empty() -- Return whether the stack is empty.


Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).


Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.
Credits:Special thanks to @jianchao.li.fighter for adding this problem and all test cases.Subscribe to see which companies asked this question
###Solution
```java
class MyStack {
 private Queue<Integer> inquene = new LinkedList<Integer>();
     private Queue<Integer> outquene = new LinkedList<Integer>();
	    int temp =0;
	    // Push element x onto stack.
	    public void push(int x) {
	        inquene.add(x);
	    }

	    // Removes the element on top of the stack.
	    public void pop() {
	      if( inquene.isEmpty()){
	    	  while( !outquene.isEmpty() ){
	    		  temp = outquene.peek();
	    		  outquene.poll();
	    		  if( !outquene.isEmpty() ){
	    			  inquene.add(temp);
	    		  }
	    	  }
	    	 
	    	  
	      }else{
	            while(  !inquene.isEmpty() ){
	            	 temp = inquene.peek();
		    		  inquene.poll();
		    		  if( !inquene.isEmpty() ){
		    			  outquene.add(temp);
		    		  }
	            }
	        }
	    }

	    // Get the top element.
	    public int top() {
	      
	        if( inquene.isEmpty() ){
	        	while( !outquene.isEmpty() ){
		    		  temp = outquene.peek();
		    		  outquene.poll();
		    	  }
	        	return temp;
	        }else{
	        	 while(  !inquene.isEmpty() ){
	            	temp = inquene.peek();
		    		inquene.poll();
		    		outquene.add(temp);
	            }
	        	 return temp;
	        }
	        
	    }

	    // Return whether the stack is empty.
	    public boolean empty() {
	        return inquene.isEmpty()&&outquene.isEmpty();
	    }

}