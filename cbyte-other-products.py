"""coderbyte - WaveSorting"""
# problem comes from https://youtu.be/ydVhD86uHJA?si=zT4FKZQrM7xPRnoQ

from typing import List

class Solution:
    def otherProducts(self, nums: List[int]) -> str:
        result = []
        for i in nums:
            oproduct = 1
            for j in nums:
                if j != i:
                    oproduct *= j
            result.append(oproduct)
        return '-'.join(map(str,result))



if __name__ == "__main__":
    test_1 = [1,2,3,4,5] # output: 120-60-40-30-24
    test_2 = [1,4,3] # output: 12-3-4
    test_3 = [3,1,2,6] # output: 12-36-18-6

    solution = Solution()
    print(solution.otherProducts(test_1))
    print(solution.otherProducts(test_2))
    print(solution.otherProducts(test_3))

