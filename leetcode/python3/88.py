from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1.pop()
        cur = 0
        ahead = 0
        if not nums2:
            return
        n2_v = nums2.pop(0)
        last = 0
        while True:

            if ahead < len(nums1):
                ahead_v = nums1[ahead]
                if ahead_v > n2_v:
                    nums1.insert(ahead, n2_v)
                    ahead+=1
                    if nums2:
                        n2_v = nums2.pop(0)
                    else:
                        return
                else:
                    ahead+=1
            else:
                nums1.insert(ahead, n2_v)
                ahead+=1
                if nums2:
                    n2_v = nums2.pop(0)
                else:
                    return

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)