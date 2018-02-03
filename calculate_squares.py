#! /usr/bin/env python3
from input_utilities import get_filename, read_csv_input
from geometry import calc_square

if __name__ == '__main__':
    quit = False

    while not quit:
        filename = get_filename()
        if filename is None:
            print('You\'re quitting. Bye!')
        else:
            print('------------')
            print('Parsing file: {}...'.format(filename))
            initial_data, distance = read_csv_input(filename);
            print('------------')
            print('Working data:')
            print(initial_data, distance)
            print('------------')
            print('Calculating square...')
            square = calc_square(initial_data, distance)
            print('The square is: {}'.format(round(square, 10)))
            print('------------')

        valid_input = False
        while not valid_input:
            answer = input('Would you like another time?(y/n): ')
            if answer in ['n', 'N']:
                valid_input = True
                quit = True
            elif answer in ['y', 'Y']:
                valid_input = True

    print('Bye!')
