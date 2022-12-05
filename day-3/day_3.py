def generate_priority(rucksacks):
    priority_total = 0
    for rucksack in rucksacks:
        first_half = rucksack[0 : len(rucksack) // 2]
        second_half = rucksack[len(rucksack) // 2 : len(rucksack)]
        values_in_first_half = set()
        for char in first_half:
            values_in_first_half.add(char)
        for char in second_half:
            if char in values_in_first_half:
                new_char_priority = 0
                if char.islower():
                    new_char_priority = ord(char) - 96
                else:
                    new_char_priority = ord(char) - 38

                priority_total += new_char_priority
                break

    return priority_total


def generate_badge(rucksacks):
    groups = {}
    index = 0
    count = 1
    priority_total = 0
    for rucksack in rucksacks:
        if index in groups:
            groups[index].append(rucksack)
        else:
            groups[index] = [rucksack]

        if count % 3 == 0:
            index += 1
        count += 1

    for group in groups.items():
        rucksacks = group[1]
        chars_in_first = set()
        chars_in_second = set()
        for char in rucksacks[0]:
            chars_in_first.add(char)
        for char in rucksacks[1]:
            chars_in_second.add(char)
        for char in rucksacks[2]:
            if char in chars_in_first:
                new_char_priority = 0
                if char in chars_in_second:
                    if char.islower():
                        new_char_priority = ord(char) - 96
                    else:
                        new_char_priority = ord(char) - 38

                    priority_total += new_char_priority
                    break

    return priority_total


with open("day_3.txt", "r", encoding="utf8") as file:
    content = file.read()
    rucksacks_input = list(content.splitlines())
    priority_sum = generate_priority(rucksacks_input)
    print("The sum of priorities is:", priority_sum)
    badge_priority = generate_badge(rucksacks_input)
    print("The sum of badge priorities is:", badge_priority)
