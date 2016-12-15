###295 Find Median from Data Stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
Examples: 
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5 

Design a data structure that supports the following two operations:


void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


For example:

add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2

Credits:Special thanks to @Louis1992 for adding this problem and creating all test cases.Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.[2,3,4] , the median is 3[2,3], the median is (2 + 3) / 2 = 2.5 
Design a data structure that supports the following two operations:

For example:
add(1)
add(2)
findMedian() -> 1.5
add(3) 
findMedian() -> 2
Credits:Special thanks to @Louis1992 for adding this problem and creating all test cases.Subscribe to see which companies asked this question
###Solution
```java
public class MedianFinder {

    private ArrayList<Integer> array;
    // Adds a number into the data structure.
    
    public MedianFinder(){
        array = new ArrayList<Integer>();
    }
    
    public void addNum(int num) {
        //array.add(num);
        int sz = array.size();
        boolean hasAdd = false;
        for(int i = 0; i < sz; i ++){
            if(num <= array.get(i)){
                array.add(i,num);
                hasAdd = true;
                break;
            }
        }
        if(!hasAdd)
            array.add(num);
        
    }

    // Returns the median of current data stream
    public double findMedian() {
        //Collections.sort(array);
        if(array.size()%2==0){
            return ((double)(array.get(array.size()/2)+array.get(array.size()/2-1))/2);
        }else{
            return array.get(array.size()/2);
        }
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf = new MedianFinder();
// mf.addNum(1);
// mf.findMedian();