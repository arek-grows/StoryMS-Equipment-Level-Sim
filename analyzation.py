import pickle
stat_names = ["STR", "DEX", "INT", "LUK",
              "HP", "MP", "WATK", "MATK", "WDEF", "MDEF",
              "ACCU", "AVOI", "SPEE", "JUMP"]


def mode(equip_sim):
    # TODO: print into a text file
    # TODO: find 50th percentile rather than the mode?
    with open('data/simulations/' + equip_sim, 'rb+') as gurgle:
        sims = pickle.load(gurgle)
        simulations = sims[3]
        rev_list = [[] for _ in range(len(sims[2]))]
        for i, new in zip(range(0, len(sims[2])), rev_list):
            for x in simulations:
                new.append(x[i])
        # print('Most common stats for ' + equip_sim + ' simulation:')
        # for stats, name in zip(rev_list, sims[1]):
        #     print('(' + name + ': ' + str(max(set(stats), key=stats.count)) + ')', end=' ')
        # print()
        # # average
        # print('Averages for ' + equip_sim + ' simulation:')
        # for stats, name in zip(rev_list, sims[1]):
        #     print('(' + name + ': ' + str(sum(stats) / 100000) + ')', end=' ')
        # print()
        for stat_list in rev_list:
            stat_list.sort()
        # 50th percentile
        print('50th percentiles for ' + equip_sim + ' simulation:')
        for stats, name in zip(rev_list, sims[1]):
            print('(' + name + ': ' + str(stats[49999]) + ')', end=' ')
        print()
        sims[3] = rev_list
    # translates to stat_list
    # file number 0, stat names 1, og base stats 2, revised and sorted list 3
    return sims


def percentile(equip_sim, sims):
    # TODO: error: file doesnt exist, levelled text stats don't match stat_list stats
    # TODO: clean up
    sim_stats = sims[3]
    percentile_list = []
    with open('levelled_equipment.txt', 'r') as l_equip:
        levelled_lines = l_equip.readlines()
        levelled_item_stats = []
        for x in range(0, len(levelled_lines)):
            number = int((levelled_lines[x][(levelled_lines[x].find('=')) + 1:]).rstrip('\n').strip())
            if number != 0:
                levelled_item_stats.append(number)
    for stat, i in zip(levelled_item_stats, range(0, len(sim_stats))):
        n = (sim_stats[i].index(stat) + (len(sim_stats[i]) - sim_stats[i][::-1].index(stat) - 1)) / 2
        N = len(sim_stats[i])
        percentile_list.append((n/N)*100)
    return print(percentile_list)
