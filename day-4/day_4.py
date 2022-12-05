def find_full_overlaps(pairs):
    overlaps = 0
    for current_pair in pairs:
        current_pair.sort()
        if (
            current_pair[0][0] != current_pair[1][0]
            and current_pair[0][1] >= current_pair[1][1]
        ):
            overlaps += 1
        elif current_pair[0][0] == current_pair[1][0]:
            overlaps += 1

    return overlaps


def find_all_overlaps(pairs):
    overlaps = 0
    for current_pair in pairs:
        current_pair.sort()
        if current_pair[1][0] <= current_pair[0][1]:
            overlaps += 1

    return overlaps


with open("day_4.txt", "r", encoding="utf8") as file:
    content = file.read()
    assignment_pairs = list(content.splitlines())
    assignment_pairs = [pair.split(",") for pair in assignment_pairs]
    for idx, pair in enumerate(assignment_pairs):
        split_interval_one = pair[0].split("-")
        split_interval_two = pair[1].split("-")
        pair[0] = (int(split_interval_one[0]), int(split_interval_one[1]))
        pair[1] = (int(split_interval_two[0]), int(split_interval_two[1]))
    FULL_OVERLAP_COUNT = find_full_overlaps(assignment_pairs)
    print("The number of full overlaps is:", FULL_OVERLAP_COUNT)
    ALL_OVERLAP_COUNT = find_all_overlaps(assignment_pairs)
    print("The number of overlaps in total is:", ALL_OVERLAP_COUNT)
