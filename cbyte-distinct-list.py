"""coderbyte - Distinct List

Take the array of numbers and determine the total number of duplicate entires
"""
# problem comes from https://youtu.be/T7dBwPTrUIk?si=YhsGtZ3pjZWPqx0j

from typing import List

class Solution:
    def DistinctList(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))

        return len(nums) - len(unique_nums)



if __name__ == "__main__":
    test_1 = [0,-2,-2,5,5,5] # output: 3
    test_2 = [100,2,101,4] # output: 0


    solution = Solution()
    print(solution.DistinctList(test_1))
    print(solution.DistinctList(test_2))

