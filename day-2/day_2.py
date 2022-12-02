def get_total_score(rounds_list):
    score_one = 0
    score_two = 0

    win_scores_part_one = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }

    win_scores_part_two = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }

    for match in rounds_list:
        score_one += win_scores_part_one[match]
        score_two += win_scores_part_two[match]

    print(f"Total Score for part one is: {score_one}")
    print(f"Total score for part two is: {score_two}")


with open("day_2.txt", "r", encoding="utf8") as file:
    content = file.read()
    rounds = list(content.splitlines())
    get_total_score(rounds)
