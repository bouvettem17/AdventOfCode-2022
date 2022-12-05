import collections

with open("day_5.txt", "r", encoding="utf8") as file:
    content = file.read()
    lines = list(content.splitlines())
    line = lines[0]
    index = 0
    stacks = {}
    while line[1] != "1":
        for idx, char in enumerate(line):
            if char.isalnum():
                stacks[idx] = stacks.get(idx, []) + [char]
        index += 1
        line = lines[index]

    stacks_adjusted = {}
    for idx, val in enumerate(line):
        if val.isalnum():
            stacks_adjusted[int(val)] = collections.deque(stacks[idx])

    index += 2
    remaining_lines = lines[index::]
    for line in remaining_lines:
        list_line = line.split()
        number_of_items_to_move = int(list_line[1])
        start_stack = int(list_line[3])
        items_to_move = collections.deque()
        end_stack = int(list_line[5])
        for _ in range(number_of_items_to_move):
            items_to_move.append(stacks_adjusted[start_stack].popleft())
        while items_to_move:
            stacks_adjusted[end_stack].appendleft(items_to_move.pop())

    PRINT_STRING = ""
    for queue in stacks_adjusted.items():
        PRINT_STRING += queue[1][0]

    print("The top of each stack is:", PRINT_STRING)
