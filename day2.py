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


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day2(file))
    file.close()
