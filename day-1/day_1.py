def create_numbers(imported_food_items):
    index = 0
    elf_calories = [0]

    for line in imported_food_items.splitlines():
        if line == "":
            index += 1
            elf_calories.append(0)
        else:
            elf_calories[index] += int(line)

    top_three = [0, 0, 0]
    for calorie_count in elf_calories:
        if calorie_count > top_three[0]:
            top_three[2] = top_three[1]
            top_three[1] = top_three[0]
            top_three[0] = calorie_count
        elif calorie_count > top_three[1]:
            top_three[2] = top_three[1]
            top_three[1] = calorie_count
        elif calorie_count > top_three[2]:
            top_three[2] = calorie_count

    return sum(top_three)


with open("day_1.txt", "r", encoding="utf8") as file:
    imported_content = file.read()
    max_calories = create_numbers(imported_content)
    print(max_calories)
