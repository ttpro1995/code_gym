from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counting_dict = {}
        highest_h = 0
        for h in citations:
            for i in range(highest_h, h + 1):
                if i not in counting_dict.keys():
                    counting_dict[i] = 1
                else:
                    counting_dict[i] += 1
                if counting_dict[i] >= i:
                    highest_h = i

        # last_key = 0
        # for key, items in counting_dict.items():
        #     if items >= key:
        #         last_key = key
        #     else:
        #         break
        return highest_h



if __name__ == "__main__":
    x1 = [3,0,6,1,5]
    sol = Solution()
    print(sol.hIndex(x1))