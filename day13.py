from __future__ import annotations


def is_right_order(left: list, right: list) -> bool:
    """
    Determines if the left and right packet are in right order
    :param left: list
    :param right: list
    :return: bool
    """
    max_length = min(len(left), len(right))

    for index in range(max_length):
        left_val = left[index]
        right_val = right[index]
        # print(f"Comparing: {left_val} vs {right_val}")

        if isinstance(left_val, int) and isinstance(right_val, int):
            if right_val < left_val:
                return False
            elif right_val > left_val:
                return True

        elif isinstance(left_val, list) and isinstance(right_val, list):
            is_ordered = is_right_order(left_val, right_val)
            if is_ordered is not None:
                return is_ordered
        else:
            if isinstance(left_val, int):
                left_val = [left_val]
            elif isinstance(right_val, int):
                right_val = [right_val]
            is_ordered = is_right_order(left_val, right_val)
            if is_ordered is not None:
                return is_ordered

    if len(left) != len(right):
        return len(left) < len(right)


def parse_list(input_string: str, starting_index: int) -> tuple[list, int]:
    """
    Given a correct input_string that represents a list, return the list
    We will assume that the first element of the input_string is a [

    Example input_strings:
    1) [1, 2, 3]
    2) [[2], [2]]
    3) [[[]]]

    :param input_string: str
    :param starting_index: int
    :return: tuple[list, int]
    """
    result = []
    element = ""
    while starting_index < len(input_string):
        character = input_string[starting_index]
        starting_index += 1

        if character == "[":
            # what happens here is that when we recurse, we want to make sure that the previous recursion doesn't run
            # the same parts of the string again
            parsed_result, starting_index = parse_list(input_string, starting_index)
            result.append(parsed_result)
        elif character == "]":
            if element != '':
                result.append(int(element))
            return result, starting_index
        else:
            if character != ",":
                element += character
            else:
                if element != '':
                    result.append(int(element))
                    element = ""


def day13(file):
    left_packets, right_packets = [], []
    lines = [line.strip("\n") for line in file.readlines() if line.strip("\n") != ""]

    part1 = 0
    for index, line in enumerate(lines):
        if index % 2 == 0:
            left_packets.append(parse_list(line, 1)[0])
        else:
            right_packets.append(parse_list(line, 1)[0])

    for packet in range(len(left_packets)):
        left, right = left_packets[packet], right_packets[packet]

        is_ordered = is_right_order(left, right)
        if is_ordered or is_ordered is None:
            part1 += packet + 1

    return part1


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day13(file))
    file.close()
