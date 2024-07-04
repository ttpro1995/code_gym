from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        accumulate_profit = 0
        buy = prices[0]
        pending_profit = 0
        for i, e in enumerate(prices):
            if e < buy:
                buy = e
                predicted_profit = 0
            else:
                predicted_profit = e - buy
            if pending_profit < predicted_profit:
                pending_profit = predicted_profit
            elif pending_profit > 0:  # predict profit is not good, should I sell it yesterday
                accumulate_profit += pending_profit
                if prices[i-1] < prices[i]:
                    buy = prices[i-1]
                else:
                    buy = prices[i]
                pending_profit = e - buy
                if pending_profit < 0:
                    pending_profit = 0
            else:
                continue
        if pending_profit > 0:
            accumulate_profit += pending_profit
        return accumulate_profit


if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    sol = Solution()
    res = sol.maxProfit(nums)
    print(res)
