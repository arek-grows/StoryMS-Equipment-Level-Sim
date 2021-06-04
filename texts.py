def stat_texts(file):
    file.write('STR = 0\n')
    file.write('DEX = 0\n')
    file.write('INT = 0\n')
    file.write('LUK = 0\n')
    file.write('HP = 0\n')
    file.write('MP = 0\n')
    file.write('WEAPON ATTACK = 0\n')
    file.write('MAGIC ATTACK = 0\n')
    file.write('WEAPON DEFENSE = 0\n')
    file.write('MAGIC DEFENSE = 0\n')
    file.write('ACCURACY = 0\n')
    file.write('AVOIDABILITY = 0\n')
    file.write('SPEED = 0\n')
    file.write('JUMP = 0\n')
    return


def create_base_text():
    with open('base_equipment.txt', 'w') as file:
        file.write('Equipment Name = ""\n')
        file.write('Starting Level = 1\n')
        file.write('Ending Level = 7\n')
        stat_texts(file)
    return


def create_levelled_text():
    with open('levelled_equipment.txt', 'w') as file:
        stat_texts(file)
        file.close()