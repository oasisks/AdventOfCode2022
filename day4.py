def day4(file):
    part1 = 0
    part2 = 0
    for line in file:
        line = line.strip("\n")
        first, second = [[int(num) for num in elf.split("-")] for elf in line.split(",")]

        first = set(range(first[0], first[1] + 1))
        second = set(range(second[0], second[1] + 1))

        if first.issubset(second) or second.issubset(first):
            part1 += 1

        if first & second:
            part2 += 1

    return part1, part2


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day4(file))
    file.close()
