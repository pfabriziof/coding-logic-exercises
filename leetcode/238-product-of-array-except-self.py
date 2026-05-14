from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 3. Multiply both
        n = len(nums)
        res = [0] * n # create 0 array with the same length of nums

        # 1. Calculate prefix product
        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        print("prefix: ", res)
        # 2. Calculate sufix product
        suf = 1
        for i in range(n-1, -1, -1):
            # 3. Multiply the prefix (already stored) and the sufix
            res[i] *= suf
            suf *= nums[i]

        return res

if __name__ == "__main__":
    test_1 = [1,2,3,4] # output: [24,12,8,6]
    test_2 = [0,0] # output:  [0,0]
    test_3 = [-1,1,0,-3,3] # output [0,0,9,0,0]

    solution = Solution()
    print(solution.productExceptSelf(test_1))
    print(solution.productExceptSelf(test_2))
    print(solution.productExceptSelf(test_3))

