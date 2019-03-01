__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"



def who_is_paying(name):
    result = []
    fulname = name
    result.append(fulname)
    short = name
    if len(name) > 2:
        short = name[0:2]
        result.append(short)
    return result



import codewar.Test as Test

Test.describe("Basic tests")
Test.assert_equals(who_is_paying("Mexico"),["Mexico", "Me"])
Test.assert_equals(who_is_paying("Melania"),["Melania", "Me"])
Test.assert_equals(who_is_paying("Melissa"),["Melissa", "Me"])
Test.assert_equals(who_is_paying("Me"),["Me"])
Test.assert_equals(who_is_paying(""), [""])
Test.assert_equals(who_is_paying("I"), ["I"])