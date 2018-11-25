__author__ = "Thai Thien"
__link__ = "https://app.codesignal.com/challenge/D7xcKDseTa2gLondg"


class Fighter:
    def __init__(self, hp, atk, res):
        self.hp = hp
        self.atk = atk
        self.res = res

    def hit(self, target):
        """
        hit the target
        :param target:
        :return:
        """
        dmg = self.atk - target.res
        if dmg < 0:
            dmg = 0
        target.hp -= dmg
        return dmg

    def is_alive(self):
        if self.hp > 0:
            return True


def make_fighter(code):
    """

    :param code: a b g
    :return:
    """
    if code == "a":
        return Fighter(5, 6, 2)
    elif code == "b":
        return Fighter(6, 8, 2)
    elif code == "g":
        return Fighter(8, 6, 5)


def format_avg_dmg(values):
    newer_method_string = "{:.2f}".format(values)
    return newer_method_string


class Profiler:
    def __init__(self):
        self.winner = ""
        self.fightersDefeated = 0
        self.fightersRemain = 0
        self.masterHealth = 0
        self.hitsByFighters = 0
        self.hitsByMaster = 0
        self.avgDamageDealtByFighters = 0
        self.avgDamageDealtByMaster = 0
        self.figterDmg = 0
        self.masterDmg = 0

    def to_return_arr(self):
        self.avgDamageDealtByFighters = format_avg_dmg(self.avgDamageDealtByFighters)
        self.avgDamageDealtByMaster = format_avg_dmg(self.avgDamageDealtByMaster)
        # if self.avgDamageDealtByFighters[-1] == '0':
        #     self.avgDamageDealtByFighters = self.avgDamageDealtByFighters[:-1]
        # if self.avgDamageDealtByMaster[-1] == '0':
        #     self.avgDamageDealtByMaster = self.avgDamageDealtByMaster[:-1]

        ret_list = []
        ret_list.append(str(self.winner))
        ret_list.append(str(self.fightersDefeated))
        ret_list.append(str(self.fightersRemain))
        ret_list.append(str(self.masterHealth))
        ret_list.append(str(self.hitsByFighters))
        ret_list.append(str(self.hitsByMaster))
        ret_list.append(str(self.avgDamageDealtByFighters))
        ret_list.append(str(self.avgDamageDealtByMaster))
        return ret_list


def duel(master, fighter, profiler):
    """
    master and another fighter is hitting each other
    :param master: a Fighter
    :param fighter: a Fighter
    :param profiler: stat
    :return: True if master win
    """
    while master.is_alive() and fighter.is_alive():
        if fighter.is_alive():
            fighter_dmg = fighter.hit(master)
            profiler.figterDmg += fighter_dmg
            profiler.hitsByFighters += 1

        if master.is_alive():
            master_dmg = master.hit(fighter)
            profiler.masterDmg += master_dmg
            profiler.hitsByMaster +=1
    if master.is_alive():
        return True
    else:
        return False


def the_epic_fight(master, list_of_fighter, profiler):
    """
    single master, duel 1-on-1 with each fighter
    :param master: a Fighter
    :param list_of_fighter: a Fighter
    :param profiler: stat
    :return: number of fighter remained
    """
    remained = 0

    for fighter in list_of_fighter:
        if not master.is_alive():
            remained += 1
            continue
        result = duel(master, fighter, profiler)
        if not result:
            remained += 1
        else:
            profiler.fightersDefeated += 1
    return remained


def round_avg(value):
    answer = round(value, 2)
    return answer


def masterVsFighters(fighters, master):
    list_of_fighter = []
    for fighter_code in fighters:
        fighter = make_fighter(fighter_code)
        list_of_fighter.append(fighter)
    master_fighter = Fighter(master[0], master[1], master[2])
    profiler = Profiler()
    remained = the_epic_fight(master_fighter, list_of_fighter, profiler)
    profiler.fightersRemain = remained

    if master_fighter.is_alive():
        profiler.masterHealth = master_fighter.hp
        profiler.winner = "Master"
    else:
        profiler.masterHealth = 0
        profiler.winner = "Fighters"

    if profiler.hitsByMaster != 0:
        profiler.avgDamageDealtByMaster = round_avg(profiler.masterDmg/profiler.hitsByMaster)
    else:
        profiler.avgDamageDealtByMaster = 0

    if profiler.hitsByFighters != 0:
        profiler.avgDamageDealtByFighters = round_avg(profiler.figterDmg/profiler.hitsByFighters)
    else:
        profiler.avgDamageDealtByFighters = 0

    return profiler.to_return_arr()

if __name__ == "__main__":
    fighters = ["a", "a", "b"]
    master = [14, 6, 4]
    result = masterVsFighters(fighters, master)
    print(result)