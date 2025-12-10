import numpy as np

def part_one(input):
    beam_positions = set()
    beam_positions.add(input[0].index("S"))

    split_count = 0
    for i in range(1, len(input)):
        if "^" not in input[i]:
            continue

        new_beam_positions = beam_positions.copy()
        for position in beam_positions:
            if input[i][position] == "^":
                split_count += 1
                new_beam_positions.remove(position)
                new_beam_positions.add(position - 1)
                new_beam_positions.add(position + 1)

        beam_positions = new_beam_positions

    print(f"Split count: {split_count}")


def part_two(input):
    beam_positions = np.zeros(len(input[0]))
    beam_positions[input[0].index("S")] += 1

    for i in range(1, len(input)):
        if "^" not in input[i]:
            continue

        new_beam_positions = beam_positions.copy()
        for position, count in enumerate(beam_positions):
            if input[i][position] == "^":
                new_beam_positions[position] = 0
                new_beam_positions[position - 1] += count
                new_beam_positions[position + 1] += count

        beam_positions = new_beam_positions
    

    print(f"Possible worlds: {sum(beam_positions)}")

data = open("day07Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    ".......S.......\n",
    "...............\n",
    ".......^.......\n",
    "...............\n",
    "......^.^......\n",
    "...............\n",
    ".....^.^.^.....\n",
    "...............\n",
    "....^.^...^....\n",
    "...............\n",
    "...^.^...^.^...\n",
    "...............\n",
    "..^...^.....^..\n",
    "...............\n",
    ".^.^.^.^.^...^.\n",
    "...............\n"
]

part_one(input)
part_two(input)