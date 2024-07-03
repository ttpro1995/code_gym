# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        cur = -200
        while p < len(nums):
            if cur == nums[p]:
                nums.pop(p)
            else:
                cur = nums[p]
                p+=1


if __name__ == "__main__":
    nums = [1,3 , 3, 5, 6, 7, 7, 8]
    val = 3
    sol = Solution()
    sol.removeDuplicates(nums)
    print(nums)
