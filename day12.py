def day12(file):
    def get_neighbors(coord: tuple[int, int]):
        """
        Returns all the neighbor coordinates given a specified coord.
        :param coord: tuple[int]
        :return: list
        """
        row, col = coord
        return [(r + row, c + col) for r in range(-1, 2) for c in range(-1, 2)]

    graph = {}
    for row, line in enumerate(file):
        line = line.strip("\n")

        for col, letter in enumerate(line):
            print(get_neighbors((row, col)))




if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day12(file))
    file.close()
