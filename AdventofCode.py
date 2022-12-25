import re


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


def day2(file):

    def determine_winner_part1(outcomes):
        """
        Determines the winner given the outcomes. Returns the score you will receive depending on the winner
        :param outcomes: list
        :return: int
        """
        scores = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
        score_outcomes = {"lost": 0, "draw": 3, "won": 6}
        opponent, self = outcomes

        # opponent chooses rock
        if opponent == "A":
            if self == "X":
                return scores["X"] + score_outcomes["draw"]
            elif self == "Y":
                return scores["Y"] + score_outcomes["won"]
            else:
                return scores["Z"] + score_outcomes["lost"]
        # opponent chooses paper
        elif opponent == "B":
            if self == "X":
                return scores["X"] + score_outcomes["lost"]
            elif self == "Y":
                return scores["Y"] + score_outcomes["draw"]
            else:
                return scores["Z"] + score_outcomes["won"]
        # opponent chooses scissors
        else:
            if self == "X":
                return scores["X"] + score_outcomes["won"]
            elif self == "Y":
                return scores["Y"] + score_outcomes["lost"]
            else:
                return scores["Z"] + score_outcomes["draw"]

    def determine_winner_part2(outcomes):
        scores = {"A": 1, "B": 2, "C": 3}
        score_outcomes = {"lost": 0, "draw": 3, "won": 6}
        opponent, self = outcomes

        # opponent chooses rock
        if opponent == "A":
            # end on a loss
            if self == "X":
                return scores["C"] + score_outcomes["lost"]
            # end on a draw
            elif self == "Y":
                return scores["A"] + score_outcomes["draw"]
            # end on a win
            else:
                return scores["B"] + score_outcomes["won"]
        # opponent chooses paper
        elif opponent == "B":
            # end on a loss
            if self == "X":
                return scores["A"] + score_outcomes["lost"]
                # end on a draw
            elif self == "Y":
                return scores["B"] + score_outcomes["draw"]
            # end on a win
            else:
                return scores["C"] + score_outcomes["won"]
        # opponent chooses scissors
        else:
            # end on a loss
            if self == "X":
                return scores["B"] + score_outcomes["lost"]
                # end on a draw
            elif self == "Y":
                return scores["C"] + score_outcomes["draw"]
            # end on a win
            else:
                return scores["A"] + score_outcomes["won"]

    total_score_part1 = 0
    total_score_part2 = 0
    for line in file:
        line = line.strip("\n").split(" ")
        total_score_part1 += determine_winner_part1(line)
        total_score_part2 += determine_winner_part2(line)

    return total_score_part1, total_score_part2


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


def day5(file):
    class Stack:
        def __init__(self, stack_number):
            self.stack_number = stack_number
            self.stack = []

        def add_to_stack(self, letter, initialization=False):
            if initialization:
                self.stack.insert(0, letter)
            else:
                self.stack.append(letter)

        def move_to_stack(self, move, destination):
            to_move = [self.stack.pop() for _ in range(move)]
            for elt in to_move:
                destination.add_to_stack(elt)

        def get_top_stack(self):
            return self.stack[-1]

        def move_multiple_to_stack(self, move, destination):
            to_move = self.stack[-move:]
            del self.stack[-move:]
            destination.stack.extend(to_move)

        def __repr__(self):
            return f"Stack<{self.stack}>"

    init_stack = []
    instructions = []
    is_stack = True
    for line in file:
        line = line.strip("\n")
        if is_stack and line:
            init_stack.append(line)
            continue
        else:
            is_stack = False

        if line:
            instructions.append(line)

    # generated the stack
    stack_numbers = re.findall(r'[0-9]', init_stack.pop(-1))
    stacks = {int(stack_number): Stack(stack_number) for stack_number in stack_numbers}
    for stack in init_stack:
        letters = [stack[index] for index in range(1, len(stack), 4)]
        for index, letter in enumerate(letters):
            if letter != " ":
                stacks[index + 1].add_to_stack(letter, True)

    # running the instructions (Part 1)
    # for instruction in instructions:
    #     instruction = [int(elt) for elt in re.findall(r'[0-9]+', instruction)]
    #     move, start, destination = instruction
    #     stacks[start].move_to_stack(move, stacks[destination])

    # running the instructions (Part 2)
    for instruction in instructions:
        move, start, destination = [int(elt) for elt in re.findall(r'[0-9]+', instruction)]
        stacks[start].move_multiple_to_stack(move, stacks[destination])

    return "".join([stacks[stack].get_top_stack() for stack in stacks])


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


