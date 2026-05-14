from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # 1. array of integers of length n
        # 2. where 1 <= a[i] <= n

        # So the numbers in the list also express locations within
        # the array. What we can do is visit these locations, mark them
        # with negative numbers and if it was previously marked, we add
        # the current number to the answer array.
        answer = []
        for i,k in enumerate(nums):
            if nums[abs(k)-1] < 0:
                answer.append(abs(nums[i]))
            else:
                nums[abs(k)-1] *= -1

        return answer


if __name__ == "__main__":
    test_1 = [4,3,2,7,8,2,3,1] # output: [2,3]
    test_2 = [1,1,2] # output: [1]
    test_3 = [1] # output: []

    solution = Solution()
    print(solution.findDuplicates(test_1))
    print(solution.findDuplicates(test_2))
    print(solution.findDuplicates(test_3))

