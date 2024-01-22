import csv
import random
import os


def file_path(config):
    if config.default_filename:
        path = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(path, 'random_data.csv')
    else:
        return input("Input full path of file\n")


# 'C:\Python projects\unversity\math statistics\lab1\random_data.csv'
def read_data(config):
    while True:
        try:
            path = file_path(config)

            with open(path, 'r', newline='') as infile:
                reader = csv.reader(infile, delimiter='\n')
                l = list(reader)

                return list(map(lambda x: round(float(x[0]), config.random_config.scale), l))
        except:
            print("Wrong path")


def generate_random_data(config):
    random_config = config.random_config
    rand_values = []
    for i in range(random_config.count):
        rand_values.append(round(random.uniform(random_config.min, random_config.max), random_config.scale))

    with open('random_data.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile, delimiter='\n')
        writer.writerow(rand_values)
        outfile.close()

    return rand_values


def get_data(config):
    if (config.random):
        print('Generate random data mode')
        return generate_random_data(config)
    else:
        print('Read value from file')
        return read_data(config)