def day7(file):
    class Directory:
        def __init__(self, name, parent=None):
            self.name = name
            self.parent = parent
            self.content = []

        def add_to_directory(self, content):
            """
            Adds content to this current directory
            :param content: an element of any type
            :return: None
            """
            self.content.append(content)

        def previous_directory(self):
            """
            Returns the previous directory
            :return: Directory
            """
            if self.parent is not None:
                return self.parent
            else:
                return self

        def get_directory(self, directory):
            """
            Finds a directory within the current directory and returns that directory
            :return: Directory or None
            """
            for content in self.content:
                if isinstance(content, Directory):
                    if content.name == directory:
                        return content

            return None

        def directory_size(self):
            """
            Returns the file size of the current directory
            :return: the size of the directory (int)
            """
            size = 0

            for content in self.content:
                if isinstance(content, Directory):
                    size += content.directory_size()
                else:
                    size += int(content[0])

            return size

        def __repr__(self):
            """
            An basic directory interpretation
            :return:
            """
            representation = f"{self.name} (dir) \n"
            for content in self.content:
                if isinstance(content, Directory):
                    representation += f"\t- {content.name} \n"
                else:
                    representation += f"\t- {content} \n"

            return representation

    parent_directory = Directory("/", None)
    current_directory = None
    lines = file.readlines()
    lines.append("end")
    collect_data = False
    for line in lines:
        if line == "end":
            break
        line = line.strip("\n")
        if collect_data:
            if line[0] != "$":
                line = line.split(" ")

                if line[0] == "dir":
                    current_directory.add_to_directory(Directory(line[1], current_directory))
                else:
                    current_directory.add_to_directory(line)
                continue
            else:
                collect_data = False  # this is the part where we hit the command line again
        # this is a command
        if line[0] == "$":
            command = line[2:].split(" ")
            if command[0] == "cd":
                argument = command[1]
                if argument == "..":
                    current_directory = current_directory.previous_directory()
                elif argument == "/":
                    current_directory = parent_directory
                else:
                    current_directory = current_directory.get_directory(argument)
            # if it is this command, then this means that we want to append all the data until we hit the command line
            elif command[0] == "ls":
                collect_data = True
                continue

    # print(parent_directory.directory_size())
    directories = [parent_directory]
    possible_deletion = []  # this is for part 2
    sum_of_directories = 0
    total_space = 70000000
    update_space = 30000000
    unused_space = total_space - parent_directory.directory_size()
    required_space = update_space - unused_space

    while directories:
        directory = directories.pop(0)
        size = directory.directory_size()

        if size >= required_space:
            possible_deletion.append(size)
        if size <= 100000:
            sum_of_directories += size

        for content in directory.content:
            if isinstance(content, Directory):
                directories.append(content)

    return sum_of_directories, min(possible_deletion)


def day8(file):
    grid = []
    total = 0

    def is_valid_coord(row, col, max_row, max_col):
        return 0 <= row <= max_row and 0 <= col <= max_col

    for line in file:
        line = [int(height) for height in line.strip("\n")]
        grid.append(line)

    total += len(grid[0]) + len(grid[-1])
    total += sum([2 for row in grid[1: -1]])
    cardinal_directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    # now we only have the internal layer of grids
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[row]) - 1):
            height = grid[row][col]

            for cardinal_direction in cardinal_directions:
                dr, dc = cardinal_direction
                nr, nc = row + dr, col + dc

                if is_valid_coord(nr, nc, len(grid), len(grid[row])):
                    # this means that it is visible
                    if height > grid[nr][nc]:
                        print(height, grid[nr][nc])
                        total += 1
                        break

    return total


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    # print(day1(file))
    # print(day2(file))
    # print(day3(file))
    # print(day4(file))
    # print(day5(file))
    # print(day6(file))
    # print(day7(file))
    print(day8(file))