import random
import math
stat_names = ["STR", "DEX", "INT", "LUK",
              "HP", "MP", "WATK", "MATK", "WDEF", "MDEF",
              "ACCU", "AVOI", "SPEE", "JUMP"]


def level_up(stat, mod, limit):
    top = int(1 + (stat / mod))
    rmax = (top * (top + 1) / 2) + top
    roll = random.randint(0, int(rmax))
    if roll < top:
        return 0
    if limit:
        return 1
    return 1 + math.floor((-1 + math.sqrt((8 * (roll - top)) + 1)) / 2)


def stat_trim(stats, names):
    item_dict = ([], [], [])
    trimmed_stats = []
    index = 0
    for s, n in zip(stats, names):
        if s != 0:
            if index < 4:
                item_dict[0].append(n)
                item_dict[1].append(4)
                trimmed_stats.append(s)
            else:
                item_dict[0].append(n)
                item_dict[1].append(16)
                trimmed_stats.append(s)
            if n != 'SPEE' and n != 'JUMP':
                item_dict[2].append(False)
            else:
                item_dict[2].append(True)
        index += 1
    return item_dict, trimmed_stats


def simulate(starting_level, ending_level, trim_stats, item_dict, iters=100000):
    data_list = []
    for x in range(0, iters):
        item_one = trim_stats
        for n in range(starting_level, ending_level):
            item_plus = []
            while sum(item_plus) == 0:
                item_plus = []
                for i in range(0, len(item_one)):
                    item_plus.append(level_up(item_one[i], item_dict[1][i], item_dict[2][i]))
            item_one = [x + y for x, y in zip(item_one, item_plus)]
        data_list.append(item_one)
    return data_list
