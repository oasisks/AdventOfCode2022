from __future__ import annotations


class Cave:
    def __init__(self):
        """
        This will represent the cave
        """
        self.rocks = set()
        self.sands = set()

        # this is to generate the grid
        self.min_x = float('inf')
        self.max_x = 0
        self.min_y = 0  # the minimum y will always be zero as the sand's location is at (500, 0)
        self.max_y = 0

    def add_rocks(self, starting_pos: list[int, int], ending_pos: list[int, int]):
        """
        Simulates adding rocks along the path in the cave
        :param starting_pos: the starting position (inclusive)
        :param ending_pos: the ending position (inclusive)
        :return: None
        """
        x_range = min(starting_pos[0], ending_pos[0]), max(starting_pos[0], ending_pos[0])
        y_range = min(starting_pos[1], ending_pos[1]), max(starting_pos[1], ending_pos[1])

        for x in range(x_range[0], x_range[1] + 1):
            for y in range(y_range[0], y_range[1] + 1):
                rock = x, y
                self._update_boundaries(x, y)
                self.rocks.add(rock)

    def simulation(self):
        """
        Just simulates the sands dropping
        :return: None
        """
        while self._simulate_sand():
            print(self)

    def _simulate_sand(self) -> bool:
        """
        Simulates a sand that falls from the position (500, 0).
        :return: tuple[int, int]
        """
        sand = 500, 0
        # attempt to simulate the sand going down
        # part 1
        while True:
            if self.falling_into_endless_void(sand):
                return False
            potential_sand = sand[0], sand[1] + 1
            # time.sleep(0.05)
            if potential_sand in self.rocks or potential_sand in self.sands or potential_sand[1] == self.max_y + 2:
                # check the left and right diagonal cells
                left = potential_sand[0] - 1, potential_sand[1]
                right = potential_sand[0] + 1, potential_sand[1]

                if left not in self.rocks and left not in self.sands:
                    sand = left
                    continue

                if right not in self.rocks and right not in self.sands:
                    sand = right
                    continue

                # at this point the sand has to be at rest
                self.sands.add(sand)
                return True

            sand = potential_sand

    def falling_into_endless_void(self, sand: tuple[int, int]) -> bool:
        """
        A help function that determines if a sand has gone out of bounds
        :param sand: the coordinate of the sand
        :return: bool
        """
        # for part 1
        x, y = sand
        return not (self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y)  # part 1

    def _update_boundaries(self, x, y):
        """
        A helper function
        :param x: x_coord
        :param y: y_coord
        :return:
        """
        if x < self.min_x:
            self.min_x = x
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

    def __str__(self):
        """
        This is a grid of the cave
        :return:
        """
        representation = ""
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                coord = x, y
                # location where the sand drops
                if coord == (500, 0):
                    representation += "+"
                    continue
                if coord in self.sands:
                    representation += "O"
                    continue
                if coord in self.rocks:
                    representation += "#"
                else:
                    representation += "."
            representation += "\n"

        return representation

    def __len__(self):
        """
        Just returns the number of sands
        :return: int
        """
        return len(self.sands)


def day14(file):
    cave = Cave()
    for line in file:
        line = line.strip("\n").split(" -> ")
        for _ in range(1, len(line)):
            starting_pos = [int(x) for x in line[_ - 1].split(",")]
            ending_pos = [int(x) for x in line[_].split(",")]
            cave.add_rocks(starting_pos, ending_pos)

    cave.simulation()

    return len(cave)


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day14(file))
    file.close()
