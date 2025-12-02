def count_zeros(starting_position, instructions):
    zero_pass = 0
    zero_stop = 0
    current_position = starting_position

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])

        if steps == 0:
            continue

        zero_pass += steps // 100
        steps = steps % 100

        if direction == "L":
            previous_position = current_position
            current_position = current_position - steps
            if current_position < 0:
                current_position = 100 + current_position
                if not previous_position == 0:  # previous position = 0 -> no zero pass despite current position < 0
                    zero_pass += 1

        else:
            current_position = current_position + steps
            if current_position > 99:
                current_position = current_position - 100
                if not current_position == 0:  # current position = 0 -> will be tracked by zero_stop
                    zero_pass += 1

        if current_position == 0:
            zero_stop += 1

    return zero_pass, zero_stop

def part_one(input):
    _, zero_stop = count_zeros(50, input)
        
    print(f"Standing on zero: {zero_stop} times")


def part_two(input):
    zero_pass, zero_stop = count_zeros(50, input)
        
    print(f"Passing zero: {zero_pass + zero_stop} times")


data = open("day01Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82"
]

part_one(input)
part_two(input)