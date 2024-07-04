from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 999999999
        for e in prices:
            if e < buy:
                buy = e
            else:
                cur_profit = e - buy
                if cur_profit > profit:
                    profit = cur_profit
        return profit


if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    sol = Solution()
    res = sol.maxProfit(nums)
    print(res)
