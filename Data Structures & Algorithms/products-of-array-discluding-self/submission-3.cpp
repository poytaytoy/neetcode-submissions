class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        vector<int> zero_index; 
        int accum = 1; 

        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 0 && zero_index.size() == 0){
                zero_index.emplace_back(i); 
                continue;
            }

            accum *= nums[i];
        } 

        if (zero_index.size()){
            vector<int> output(nums.size(), 0);

            output[zero_index[0]] = accum;

            return output;  
        }

        vector<int> output; 

        for (int i = 0; i < nums.size(); i++){
            output.emplace_back(accum / nums[i]);
        } 

        return output; 

    }
};
