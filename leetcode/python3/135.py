from typing import List


# def candy(self, ratings: List[int]) -> int:
#     k = []
#     for i, r in enumerate(ratings):
#         if i == 0:
#             k.append(1)
#             continue
#         if r <= ratings[i - 1]:
#             k.append(1)
#             if k[i - 1] == 1:  # and r < ratings[i-1]:
#                 b1 = i
#                 b2 = i - 1
#                 while b2 >= 0:
#                     if ratings[b1] < ratings[b2] and k[b2] == k[b1]:
#                         k[b2] = k[b1] + 1
#                     b1 -= 1
#                     b2 -= 1
#                 # k[i-1] = 2
#             continue
#         if r > ratings[i - 1]:
#             k.append(k[i - 1] + 1)
#             continue
#     print(k)
#     return sum(k)

class Solution:


    def candy(self, ratings: List[int]) -> int:
        def select_max(a, b):
            if a > b:
                return a
            else:
                return b

        k = []
        for i, r in enumerate(ratings):
            if i == 0:
                k.append(1)
                continue
            if r <= ratings[i-1]:
                k.append(1)
                continue
            if r > ratings[i-1]:
                k.append(k[i-1] + 1)
                continue

        b1 = len(ratings)-1
        b2 = b1 - 1
        while b2 >= 0:
            if ratings[b1] < ratings[b2]:
                k[b2] = select_max(k[b2], k[b1] + 1)
            b1 -= 1
            b2 -= 1
        print(k)
        return sum(k)


if __name__ == "__main__":
    x = [1,3,2,2,1]
    x2 = [1,2,87,87,87,2,1]
    sol = Solution()
    print(sol.candy([20000,19999,19998,19997,19996,19995,19994]))
    print(sol.candy([0,1,2,3,2,1]))
    print(sol.candy([1,0,2]))
    print(sol.candy(x))
    print(sol.candy(x2))
