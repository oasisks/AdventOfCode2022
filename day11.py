from __future__ import annotations

import re


def day11(file):
    class Monkey:
        def __init__(self, number, starting_items, operation, tests, true, false):
            """
            This class will represent all of the monkeys in this problem
            """
            self.number = int(number[0])
            self.starting_items = [int(item) for item in starting_items]
            self.operation = operation[0]
            self.tests = int(tests[0])
            self.true = int(true[0])
            self.inspected_times = 0
            self.false = int(false[0])

        def throw_item(self, item, other_monkey: Monkey):
            """
            Throws an item to another monkey
            :param item: int
            :param other_monkey: Monkey
            :return: None
            """
            other_monkey.receive_item(item)

        def receive_item(self, item):
            self.starting_items.append(item)

        def inspect_items(self, monkeys: dict[int]):
            """
            The function that simulates how a monkey will inspect all elements
            :return:
            """
            for item in self.starting_items:
                self.inspected_times += 1
                operator = re.findall(r'\*|\+', self.operation)[0]
                operand = re.split(r'\s\+\s|\s\*\s', self.operation)
                term1 = item if operand[0] == 'old' else int(operand[0])
                term2 = item if operand[1] == 'old' else int(operand[1])

                if operator == "+":
                    new_worry_level = term1 + term2
                else:
                    new_worry_level = term1 * term2

                new_worry_level //= 3
                if new_worry_level % self.tests == 0:
                    # we do the true
                    self.throw_item(new_worry_level, monkeys[self.true])
                else:
                    # we do the false
                    self.throw_item(new_worry_level, monkeys[self.false])

            self.starting_items = []

        def __str__(self):
            return f"Monkey {self.number}: {' '.join([str(item) for item in self.starting_items])}"

    class Simulation:
        def __init__(self):
            """
            This will be used to simulate the monkey rounds
            """
            self.monkeys = {}

        def add_monkey(self, stats):
            """
            Adds a monkey base on the raw stats
            :param stats: str
            :return: None
            """
            number = re.findall(r'[0-9]+', stats[0])
            starting_items = re.findall(r'[0-9]+', stats[1])
            operation = re.findall(r'new\s*=\s*([\S\s]+)', stats[2])
            tests = re.findall(r'[0-9]+', stats[3])
            true = re.findall(r'[0-9]+', stats[4])
            false = re.findall(r'[0-9]+', stats[5])
            self.monkeys[int(number[0])] = Monkey(number, starting_items, operation, tests, true, false)

        def start_round(self):
            """
            Simulates the round
            :return:
            """
            for _ in range(20):
                for monkey in self.monkeys:
                    self.monkeys[monkey].inspect_items(self.monkeys)

        def top_two_annoying_monkey_scores(self):
            """
            Returns the result of multiplying two monkeys with the most inspected items
            :return:
            """
            scores = [monkey.inspected_times for monkey in self.monkeys.values()]
            scores.sort(reverse=True)

            return scores[0] * scores[1]

    simulation = Simulation()
    lines = [line.strip('\n') for line in file.readlines() if line.strip('\n') != '']

    for monkey in range(len(lines) // 6):
        simulation.add_monkey(lines[6 * monkey: 6 * (monkey + 1)])

    simulation.start_round()

    return simulation.top_two_annoying_monkey_scores()


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day11(file))
    file.close()
