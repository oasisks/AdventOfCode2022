from __future__ import annotations


def day9(file):
    cardinal_vectors = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    class Knot:
        def __init__(self):
            """
            This represents the basic object block for this problem
            """
            self.x = 0
            self.y = 0
            self.visited = set()

        def get_position(self):
            """
            Returns the current position of the knot
            :return: tuple(x, y)
            """

            return self.x, self.y

        def move(self, vector: tuple[int, int]):
            """
            Updates the current position of the knot
            :return: None
            """
            self.x += vector[0]
            self.y += vector[1]
            self.visited.add((self.x, self.y))

        def get_visited_length(self):
            return len(self.visited)

    class Tail(Knot):
        def __init__(self):
            super(Tail, self).__init__()

        def move(self, head: Knot):
            """
            The tail will move base on the position of the head
            :param head: Knot
            :return: None
            """

            # the tail will only move, if the head is two steps ahead
            x_diff = head.x - self.x
            y_diff = head.y - self.y

            if abs(x_diff) == 2:
                x_displacement = int(x_diff / 2)

                # this is a diagonal
                if abs(y_diff) == 1:
                    self.x += x_displacement
                    self.y += y_diff
                else:
                    self.x += x_displacement
            elif abs(y_diff) >= 2:
                y_displacement = int(y_diff / 2)

                # this is a diagonal
                if abs(x_diff) == 1:
                    self.x += x_diff
                    self.y += y_displacement
                else:
                    self.y += int(y_diff / 2)

            self.visited.add(self.get_position())

    class Rope:
        def __init__(self):
            """
            This will be place that simulates the rope
            """
            self.head = Knot()
            self.tail = Tail()

        def update(self, direction, unit):
            """
            Update the position of the head which ultimately updates the position of the tail
            :param direction: str
            :param unit: int
            :return: None
            """
            # this simulates frames
            for step in range(unit):
                self.head.move(cardinal_vectors[direction])
                self.tail.move(self.head)  # the tail will be updated each frame along with the head

    rope = Rope()
    for line in file:
        direction, unit = line.strip("\n").split(" ")
        rope.update(direction, int(unit))

    return rope.tail.get_visited_length()


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day9(file))
    file.close()
