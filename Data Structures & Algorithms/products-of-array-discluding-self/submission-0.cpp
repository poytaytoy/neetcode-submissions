class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> storage;    
        vector<int> storage2(nums.size()); 

        for (int i = 0; i < nums.size(); i++){

            if (i == 0){
                storage.emplace_back(1); 
            } else {
                int back = i - 1; 

                storage.emplace_back(storage[back] * nums[back]);
            }
        }
        
        for (int i = nums.size() - 1; i >= 0; i--){
            if (i == nums.size() - 1){
                storage2[i] = 1; 
            } else {
                int back = i + 1; 
                storage2[i] = storage2[back] * nums[back];
            }
        }


        vector<int> output; 

        for (int i = 0; i < nums.size(); i++){
            output.emplace_back(storage[i] * storage2[i]);
        }


        return output; 
    }
};
