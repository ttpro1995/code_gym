from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        customer_overlaps = []
        for i, c in enumerate(customers):
            time_wait_next = 0
            if i < len(customers) - 1:
                time_wait_next = customers[i + 1][0] - c[0]
                overlap = c[1] - time_wait_next
                if overlap > 0:
                    customer_overlaps.append(overlap)
                    customers[i + 1][1] += overlap
                else:
                    customer_overlaps.append(0)
        time_process = [x[1] for x in customers]
        # total_wait = sum(time_process) # + sum(customer_overlaps)
        total_wait = sum(time_process) # + sum(customer_overlaps)
        average = total_wait / len(customers)
        print("overlaps ", customer_overlaps)
        return average

if __name__ == "__main__":
    customers = [[1,2],[2,5],[4,3]]
    sol = Solution()
    print(sol.averageWaitingTime(customers))

