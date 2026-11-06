#include <string>
#include <unordered_map>
#include <set>
#include <queue>

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char, int> s1_set; 

        for (char character: s1){
            s1_set[character] += 1;  
        }

        std::unordered_map<char, int> s2_set = s1_set; 
        std::queue<char> nth_last;

        for (char character: s2){ 
            if (!s2_set.contains(character)){
                while (!nth_last.empty()){
                    char front = nth_last.front(); 
                    s2_set[front] += 1;
                    nth_last.pop(); 

                    if (front == character){
                        break;
                    }
                }
            }

            if (s2_set.contains(character)){
                nth_last.push(character); 

                s2_set[character] -= 1; 
                if (s2_set[character] == 0){
                    s2_set.erase(character);
                    if (s2_set.empty()){
                        return true;
                    }
                }
            } 
        }

       

        return false;
    }
};
