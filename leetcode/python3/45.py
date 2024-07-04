# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jump_log = []
        jump_count = 0
        while i < len(nums) - 1:
            current_val = nums[i]
            current_index = i

            # look ahead at option
            max_range = current_val
            # check if max_range help us reach final index
            if i + max_range >= len(nums) - 1:
                return jump_count + 1
            jump_to = i + 1
            for steps in range(1, current_val + 1):
                tar_pos = i + steps
                if tar_pos >= len(nums):
                    return jump_count + 1
                else:
                    tar_val = nums[i + steps]
                predicted_range = i + steps + tar_val
                if predicted_range > max_range:
                    max_range = predicted_range
                    jump_to = i + steps
            jump_log.append((i, jump_to))
            i = jump_to
            jump_count += 1

        print(jump_log)
        return jump_count

if __name__ == "__main__":
    nums1 = [2,3,1,1,4]
    nums2 = [2, 1]
    nums3 = [2,3,1]

    sol = Solution()
    # print(sol.canJump(nums1))
    # print(sol.canJump(nums2))

    print(sol.jump(nums3))