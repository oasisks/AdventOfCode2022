def day8(file):
    def next_great_value(iterable: list):
        """
        Returns a list of indices that points to the next great value
        NOTE: This is a variation. Values of the same will be considered as the next great value (i.e. [5, 5] = [1, -1])
        input: [1, 3, 2, 5, 6, 21]
        output: [1, 3, 3, 4, 5, -1] -> [3, 5, 5, 6, 21, -1]
        :param iterable: a list of values
        :return: list of indices
        """

        # pops the first element from the list
        stack = []
        indices = [0] * len(iterable)

        for index, elt in enumerate(iterable):
            # if the stack is empty just push the element and move on
            data = elt, index

            if not stack:
                stack.append(data)
                continue
            if elt < stack[-1][0]:
                stack.append(data)
                continue
            while stack and elt >= stack[-1][0]:
                indices[stack.pop()[1]] = index

            stack.append(data)

        # the remaining elements in the stack will have no greater element
        while stack:
            indices[stack.pop()[1]] = -1

        return indices

    def count_visible_trees(grid):
        """
        Returns a count of all visible trees
        :param grid: list[list]
        :return: int
        """
        total_visible_trees = 0
        for row in grid:
            for col in row:
                if col:
                    total_visible_trees += 1

        return total_visible_trees

    def update_grid(grid, visibility, col=None, row=None, horizontal=False):
        """
        Sets a tree to be true if the tree is visible
        :param visibility: list
        :param grid: list[list]
        :param col: int
        :param row: int
        :param horizontal: bool
        :return: None
        """
        if horizontal and row is not None:
            for index, tree in enumerate(visibility):
                # there is no tree bigger than the current tree when looking horizontally
                if tree == -1:
                    grid[row][index] = True
        elif not horizontal and col is not None:
            for index, tree in enumerate(visibility):
                # there is no tree bigger than the current tree when looking vertically
                if tree == -1:
                    grid[index][col] = True

    def find_highest_scenic_score(grid):
        """
        Finds the highest scenic score given a grid of scenic scores
        :param grid: list[list]
        :return: int
        """

        highest_score = None
        for row in grid:
            for col in row:
                if highest_score is None:
                    highest_score = col
                    continue
                if col > highest_score:
                    highest_score = col

        return highest_score

    def update_grid_scenic_score(grid, visibility, row=None, col=None, horizontal=True):
        """
        This updates the grid from left_to_right and top_to_bottom
        :param grid: list[list]
        :param visibility: list
        :param row: int
        :param col: int
        :param horizontal: bool
        :return: None
        """
        for index, tree in enumerate(visibility):
            if horizontal:
                if tree != -1:
                    grid[row][index] *= tree - index
                else:
                    grid[row][index] *= len(left_to_right) - 1 - index
            else:
                if tree != -1:
                    grid2[index][col] *= tree - index
                else:
                    grid2[index][col] *= len(top_to_bottom) - 1 - index

    def update_grid_scenic_score_reverse(grid, visibility, row=None, col=None, horizontal=True):
        for index, tree in enumerate(visibility[::-1]):
            new_index = len(visibility) - 1 - tree
            if horizontal:
                if tree != -1:
                    grid[row][index] *= abs(index - new_index)
                else:
                    grid[row][index] *= index
            else:
                if tree != -1:
                    grid[index][col] *= abs(index - new_index)
                else:
                    grid[index][col] *= index

    lines = [[int(num) for num in line.strip("\n")] for line in file.readlines()]

    grid1 = [[False for elt in line] for line in lines]  # part 1
    grid2 = [[1 for elt in line] for line in lines]  # part 2

    # this is checking the rows
    for row in range(len(lines)):
        trees = lines[row]
        left_to_right = next_great_value(trees)
        right_to_left = next_great_value(trees[::-1])

        # this updates the grid
        update_grid(grid1, left_to_right, horizontal=True, row=row)
        update_grid(grid1, right_to_left[::-1], horizontal=True, row=row)

        # this is part 2
        update_grid_scenic_score(grid2, left_to_right, row=row, horizontal=True)
        update_grid_scenic_score_reverse(grid2, right_to_left, row=row, horizontal=True)

    # this is checking the columns
    for col in range(len(lines)):
        column = []
        for row in range(len(lines)):
            column.append(lines[row][col])

        top_to_bottom = next_great_value(column)
        bottom_to_top = next_great_value(column[::-1])

        update_grid(grid1, top_to_bottom, col=col)
        update_grid(grid1, bottom_to_top[::-1], col=col)

        # this is part 2
        update_grid_scenic_score(grid2, top_to_bottom, col=col, horizontal=False)
        update_grid_scenic_score_reverse(grid2, bottom_to_top, col=col, horizontal=False)

    return count_visible_trees(grid1), find_highest_scenic_score(grid2)


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day8(file))
    file.close()
