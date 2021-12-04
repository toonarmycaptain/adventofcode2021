from day3_input import input

test_input = ['00100',
              '11110',
              '10110',
              '10111',
              '10101',
              '01111',
              '00111',
              '11100',
              '10000',
              '11001',
              '00010',
              '01010',
              ]


def get_gamma_epsilon(data: list = input):
    gamma_str = ''
    for place in range(len(data[0])):
        zeros = 0
        ones = 0
        for number in data:
            if number[place] == '0':
                zeros += 1
            elif number[place] == '1':
                ones += 1
            else:
                print("Error")

        if zeros > ones:
            gamma_str += '0'
        elif ones > zeros:
            gamma_str += '1'
        else:
            print('zeros == ones')

    gamma_num = int(gamma_str, 2)

    epsilon_str = gamma_str.translate(str.maketrans("01", "10"))
    epsilon_num = int(epsilon_str, 2)

    print(f'{gamma_str=}, {gamma_num=}, {epsilon_str=}, {epsilon_num=}, product={gamma_num * epsilon_num}')


# print(get_gamma(test_input))
get_gamma_epsilon(input)


def get_oxygen_co2_scrubber(data: list = input):
    orig_data = data[:]
    for place in range(len(data[0])):
        zeros = 0
        ones = 0
        for number in data:
            if number[place] == '0':
                zeros += 1
            elif number[place] == '1':
                ones += 1
            else:
                print("Error")
        removal_list = data[:]
        if zeros > ones:
            for number in data:
                if number[place] == '1':
                    removal_list.remove(number)
        elif ones >= zeros:
            for number in data:
                if number[place] == '0':
                    removal_list.remove(number)
        else:
            print('Error')
        data = removal_list
        if len(data) == 1:
            break
    if len(data) != 1:
        print('Error: more than value remaining)')
    oxygen_number = int(data[0], 2)


    data = orig_data[:]
    for place in range(len(data[0])):
        zeros = 0
        ones = 0
        for number in data:
            if number[place] == '0':
                zeros += 1
            elif number[place] == '1':
                ones += 1
            else:
                print("Error")
        removal_list = data[:]
        if zeros <= ones:
            for number in data:
                if number[place] == '1':
                    removal_list.remove(number)
        elif ones < zeros:
            for number in data:
                if number[place] == '0':
                    removal_list.remove(number)
        else:
            print('Error')
        data = removal_list
        if len(data) == 1:
            break
    if len(data) != 1:
        print('Error: more than value remaining)')

    co2_number = int(data[0], 2)
    print(f'{oxygen_number=}, {co2_number=}, product={oxygen_number*co2_number}')


# get_oxygen_co2_scrubber(test_input)
get_oxygen_co2_scrubber()