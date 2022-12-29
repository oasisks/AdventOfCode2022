def day3(file):
    lowercase_scores = {chr(96 + i): i for i in range(1, 27)}
    uppercase_scores = {chr(64 + i): i + 26 for i in range(1, 27)}

    scores = dict(lowercase_scores, **uppercase_scores)
    lines = file.readlines()

    # this is part 1
    similar_items_part1 = []
    for line in lines:
        line = line.strip("\n")
        mid = int(len(line) / 2)
        first, second = set(line[:mid]), set(line[mid:])
        similar_items_part1.append((first & second).pop())

    # this is part 2
    similar_items_part2 = []
    for index in range(2, len(lines) + 1, 3):
        first, second, third = [set(line.strip("\n")) for line in lines[index - 2: index + 1]]
        badge = first & second & third
        similar_items_part2.append(badge.pop())

    def calculate_score(items):
        return sum([scores[item] for item in items])

    return calculate_score(similar_items_part1), calculate_score(similar_items_part2)


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day3(file))
    file.close()
