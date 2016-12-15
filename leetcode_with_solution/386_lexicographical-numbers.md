###386 Lexicographical Numbers

Given an integer n, return 1 - n in lexicographical order.


For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].


Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.

Given an integer n, return 1 - n in lexicographical order.

For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].

Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
Subscribe to see which companies asked this question
###Solution
```java
public class Solution {
	public  List<Integer> lexicalOrder(int n) {
		int bit = 1;
		int temp = n;
		while (temp >= 10) {
			temp /= 10;
			bit++;
		}

		int num;
		List<Integer> ret = new ArrayList<Integer>();
		int x = Math.min(9,n);
		for (int i = 1; i <= x; i++) {
			num = i;
			addNum(i,bit,n,ret);
		}
		return ret;
	}

	private  void addNum(int i, int j, int n, List<Integer> ret) {
		//System.out.println(ret);

		if (j == 1){
			if(i<=n)
				ret.add(i);
		}
		else {
			if(i<=n)
				ret.add(i);
			for (int k = 0; k <= 9; k++) {
				addNum(i * 10 + k, j - 1, n, ret);
			}
		}
	}

}