/*
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

*/

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        int A = rowIndex;
        vector<int> row;
    	vector<int> prevRow;
    	if (A == 0) {
    		row.push_back(1);
    		return row;
    	}
    	else if (A == 1)
    	{
    		row.push_back(1);
    		row.push_back(1);
    		return row;
    	}
    	prevRow.push_back(1);
    	prevRow.push_back(1);
    	for (int i = 2; i < A + 1; i++) {
    		row.clear();
    		row.push_back(1);
    		for (int j = 1; j < i; j++) {
    			row.push_back(prevRow[j - 1] + prevRow[j]);
    		}
    		row.push_back(1);
    		prevRow = row;
    	}
    	return row;
    }
};