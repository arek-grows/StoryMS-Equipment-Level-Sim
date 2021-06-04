# this project is a mess, my 2nd ever python project, after game of life :)

import texts
import levelsim
import pickle
import os
import analyzation


# TODO: error testing (file doesnt exit, invalid characters)
def create_option(base):
    with open(base, 'r') as base_file:
        file_lines = base_file.readlines()
        # equipment name put into a string
        equip_name = file_lines[0]
        equip_name = (equip_name[(equip_name.find('"')):]).rstrip('\n').strip('"')
        # starting level/ending level and stats
        s_level = int((file_lines[1][(file_lines[1].find('=')) + 1:]).rstrip('\n').strip())
        e_level = int((file_lines[2][(file_lines[2].find('=')) + 1:]).rstrip('\n').strip())
        item_stats = []
        for x in range(3, 17):
            number = int((file_lines[x][(file_lines[x].find('=')) + 1:]).rstrip('\n').strip())
            item_stats.append(number)
        if sum(item_stats) == 0:
            return print('simulation failed: all stats in "base_equipment.txt" are 0')

    print('simulating "' + equip_name + '" lvl ' + str(s_level) + '-' + str(e_level) + '...')
    passers = levelsim.stat_trim(item_stats, levelsim.stat_names)
    sims = levelsim.simulate(s_level, e_level, passers[1], passers[0])

    with open("data/counter", 'r') as counter_file:
        current_count = counter_file.readline()

    # TODO: add zero to the beginning of current_count if the length increases
    file_name = '(' + current_count + ') ' + equip_name + ' lvl ' + str(s_level) + '-' + str(e_level)
    # file number, stat names, og base stats, level sims
    file_list = [0, 0, 0, 0]
    file_list[0] = current_count
    file_list[1] = passers[0][0]
    file_list[2] = passers[1]
    file_list[3] = sims
    with open('data/simulations/' + file_name, 'wb') as new_sim:
        pickle.dump(file_list, new_sim)

    with open("data/counter", 'w') as counter_file:
        counter_file.write(str(int(current_count) + 1))

    print('100,000 simulations of equipment named "' + file_name + '" created.')
    # TODO: "reset file?"
    #  texts.create_base_text()
    if input('Would you like to analyze the item now? (y/n) ').lower() == 'y':
        print()
        return menu('analyze', file_name)
    return print(), menu('main')


def analyze_option(letter, equip_sim, sims):
    # TODO: plot, percentile
    # TODO: percentile menu
    if letter == 'p':
        analyzation.percentile(equip_sim, sims)
        return print(), menu('analyze', equip_sim, sims)
    elif letter == 'd':
        print('plot')
        return print(''), reanalyze(equip_sim, sims)
    elif letter == 'c':
        return print(), menu('analyze')
    elif letter == 'x':
        exit()
    elif letter == 'b':
        return print(''), menu('main')
    else:
        return print('Invalid option.\n'), reanalyze(equip_sim, sims)


def reanalyze(equip_sim, stat_list):
    return analyze_option(input('What would you like to do? ').lower(), equip_sim, stat_list)


def first_option(letter):
    print()
    if letter == 'c':
        create_option('base_equipment.txt')
    elif letter == 'a':
        return print(''), menu('analyze')
    elif letter == 'r':
        texts.create_base_text()
        texts.create_levelled_text()
        return print('base_equipment.txt and levelled_equipment.txt have been reset.\n'), menu('main')
    elif letter == 'x':
        exit()
    else:
        return print('Invalid option.\n'), menu('main')


def choose_sim(files):
    file_names = []
    file_numbers = []
    for f in files:
        print(f)
        file_names.append(str(f))
        with open('data/simulations/' + f, 'rb') as yup:
            y = pickle.load(yup)
            # [1] and [2] names and stats
            file_numbers.append(y[0])
            # print('  ', end='')
            for i in range(0, len(y[1])):
                bs = ' '
                if i == len(y[1]) - 1:
                    bs = '\n'
                print(y[1][i] + ':' + str(y[2][i]), end=bs)
            print('----')
    print()
    exists = False
    sim_nr = 0
    while not exists:
        print('Which item sim would you like to analyze?')
        sim_nr = input('Enter the corresponding number.')
        if sim_nr in file_numbers:
            exists = True
        else:
            print("error: that item sim doesn't exist.")
    print()
    # returns the name of the file the user has chosen
    return file_names[file_numbers.index(sim_nr)]


def menu(current, sim_file='null', sims='null'):
    if current == 'main':
        print('[c]reate a new equipment sim from "base_equipment.txt"')
        print('[a]nalyze existing equipment sim')
        print('[r]eset "base_equipment.txt" and "levelled_equipment.txt" to original')
        print('e[x]it program')
        return first_option(input('What would you like to do? ').lower())

    if current == 'analyze':
        files = os.listdir('data/simulations')
        if sim_file == 'null':
            sim_file = choose_sim(files)
        if sims == 'null':
            sims = analyzation.mode(sim_file)
            print()
        print("find out what [p]ercentile your equipment's stats fall in")
        print('plot the [d]istribution of a specific stat')
        print('[c]hoose a different item')
        print('[b]ack to main menu')
        print('e[x]it program')
        return analyze_option(input('What would you like to do? ').lower(), sim_file, sims)
    return print('menu error')


menu('main')
