def day6(file):
    for line in file:
        line = line.strip("\n")

        # part 1
        # for character in range(len(line) - 3):
        #     marker = set(line[character: character + 4])
        #     if len(marker) == 4:
        #         return character + 4

        # part 2
        for character in range(len(line) - 13):
            marker = set(line[character: character + 14])
            if len(marker) == 14:
                return character + 14
    return None


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day6(file))
    file.close()
