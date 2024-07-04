# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 0
        cur = -200
        flag = 0
        while p < len(nums):
            if cur == nums[p]:
                flag += 1
                if flag > 1:
                    nums.pop(p)
                else:
                    p+=1
            else:
                cur = nums[p]
                p+=1
                flag = 0


if __name__ == "__main__":
    nums = [1,3,3, 5, 6, 7, 7, 7, 7, 8]
    val = 3
    sol = Solution()
    sol.removeDuplicates(nums)
    print(nums)
