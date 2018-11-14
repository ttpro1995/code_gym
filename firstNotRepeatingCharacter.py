__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"
__link__ = "https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC"

def firstNotRepeatingCharacter(s):
    appear = set()
    first_appear = []

    for c in s:
        if c not in appear: ## never appear
            first_appear.append(c)
            appear.add(c)
        else: # already appear
            if c in first_appear:
                first_appear.remove(c) # that repeat, so remove from appear list

    if len(first_appear) == 0:
        return "_"
    else:
        return first_appear[0]


print(firstNotRepeatingCharacter("abacabad"))
print(firstNotRepeatingCharacter("abacabaabacaba"))