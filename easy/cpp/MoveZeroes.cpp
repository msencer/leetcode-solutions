class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        if (nums.size() < 2)
            return;
        int swapIndex = 1;
        int i = 0;
        while(swapIndex < nums.size()){
            
            if (nums[i] == 0 && nums[swapIndex] != 0)
            {
                nums[i] = nums[swapIndex];
                nums[swapIndex] = 0;
                swapIndex++;
                i++;
            }
            else if(nums[i] == 0 && nums[swapIndex] == 0)
            {
                  swapIndex++;
            }
            else
            {
                i++;
                swapIndex++;
            }
        }
    }
};