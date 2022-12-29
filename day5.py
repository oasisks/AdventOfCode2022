import re


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


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day5(file))
    file.close()
