# https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counting_dict = {}
        m = len(nums)
        tar = m/2
        tar_c = 0
        result = 0
        for e in nums:
            if e not in counting_dict:
                counting_dict[e] = 1
            else:
                counting_dict[e] += 1
            if counting_dict[e] > tar:
                return e


if __name__ == "__main__":
    nums = [1,3,3, 5, 6, 7, 7, 7, 7, 8]
    val = 3
    sol = Solution()
    res = sol.majorityElement(nums)
    print(res)
