#include <utility>
#include <algorithm>

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<std::pair<int, int>> pair_count; 

        for (int i = -1000; i <= 1000; i++){
            pair_count.emplace_back(i, 0); 
        }

        for (auto& i: nums){
            int new_index = i + 1000; 
            pair_count[new_index].second += 1; 
        }

        std::sort(pair_count.begin(), pair_count.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            return a.second > b.second;
        }); 

        vector<int> output;

        for (int i = 0; i < k; i++){
            output.emplace_back(pair_count[i].first);
        }

        return output; 
    }
};
