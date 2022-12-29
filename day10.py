def day10(file):
    class CPU:
        def __init__(self):
            """
            This class will represent the CPU described by the problem
            """
            self.cycle = 1
            self.X = 1
            self.logs = {}
            self.image = [["." for _ in range(40)] for _ in range(6)]

        def execute_instruction(self, instruction: list):
            """
            Takes in an instruction, executes it, renders the image, and saves it to some logs
            :param instruction: list
            :return: None
            """
            # during every cycle, we will be adding a "#" to the row

            if instruction[0] == "noop":
                self.logs[self.cycle] = self.X
                # if the current cycle is contained within the available # ranges
                if self.X - 1 <= (self.cycle - 1) % 40 <= self.X + 1:
                    self.image[self.cycle // 40][self.cycle % 40 - 1] = "#"
                self.cycle += 1
            elif instruction[0] == "addx":
                # simulating two cycles and saves it during the cycle
                for _ in range(2):
                    self.logs[self.cycle] = self.X
                    if self.X - 1 <= (self.cycle - 1) % 40 <= self.X + 1:
                        self.image[self.cycle // 40][self.cycle % 40 - 1] = "#"
                    self.cycle += 1
                self.X += int(instruction[1])

        def show_logs(self):
            """
            Shows the logs
            :return: None
            """
            for cycle, value in self.logs.items():
                print(f"During cycle {cycle} with value {value}")

        def total_signal_strength(self):
            """
            Returns the total strength at some predetermined cycle
            :return: int
            """
            strength = 0
            cycles = [20, 60, 100, 140, 180, 220]
            for cycle in cycles:
                strength += cycle * self.logs[cycle]

            return strength

        def render_image(self):
            """
            Renders the image
            :return: None
            """
            for row in self.image:
                print("".join(row))

    cpu = CPU()
    for line in file:
        line = line.strip("\n").split(" ")
        cpu.execute_instruction(line)
        
    cpu.render_image()
    return cpu.total_signal_strength()


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day10(file))
    file.close()
