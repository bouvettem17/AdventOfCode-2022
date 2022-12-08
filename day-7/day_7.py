"""Day 7 Advent of Code - No Space Left On Device"""


def sum_directories(directories):
    "Sum The Directories That Have Size Less Than 100000 (Part 1)"
    directory_sum = 0
    for directory in directories:
        if directories[directory] <= 100000:
            directory_sum += directories[directory]

    return directory_sum


def handle_commands(inputs):
    """Handle Command"""
    directories = {"/": 0}
    current_path = ["/"]
    current_directories = ["/"]
    idx = 0
    while idx < len(inputs):
        current_line = inputs[idx].split()
        if current_line[0] == "$" and current_line[1] == "cd":
            if current_line[2] == "/":
                current_path = ["/"]
                current_directories = ["/"]
            elif current_line[2] == "..":
                current_path.pop()
                current_directories.pop()
            else:
                current_path.append(current_line[2])
                current_directories.append("/".join(current_path))
                if "/".join(current_path) not in directories:
                    directories["/".join(current_path)] = 0
        if current_line[0].isnumeric():
            for directory in current_directories:
                directories[directory] += int(current_line[0])
        idx += 1

    res = sum_directories(directories)
    print("The sum of directories of size < 100000 is:", res)

    current_system_size = directories["/"]
    remaining_space = 70000000 - current_system_size
    necessary_deletion_size = 30000000 - remaining_space
    current_deletion_directory_size = current_system_size

    for (directory, size) in directories.items():
        if necessary_deletion_size < size < current_deletion_directory_size:
            current_deletion_directory_size = size

    print(
        "The Smallest Directory We Can Delete Has Size:",
        current_deletion_directory_size,
    )


with open("day_7.txt", "r", encoding="utf8") as file:
    content = file.read()
    terminal_inputs = list(content.splitlines())
    handle_commands(terminal_inputs)
