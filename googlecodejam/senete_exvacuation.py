__author__ = "Thai Thien"
__email__ = "tthien@apcs.vn"

from googlecodejam.google_interactive import readline_int_list ,readline, readline_int, readline_two_int

import string


class Party:
    def __init__(self, name, num):
        self.name = name
        self.num = num

    def evacuate(self):
        self.num -= 1
        if self.num == 0:
            return True
        else:
            return False


def check_majority(remaining_member, n_party, first_party):
    if n_party == 1:
        return True
    if n_party == 0:
        return False
    if first_party.num > remaining_member/2:
        return True
    return False


def process_test_case():
    alphabet = list(string.ascii_uppercase)
    n_party = readline_int()
    parties_dict = dict()
    toks = readline_int_list()
    parties = []
    alpha_iter = 0
    remaining_member = 0
    for nmem in toks:
        remaining_member += nmem
        p = Party(alphabet[alpha_iter], nmem)
        alpha_iter += 1
        parties.append(p)
        parties_dict[alphabet[alpha_iter]] = p

    parties.sort(key=lambda party: party.num, reverse=True)

    answer_queue = []

    while(remaining_member > 0):
        # remove first member
        team = []
        p1 = parties[0].name
        p1_out_all = parties[0].evacuate()
        if (p1_out_all):
            n_party -= 1 # one party gone
        remaining_member -= 1 # one member gone
        team.append(p1)
        # sort
        parties.sort(key=lambda party: party.num, reverse=True)
        # remove second member
        p2 = parties[0].name
        p2_out_all = parties[0].evacuate()
        remaining_member -= 1 # one member gone
        parties.sort(key=lambda party: party.num, reverse=True)

        if (p2_out_all):
            n_party -= 1
        majority = check_majority(remaining_member, n_party, parties[0])

        if majority: # no good, undo
            parties_dict[p2].num+= 1
            remaining_member += 1
            if (p2_out_all):
                n_party += 1
        else: # no majority
            team.append(p2)

        answer_queue.append(team)
    ## done while loop
    return answer_queue


if __name__ == "__main__":
    t = readline_int()