def part_one(input):
    invalid_id_sum = 0
    id_ranges = input[0].split(",")
    
    for id_range in id_ranges:
        range_start, range_end = id_range.split("-")
        for id in range(int(range_start), int(range_end) + 1):
            id_str = str(id)

            if len(id_str) % 2 == 0:
                first_half = id_str[:len(id_str)//2]
                second_half = id_str[len(id_str)//2:]
                if first_half == second_half:
                    invalid_id_sum += id

    print(f"Invalid id sum part one: {invalid_id_sum}")


def part_two(input):
    invalid_id_sum = 0
    id_ranges = input[0].split(",")
    
    for id_range in id_ranges:
        range_start, range_end = id_range.split("-")
        for id in range(int(range_start), int(range_end) + 1):
            id_str = str(id)
            series_length = len(id_str)//2
            rest_length = len(id_str) - series_length

            while series_length > 0:
                if rest_length % series_length == 0:
                    series = id_str[:series_length]
                    part_to_check = id_str[series_length:]

                    id_without_series = part_to_check.replace(series, "")

                    if len(id_without_series) == 0:
                        invalid_id_sum += id
                        break

                series_length -= 1
                rest_length += 1

    print(f"Invalid id sum part two: {invalid_id_sum}")
                        

data = open("day02Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
]

part_one(input)
part_two(input)