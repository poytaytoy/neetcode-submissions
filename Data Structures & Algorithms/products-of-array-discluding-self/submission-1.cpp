class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {

        vector<int> storage;    
        vector<int> storage2; 

        for (int i = 0; i < nums.size(); i++){

            if (i == 0){
                storage.emplace_back(1); 
                storage2.emplace_back(1); 
            } else {
                int back = i - 1; 
                storage.emplace_back(storage[back] * nums[back]);
                storage2.emplace_back(storage2[back] * nums[nums.size() - i]);
            }
        }


        vector<int> output; 

        for (int i = 0; i < nums.size(); i++){
            output.emplace_back(storage[i] * storage2[nums.size() - 1 - i]);
        }


        return output; 
    }
};
