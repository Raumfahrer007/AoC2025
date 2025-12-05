def get_valid_ids(input):
    """
    {
        length:
            [
                [start, end], ...
            ]
    }
    """
    id_ranges = []
    for line in input:
        line = line.replace("\n", "")
        range_start, range_end = line.split("-")

        id_ranges.append([int(range_start), int(range_end)])

    id_ranges.sort()
    i = 0
    while i < len(id_ranges):

        while i > 0 and id_ranges[i][0] <= id_ranges[i - 1][1]:
            id_ranges[i][0] = id_ranges[i - 1][0]
            del id_ranges[i - 1]
            i += 1

        while i + 1 < len(id_ranges) and id_ranges[i][1] >= id_ranges[i + 1][0]:
            if id_ranges[i][1] < id_ranges[i + 1][1]:
                id_ranges[i][1] = id_ranges[i + 1][1]

            del id_ranges[i + 1]

        i += 1


    return id_ranges


def part_one(input):
    valid_ids_end = input.index("\n")
    valid_ids = get_valid_ids(input[:valid_ids_end])

    valid_id_counter = 0

    for id in input[valid_ids_end + 1:]:
        id = id.replace("\n", "")
        for ranges in valid_ids:
            if int(id) >= ranges[0] and int(id) <= ranges[1]:
                valid_id_counter += 1
                break

    print(f"Valid id counter: {valid_id_counter}")



def part_two(input):
    valid_ids_end = input.index("\n")
    valid_ids = get_valid_ids(input[:valid_ids_end])

    valid_id_counter = 0

    for range in valid_ids:
        valid_id_counter += range[1] - range[0] + 1

    print(f"Total valid ids: {valid_id_counter}")


data = open("day05Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    "3-5\n",
    "10-14\n",
    "16-20\n",
    "12-18\n",
    "\n",
    "1\n",
    "5\n",
    "8\n",
    "11\n",
    "17\n",
    "32\n"
]

part_one(input)
part_two(input)