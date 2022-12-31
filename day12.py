from __future__ import annotations


def day12(file):
    directions = {"right": (0, 1), "left": (0, -1), "up": (-1, 0), "down": (1, 0)}
    graph = {}

    def valid_cell(position: tuple[int, int], max_row: int, max_col: int) -> bool:
        """
        Given a position (x, y), checks if the position is within bounds
        :param position: tuple
        :param max_row: int
        :param max_col: int
        :return: bool
        """
        row, col = position
        return 0 <= row < max_row and 0 <= col < max_col

    def reachable(current_letter: str, other_letter: str):
        """
        Returns whether the current letter can reach the other letter
        :param current_letter: Cell
        :param other_letter: Cell
        :return: bool
        """
        if current_letter == "S":
            current_letter = ord('a')
        elif current_letter == "E":
            current_letter = ord('z')

        if other_letter == "S":
            other_letter = ord('a')
        elif other_letter == "E":
            other_letter = ord('z')

        current_letter = ord(current_letter) if isinstance(current_letter, str) else current_letter
        other_letter = ord(other_letter) if isinstance(other_letter, str) else other_letter

        distance = other_letter - current_letter

        if distance <= 1:
            return True

        return False

    def bfs(graph: dict, source: tuple[str, tuple], destination: tuple[str, tuple]) -> tuple:
        """
        Returns the shortest path from source to destination
        :param graph: dict
        :param source: represents the source
        :param destination: represents the destination
        :return: tuple
        """
        to_be_visited = [(source, )]
        visited = set()
        visited.add(source)

        while to_be_visited:
            cell = to_be_visited.pop(0)

            if cell[-1] == destination:
                return cell

            neighbors = graph[cell[-1]]

            for neighbor in neighbors:
                if neighbor not in visited:
                    to_be_visited.append((*cell, neighbor))
                    visited.add(neighbor)

        return ()

    lines = file.readlines()
    max_row = len(lines)
    max_col = len(lines[0]) - 1  # account for the /n
    destination = None
    source = None
    sources = []

    # graph generation
    for row, line in enumerate(lines):
        line = line.strip("\n")
        for col, current_cell in enumerate(line):
            children = []
            if current_cell == "S" or current_cell == "a":
                sources.append((current_cell, (row, col)))
                # this is to maintain part 1
                if current_cell == "S":
                    source = current_cell, (row, col)
            if current_cell == "E":
                destination = current_cell, (row, col)

            # go through all 4 cardinal directions
            for direction in directions:
                neighbor_coord = row + directions[direction][0], col + directions[direction][1]
                # only add the neighbor if the cell is valid and is reachable from the current cell
                if valid_cell(neighbor_coord, max_row, max_col):
                    neighbor_cell = lines[neighbor_coord[0]][neighbor_coord[1]]
                    if reachable(current_cell, neighbor_cell):
                        children.append((neighbor_cell, neighbor_coord))

            # add the edges to the graph
            graph[(current_cell, (row, col))] = children

    # we are subtracting for over counting the source
    min_distance = float('inf')
    for potential_sources in sources:
        path = bfs(graph, potential_sources, destination)
        if path:
            if len(path) - 1 < min_distance:
                min_distance = len(path) - 1

    return len(bfs(graph, source, destination)) - 1, min_distance


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day12(file))
    file.close()
