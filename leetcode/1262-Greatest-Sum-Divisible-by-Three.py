from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> float:
        total = 0
        smallest_one = float("inf")
        smallest_two =  float("inf")
        for n in nums:
            total += n
            if n % 3 == 1:
                smallest_two = min(smallest_two, n + smallest_one)
                smallest_one = min(smallest_one, n)
            if n % 3 == 2:
                smallest_one = min(smallest_one, n + smallest_two)
                smallest_two = min(smallest_two, n)

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - smallest_one
        if total % 3 == 2:
            return total - smallest_two

        return 0

if __name__ == "__main__":
    test_1 = [3,6,5,1,8]
    test_2 = [4]
    test_3 = [1,2,3,4,4]

    solution = Solution()
    print(solution.maxSumDivThree(test_1))
    print(solution.maxSumDivThree(test_2))
    print(solution.maxSumDivThree(test_3))

