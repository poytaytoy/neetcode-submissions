class Solution {
public:
    int findMin(vector<int> &nums) {
        
        int left = 0;
        int right = nums.size() - 1;

        while (right - left > 1){
            int mid = left + (right - left) / 2; 

            if (nums[mid] < nums[left]){
                right = mid; 
            } else if (nums[mid] > nums[right]) { 
                left = mid;
            } else { 
                right -= 1;
            }
        }

        int min = nums[left];

        if (nums[right] < min){
            return nums[right]; 
        }

        return min;
    }
};
