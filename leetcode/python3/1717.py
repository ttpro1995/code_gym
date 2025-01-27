class Solution:

    def find_substring(self, s: list, first: str, second: str):
        # ss = "".join(s)
        i = 0
        flag_second = 0
        while i < len(s) - 1:
            if s[i] == first[0] and s[i+1] == first[1]:
                return first
            if s[i] == second[0] and s[i+1] == second[1]:
                flag_second = 1
            i+= 1
        if flag_second:
            return second
        else:
            return None
    def maximumGain(self, s: str, x: int, y: int) -> int:
        i = 0
        score = 0
        s = list(s)
        # score_log = []
        if x > y:
            first = "ab"
            second = "ba"
            score_first = x
            score_seond = y
        else:
            first = "ba"
            second = "ab"
            score_first = y
            score_seond = x

        substr = self.find_substring(s, first, second)
        while substr:
            if substr == first:
                score_plus = score_first
            else:
                score_plus = score_seond
            i = 0
            while i < len(s) - 1:
                next = s[i] + s[i + 1]
                # if next == first:
                if s[i] == substr[0] and s[i+1] == substr[1]:
                    # s.pop(i)
                    # s.pop(i)
                    s[i:i+2] = []
                    score += score_plus
                    # score_log.append(score_plus)
                    if i > 0:
                        i-= 1
                else:
                    i += 1
            substr = self.find_substring(s, first, second)

        # print(score_log)
        return score

if __name__ == "__main__":
    sol = Solution()
    # 4 ab
    # 5 ba
    print(sol.maximumGain("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", 123, 3495))
    # print(sol.maximumGain("cdbcbbaaabab", 4, 5))