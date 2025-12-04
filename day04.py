OPERATIONS = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def add_padding(input):
    new_input = []
    for line in input:
        new_input.append("." + line.replace("\n", "") + ".")

    new_input.insert(0, "." * len(new_input[0]))
    new_input.append("." * len(new_input[0]))
    return new_input

def part_one(input):
    modified_input = add_padding(input)

    accessible_paper_count = 0
    for i in range(1, len(modified_input) - 1):
        for j, cell in enumerate(modified_input[i]):
            if cell == "@":
                adjacent_paper_count = 0
                for operation in OPERATIONS:
                    if modified_input[i + operation[0]][j + operation[1]] == "@":
                        adjacent_paper_count += 1
                if adjacent_paper_count < 4:
                    accessible_paper_count += 1
    print(f"Accessible paper count: {accessible_paper_count}")


def part_two(input):
    removed_paper_count = 0
    removed_paper = True
    modified_input = add_padding(input)

    while removed_paper:
        removed_paper = False
        for i in range(1, len(modified_input) - 1):
            for j, cell in enumerate(modified_input[i]):
                if cell == "@":
                    adjacent_paper_count = 0
                    for operation in OPERATIONS:
                        if modified_input[i + operation[0]][j + operation[1]] == "@":
                            adjacent_paper_count += 1
                    if adjacent_paper_count < 4:
                        new_line = modified_input[i][:j] + "." + modified_input[i][j+1:]
                        modified_input[i] = new_line
                        removed_paper = True
                        removed_paper_count += 1
    print(f"Removed paper count: {removed_paper_count}")


data = open("day04Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    "..@@.@@@@.\n",
    "@@@.@.@.@@\n",
    "@@@@@.@.@@\n",
    "@.@@@@..@.\n",
    "@@.@@@@.@@\n",
    ".@@@@@@@.@\n",
    ".@.@.@.@@@\n",
    "@.@@@.@@@@\n",
    ".@@@@@@@@.\n",
    "@.@.@@@.@.\n"
]

part_one(input)
part_two(input)