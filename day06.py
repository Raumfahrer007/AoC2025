def part_one(input):
    problems = []

    for i, line in enumerate(input):
        for j, problem_part in enumerate(line.replace("\n", "").split()):
            if i == 0:
                problems.append([])

            problems[j].append(problem_part)

    solution_sum = 0
    for problem in problems:
        operation = problem[-1]
        solution = int(problem[0])
        for problem_part in problem[1:-1]:
            if operation == "+":
                solution += int(problem_part)
            else:
                solution *= int(problem_part)

        solution_sum += solution

    print(f"Solution sum part one: {solution_sum}")

def part_two(input):
    input = [line.replace("\n", "") for line in input]
    problem_borders = [-1] # -1 to include the first problem

    for i, char in enumerate(input[0]):
        if char == " ":
            problem_border = True
            for j in range(len(input) - 1):
                if input[j + 1][i] != " ":
                    problem_border = False
                    break
            if problem_border:
                problem_borders.append(i)

    problem_borders.append(len(input[0]))

    solution_sum = 0
    for i in range(len(problem_borders) - 1):
        problem_start = problem_borders[i] + 1
        problem_end = problem_borders[i + 1]
        operation = input[-1][problem_start]

        problem_part = ""
        for k in range(len(input) - 1):
            problem_part += input[k][problem_start]

        solution = int(problem_part)

        for j in range(problem_start + 1, problem_end):
            problem_part = ""
            for k in range(len(input) - 1):
                problem_part += input[k][j]

            if operation == "+":
                solution += int(problem_part)
            else:
                solution *= int(problem_part)

        solution_sum += solution
            
    print(f"Solution sum part two: {solution_sum}")

data = open("day06Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    "123 328  51 64 \n",
    " 45 64  387 23 \n",
    "  6 98  215 314\n",
    "*   +   *   +  \n"
]

part_one(input)
part_two(input)