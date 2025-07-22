

import sys


def add_data_for_name(name_data, year, rank, name):
    if name not in name_data:
        name_data[name] = {year: rank}
    else:  # name in name_data (check the year)
        if year not in name_data[name]:
            name_data[name][year] = rank
        else:  # if exist, keep the better rank
            if int(rank) < int(name_data[name][year]):
                name_data[name][year] = rank


def add_file(name_data, filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        year = lines[0].strip()
        for line in lines[1:]:  # rank, boy, girl
            part = line.split(',')
            rank = part[0].strip()
            boy = part[1].strip()
            girl = part[2].strip()
            add_data_for_name(name_data, year, rank, boy)
            add_data_for_name(name_data, year, rank, girl)


def read_files(filenames):
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)
    return name_data


def search_names(name_data, target):
    names = []
    target_lower = target.lower()  # case insensitive
    for name in name_data:
        if target_lower in name.lower():
            names.append(name)
    return names


def print_names(name_data):
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    args = sys.argv[1:]
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
