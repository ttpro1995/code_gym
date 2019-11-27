__link__ = "https://brilliant.org/problems/secrets-of-the-gods/"

import random
import time

class Hydra:
    def __init__(self):
        self.head = [0]
        random.seed(time.time())

    def regrow(self):
        result = random.uniform(0, 1)
        if result > 0.5:
            return True

    def cut(self):
        self.head.pop(0)
        if self.regrow():
            self.head.append(0)
            self.head.append(0)
            self.head.append(0)
        if len(self.head)==0:
            return True
        else:
            return False

def battle(max_turn = 200):
    is_win = False
    a_hydra = Hydra()
    turn = 0
    while not is_win:
        is_win = a_hydra.cut()
        turn += 1
        if turn >= max_turn:
            return is_win
    return is_win

if __name__ == "__main__":
    win_count = 0
    for i in range(1000000):
        battle_result = battle()
        if battle_result:
            win_count+=1
    print(win_count)