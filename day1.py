from day1_input import input


def increasing_depths():
    increases = 0
    for index in range(0, len(input) - 1):
        if input[index + 1] > input[index]:
            increases += 1
        # print(index, index + 1, input[index], input[index + 1], increases)
    print(f'number of increases: {increases}')


increasing_depths()


def increasing_depth_sums():
    increases = 0
    for index in range(0, len(input) - 3):
        if (input[index + 1] + input[index + 2] + input[index + 3]) > (
                input[index] + input[index + 1] + input[index + 2]):
            increases += 1
        # print(index, index + 1, input[index], input[index + 1], increases)
    print(f'number of depth sum increases: {increases}')


increasing_depth_sums()
