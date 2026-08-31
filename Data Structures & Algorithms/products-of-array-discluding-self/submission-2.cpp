class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
        vector<int> zero_index; 

        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 0){
                zero_index.emplace_back(i); 
            }
        } 

        if (zero_index.size() == 1){

            int accum = 1; 

            for (auto& i: nums){
                if (i != 0){
                    accum *= i; 
                }
            }

            vector<int> output(nums.size(), 0);

            output[zero_index[0]] = accum;

            return output;  
        }

        if (zero_index.size() >= 1){
            vector<int> output(nums.size(), 0);

            return output; 
        }   

        int accum = 1; 

        for (auto& i: nums){
            accum *= i; 
        }

        vector<int> output; 

        for (int i = 0; i < nums.size(); i++){
            output.emplace_back(accum / nums[i]);
        } 

        return output; 

    }
};
