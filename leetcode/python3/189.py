# https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            v = nums.pop()
            nums.insert(0, v)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    sol = Solution()
    res = sol.rotate(nums, k)
    print(nums)
