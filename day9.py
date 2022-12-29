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

        def move(self, vector: list[bool]):
            """
            Updates the current position of the knot
            :return: None
            """
            self.x += vector[0]
            self.y += vector[1]
            print(self.x, self.y)
            self.visited.add((self.x, self.y))

    class Tail(Knot):
        def __init__(self):
            super(Tail, self).__init__()

        def move(self, head: Knot):
            """
            The tail will move base on the position of the head
            :param head: Knot
            :return: None
            """

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

    print(rope.head.get_position())


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day9(file))
    file.close()