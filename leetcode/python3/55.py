# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        if 0 not in nums:
            return True

        while i < len(nums)-1:
            max_range = nums[i]
            max_idx = 0
            max_val = 0

            for step in range(1, max_range + 1):
                pos = i + step
                if pos > len(nums) - 1 - 1:
                    return True
                val = nums[pos] + pos
                if val > max_val:
                    max_val = val
                    max_idx = pos
            if max_idx <= i < len(nums)-1:
                return False

            i = max_idx

        return True


if __name__ == "__main__":
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    sol = Solution()
    # print(sol.canJump(nums1))
    # print(sol.canJump(nums2))
    nums3 = [1, 1, 1, 0]
    nums4 = [3,2,1,0,4]
    nums5 = [2, 5, 0, 0]
    nums6 = [5,9,3,2,1,0,2,3,3,1,0,0]
    print(sol.canJump(nums6))