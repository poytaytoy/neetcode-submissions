class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        int zero_index = -1;
        int accum = 1; 

        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 0 && zero_index == -1){
                zero_index = i;  
                continue;
            }

            accum *= nums[i];
        } 

        if (zero_index != -1){
            vector<int> output(nums.size(), 0);

            output[zero_index] = accum;

            return output;  
        }

        vector<int> output; 

        for (int i = 0; i < nums.size(); i++){
            output.emplace_back(accum / nums[i]);
        } 

        return output; 

    }
};
