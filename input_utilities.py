import os
import csv


def read_csv_input(filename):
    with open(filename, 'r') as csvfile:
        test_reader = csv.reader(csvfile, delimiter=',')
        data = []
        for row in test_reader:
            try:
                height = int(row[0])
                length = 0
                if len(row) == 2:
                    length = int(row[1])
                data.append((height, length))
            except ValueError as e:
                print('Can\'t parse, not adding row: {}'.format(row))

        distance = data[-1][0]
        data = data[:-1]

        return data, distance


def get_filename():
    prompt = '> '
    filename = 'test.csv'

    suitable_files = [filename for filename in os.listdir() if filename.endswith('.csv') or filename.endswith('.txt')]

    file_number = None
    valid_input = False
    while not valid_input:
        print('Files in the app dir: ')
        print('------------')
        for index, filename in enumerate(suitable_files):
            print('{}. {}'.format(index, filename))
        print('------------')
        print('Select file by number and press enter. Press q to quit.')
        user_choice = input(prompt)
        print('You\'ve entered: {}'.format(user_choice))

        if user_choice == 'q':
            user_choice = None
            valid_input = True
        else:
            try:
                file_number = int(user_choice)
                valid_input = True
            except ValueError as e:
                print('Wrong input. You\'ve entered {}'.format(user_choice))

    if file_number is None:
        return None
    return suitable_files[file_number]