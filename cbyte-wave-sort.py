"""coderbyte - WaveSorting"""
# problem comes from https://youtu.be/v7JdUO8LH9M?si=_YY-mCXqyeU-WemS

from typing import List

class Solution :
    def wiggleSort(self, nums: List[int]) -> bool:
        total_length = len(nums)
        count_helper = {}

        for i in nums:
            if i not in count_helper:
                count_helper[i] = 1
            else:
                count_helper[i] += 1

        max_ocurrencies = max(count_helper.values())
        print(count_helper)
        print(max_ocurrencies)

        if max_ocurrencies > total_length / 2:
            return False
        return True


if __name__ == "__main__":
    test_1 = [0,1,2,4,1,4] # True
    test_2 = [0,1,2,4,1,1,1] # False
    test_3 = [0,4,22,4,14,4,2] # True
    test_4 = [0,0,0,0] # False

    solution = Solution()
    print(solution.wiggleSort(test_1))
    print(solution.wiggleSort(test_2))
    print(solution.wiggleSort(test_3))
    print(solution.wiggleSort(test_4))
