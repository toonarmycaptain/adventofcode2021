from day2_input import input


def position():
    depth = 0
    horiz = 0

    for command in input:
        split = command.split()
        if split[0] == 'forward':
            horiz += int(split[1])
        if split[0] == 'up':
            depth -= int(split[1])
        if split[0] == 'down':
            depth += int(split[1])
    return f'{horiz=}, {depth=}, product={(depth*horiz)=}'


print(position())


def get_aim():
    depth = 0
    horiz = 0
    aim = 0

    for command in input:
        split = command.split()
        if split[0] == 'forward':
            horiz += int(split[1])
            depth += aim * int(split[1])
        if split[0] == 'up':
            aim -= int(split[1])
        if split[0] == 'down':
            aim += int(split[1])
    return f'{horiz=}, {depth=}, {aim=}, product={(depth*horiz)=}'


print(get_aim())
