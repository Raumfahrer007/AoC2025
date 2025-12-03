def part_one(input):
    joltage_sum = 0

    for line in input:
        line = line.replace("\n", "")

        first_digit = max(line[:-1])
        first_digit_index = line.index(first_digit)
        last_digit = max(line[first_digit_index + 1:])

        line_joltage = str(first_digit) + str(last_digit)
        joltage_sum += int(line_joltage)

    print(f"Joltage sum: {joltage_sum}")

def part_two(input):
    joltage_sum = 0

    for line in input:
        line = line.replace("\n", "")
        line = line + "0"    # dummy digit to avoid index errors
        joltage_str = ""

        first_digit = max(line[:-12])
        joltage_str += first_digit
        previous_digit_index = line[:-12].index(first_digit)

        for i in range(11):
            next_digit = max(line[previous_digit_index + 1:-11 + i])
            joltage_str += next_digit
            previous_digit_index = line[previous_digit_index + 1:-11 + i].index(next_digit) + previous_digit_index + 1

        joltage_sum += int(joltage_str)

    print(f"Joltage sum: {joltage_sum}")

data = open("day03Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    "987654321111111\n",
    "811111111111119\n",
    "234234234234278\n",
    "818181911112111\n"
]

part_one(input)
part_two(input)