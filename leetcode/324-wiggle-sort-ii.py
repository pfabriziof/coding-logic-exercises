from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        # Add 1 so the left part in odd array has the extra element
        mid = (len(nums) + 1) // 2 # Floor division by 2
        left, right = nums[:mid][::-1], nums[mid:][::-1] # split array and reverse
        nums[::2], nums [1::2] = left, right
        return nums

if __name__ == "__main__":
    test_1 = [1,5,1,1,6,4] # output: [1,6,1,5,1,4]
    test_2 = [1,3,2,2,3,1] # output: [2,3,1,3,1,2]
    test_3 = [0,1,2,3]

    solution = Solution()
    print(solution.wiggleSort(test_1))
    print(solution.wiggleSort(test_2))
    print(solution.wiggleSort(test_3))

