#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
// #include <cstdio>
using std::cout;
using std::endl;

class Solution {
    public:
        int maxSumDivThree(std::vector<int>& nums){
            int total = 0;
            float smallest_one = std::numeric_limits<float>::infinity();
            float smallest_two = std::numeric_limits<float>::infinity();
            for (int i=0; i < nums.size(); i++){
                int n = nums[i];
                total += n;
                if (n % 3 == 1){
                    auto min_it_auto = std::min_element(nums.begin(), nums.end());
                    smallest_one = *min_it_auto;
                }
                if (n % 3 == 2){
                    auto min_it_auto = std::min_element(nums.begin(), nums.end());
                    smallest_two = *min_it_auto;
                }
            }
            cout << "Total sum: " << total << endl;
            if (total % 3 == 0) {
                return total;
            }
            if (total % 3 == 1){
                return total - smallest_one;
            }
            if (total % 3 == 2){
                return total - smallest_two;
            }

            return 0;
        }
};



int main(){
    std::cout << "Hello, world!" << std::endl;
    // printf("Hello, world!\n");
    std::vector nums_1 = {3,6,5,1,8};
    std::vector nums_2 = {4};
    std::vector nums_3 = {1,2,3,4,4};
    Solution solution = Solution();
    solution.maxSumDivThree(nums_1);

    return 0;
}


