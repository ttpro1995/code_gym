from typing import List


# def start_at(idx):
#     """
#     check if we can start at idx
#     """
#     course_gas = gas[:idx] + gas[idx:]
#     course_cost = cost[:idx] + cost[idx:]
#     gas_tank = 0
#     for gas_i, cost_i in zip(course_gas, course_cost):
#         gas_tank += gas_i
#         gas_tank -= cost_i
#         if gas_tank < 0:
#             return False
#     return True

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = [g - c for g, c in zip(gas, cost)]
        max_end_here = 0
        start_end_here = 0
        flag = 1
        if sum(surplus) < 0:
            return -1

        max_so_far = 0
        start_so_far = 0
        for i, e in enumerate(surplus + surplus):
            max_end_here += e
            if max_end_here > 0 and flag:
                start_end_here = i
                flag = 0
            if max_so_far < max_end_here:
                max_so_far = max_end_here
                start_so_far = start_end_here
            if max_end_here < 0:
                max_end_here = 0
                flag = 1
        return start_so_far

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    gas2 = [5,8,2,8]
    cost2 = [6,5,6,6]
    sol = Solution()
    print(sol.canCompleteCircuit(gas, cost))
    print(sol.canCompleteCircuit(gas2, cost2))