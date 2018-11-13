__author__ = "Thai Thien"

"""
https://app.codesignal.com/challenge/4LxoTpx7zdCSrWQdg
"""
"""
[" **  **   **  **   **  ** ", 
 "******** ******** ********", 
 "******** ******** ********", 
 " ******   ******   ****** ", 
 "  ****     ****     ****  ", 
 "   **       **       **   "]
"""

"""
 **  ** 
********
********
 ****** 
  ****   
   **   
"""

fullHearth = []  # 4 value
fullHearth.append(" **  ** ")
fullHearth.append("********")
fullHearth.append("********")
fullHearth.append(" ****** ")
fullHearth.append("  ****  ")
fullHearth.append("   **   ")

d3Health = []  # 3
d3Health.append(" **     ")
d3Health.append("****    ")
d3Health.append("****    ")
d3Health.append(" ****** ")
d3Health.append("  ****  ")
d3Health.append("   **   ")

d2Health = []  # 2
d2Health.append(" **     ")
d2Health.append("****    ")
d2Health.append("****    ")
d2Health.append(" ***    ")
d2Health.append("  **    ")
d2Health.append("   *    ")

d1Health = []  # 1
d1Health.append(" **     ")
d1Health.append("****    ")
d1Health.append("****    ")
d1Health.append("        ")
d1Health.append("        ")
d1Health.append("        ")

d0Health = []  # 0
d0Health.append("        ")
d0Health.append("        ")
d0Health.append("        ")
d0Health.append("        ")
d0Health.append("        ")
d0Health.append("        ")

# we have 12 part in health bar


def calculate_health(hp, max_hp):
    """
    calculate how many hp part left
    :param hp:
    :param max_hp:
    :return: part left / 12 total part
    """
    part_value = max_hp / 12
    current_part = int(hp / part_value)
    spare_hp = hp - current_part*part_value
    part = current_part
    if spare_hp > 0:
        part += 1
    return part


def render_health(part):
    """
    render the ascii health bar
    :param part:
    :return:
    """
    total = []
    for i in range(3):
        if part >= 4:
            total.append(fullHearth)
            part -= 4
        elif part == 3:
            total.append(d3Health)
            part -= 3
        elif part == 2:
            total.append(d2Health)
            part -= 2
        elif part == 1:
            total.append(d1Health)
            part -= 1
        elif part == 0:
            total.append(d0Health)
    result = ["", "", "", "", "", ""]
    result[0] = " ".join([total[0][0], total[1][0], total[2][0]])
    result[1] = " ".join([total[0][1], total[1][1], total[2][1]])
    result[2] = " ".join([total[0][2], total[1][2], total[2][2]])
    result[3] = " ".join([total[0][3], total[1][3], total[2][3]])
    result[4] = " ".join([total[0][4], total[1][4], total[2][4]])
    result[5] = " ".join([total[0][5], total[1][5], total[2][5]])

    return result


def healthDisplay(health, maxHealth):
    """
    main function to solve (must have)
    :param health:
    :param maxHealth:
    :return:
    """
    part = calculate_health(health, maxHealth)
    result = render_health(part)
    return result


def display_health(render_result):
    """
    print line by line
    for debug
    not require
    :param render_result:
    :return:
    """
    for line in render_result:
        print(line)


if __name__ == "__main__":
    display_health(healthDisplay(100, 100))
    print("--------------------------------")
    display_health(healthDisplay(8, 561))
    print("--------------------------------")
    display_health(healthDisplay(195, 259))

