from day6_input import input

test_input = [3, 4, 3, 1, 2]


def day6(fishes, day_end):
    fish_timer_counts = [fishes.count(i) for i in range(9)]
    for days in range(day_end):
        # print(f'{fish_timer_counts=}')
        num_reproducing_fish = fish_timer_counts[0]
        fish_timer_counts[0:8] = fish_timer_counts[1:9]
        fish_timer_counts[6] += num_reproducing_fish
        fish_timer_counts[8] = num_reproducing_fish
    return sum(fish_timer_counts)


# print(day6(test_input, 18))
# print(day6(test_input, 80))
# print(day6(test_input, 256))
print(day6(input, 80))
print(day6(input,256))
