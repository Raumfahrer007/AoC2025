import math

def calculate_distance(fuse1, fuse2):
    distance = math.sqrt(sum((x - y) ** 2 for x, y in zip(fuse1, fuse2)))

    return distance

def get_fuse_distances(input):
    fuses = []
    distances = {}
    """
    {
        fuse:
            other_fuse: distance
    }
    """
    for line in input:
        coordinates = list(map(int, line.replace("\n", "").split(",")))
        fuses.append(coordinates)

    for fuse in fuses:
        distances[tuple(fuse)] = {}
        other_fuses = fuses.copy()
        other_fuses.remove(fuse)

        for other_fuse in other_fuses:
            distances[tuple(fuse)][tuple(other_fuse)] = calculate_distance(fuse, other_fuse)

    distances = {
        key: dict(sorted(subdict.items(), key=lambda item: item[1]))
        for key, subdict in distances.items()
    }

    return distances

def add_next_fuses_to_circuit(distances, circuits):
    shortest_distance = math.inf
    closest_pair = []

    for fuse in distances.keys():
        closest_fuse = next(iter(distances[fuse].items()))

        if closest_fuse[1] < shortest_distance:
            shortest_distance = closest_fuse[1]
            closest_pair = [fuse, closest_fuse[0]]

    circuit_indices = [-1, -1]
    for i, circuit in enumerate(circuits):
        if closest_pair[0] in circuit:
            circuit_indices[0] = i
            continue

        if closest_pair[1] in circuit:
            circuit_indices[1] = i
            continue

    if circuit_indices[0] != -1 and circuit_indices[1] != -1:
        circuits[circuit_indices[0]].update(circuits[circuit_indices[1]])
        del circuits[circuit_indices[1]]

    elif circuit_indices[0] != -1:
        circuits[circuit_indices[0]].add(closest_pair[1])

    elif circuit_indices[1] != -1:
        circuits[circuit_indices[1]].add(closest_pair[0])

    else:
        circuits.append({closest_pair[0], closest_pair[1]})

    del distances[tuple(closest_pair[0])][closest_pair[1]]
    if not distances[tuple(closest_pair[0])]:
        del distances[tuple(closest_pair[0])]
    del distances[tuple(closest_pair[1])][closest_pair[0]]
    if not distances[tuple(closest_pair[1])]:
        del distances[tuple(closest_pair[1])]

    return closest_pair


def solve(input):
    distances = get_fuse_distances(input)

    circuits = []
    """PART ONE"""
    for _ in range(1000):
        add_next_fuses_to_circuit(distances, circuits)
        
    sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    result = 1
    for i in range(3):
        result *= len(sorted_circuits[i])

    print(f"Three largest circuits product: {result}")

    """PART TWO"""
    connecting = True
    while connecting:
        last_fuses = add_next_fuses_to_circuit(distances, circuits)

        if len(circuits) == 1 and len(circuits[0]) == len(input):
            connecting = False

    result_two = last_fuses[0][0] * last_fuses[1][0]	
    print(f"Last two fuses product: {result_two}")


data = open("day08Input.txt", "r")
input = data.readlines()
data.close()

test_input = [
    "162,817,812\n",
    "57,618,57\n",
    "906,360,560\n",
    "592,479,940\n",
    "352,342,300\n",
    "466,668,158\n",
    "542,29,236\n",
    "431,825,988\n",
    "739,650,466\n",
    "52,470,668\n",
    "216,146,977\n",
    "819,987,18\n",
    "117,168,530\n",
    "805,96,715\n",
    "346,949,466\n",
    "970,615,88\n",
    "941,993,340\n",
    "862,61,35\n",
    "984,92,344\n",
    "425,690,689\n"
]

solve(input)