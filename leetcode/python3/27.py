# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        point = 0
        while point < len(nums):
            while point < len(nums) and nums[point] == val:
                nums.pop(point)
            point+= 1
        return len(nums)


if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    sol = Solution()
    res = sol.removeElement(nums, val)
    print(nums)
    print(res)