
def day7(file):
    class Directory:
        def __init__(self, name, parent=None):
            self.name = name
            self.parent = parent
            self.content = []

        def add_to_directory(self, content):
            """
            Adds content to this current directory
            :param content: an element of any type
            :return: None
            """
            self.content.append(content)

        def previous_directory(self):
            """
            Returns the previous directory
            :return: Directory
            """
            if self.parent is not None:
                return self.parent
            else:
                return self

        def get_directory(self, directory):
            """
            Finds a directory within the current directory and returns that directory
            :return: Directory or None
            """
            for content in self.content:
                if isinstance(content, Directory):
                    if content.name == directory:
                        return content

            return None

        def directory_size(self):
            """
            Returns the file size of the current directory
            :return: the size of the directory (int)
            """
            size = 0

            for content in self.content:
                if isinstance(content, Directory):
                    size += content.directory_size()
                else:
                    size += int(content[0])

            return size

        def __repr__(self):
            """
            An basic directory interpretation
            :return:
            """
            representation = f"{self.name} (dir) \n"
            for content in self.content:
                if isinstance(content, Directory):
                    representation += f"\t- {content.name} \n"
                else:
                    representation += f"\t- {content} \n"

            return representation

    parent_directory = Directory("/", None)
    current_directory = None
    lines = file.readlines()
    lines.append("end")
    collect_data = False
    for line in lines:
        if line == "end":
            break
        line = line.strip("\n")
        if collect_data:
            if line[0] != "$":
                line = line.split(" ")

                if line[0] == "dir":
                    current_directory.add_to_directory(Directory(line[1], current_directory))
                else:
                    current_directory.add_to_directory(line)
                continue
            else:
                collect_data = False  # this is the part where we hit the command line again
        # this is a command
        if line[0] == "$":
            command = line[2:].split(" ")
            if command[0] == "cd":
                argument = command[1]
                if argument == "..":
                    current_directory = current_directory.previous_directory()
                elif argument == "/":
                    current_directory = parent_directory
                else:
                    current_directory = current_directory.get_directory(argument)
            # if it is this command, then this means that we want to append all the data until we hit the command line
            elif command[0] == "ls":
                collect_data = True
                continue

    # print(parent_directory.directory_size())
    directories = [parent_directory]
    possible_deletion = []  # this is for part 2
    sum_of_directories = 0
    total_space = 70000000
    update_space = 30000000
    unused_space = total_space - parent_directory.directory_size()
    required_space = update_space - unused_space

    while directories:
        directory = directories.pop(0)
        size = directory.directory_size()

        if size >= required_space:
            possible_deletion.append(size)
        if size <= 100000:
            sum_of_directories += size

        for content in directory.content:
            if isinstance(content, Directory):
                directories.append(content)

    return sum_of_directories, min(possible_deletion)


if __name__ == '__main__':
    file = open("input.txt", "r", encoding="utf-8")
    print(day7(file))
    file.close()
