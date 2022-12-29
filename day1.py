def day1(file):
    calories = []
    calorie = 0

    for line in file:
        line = line.strip("\n")
        if line == "":
            calories.append(calorie)
            calorie = 0
        else:
            calorie += int(line)

    calories = sorted(calories)[::-1]

    return calories[0], sum(calories[:3])


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day1(file))
    file.close()