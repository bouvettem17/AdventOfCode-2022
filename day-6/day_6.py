"""Day 6 Advent of Code - Sliding Window"""


def has_duplicate(window):
    """Checking for duplicate"""
    seen = set()
    for char in window:
        if char in seen:
            return True
        seen.add(char)

    return False


def slide_window(window, datastream, idx_datastream):
    """Moves the window being looked at for duplicates"""
    subtract_value = 13
    for idx_window in range(0, 14):
        window[idx_window] = datastream[idx_datastream - subtract_value]
        subtract_value -= 1

    return window


def find_marker(datastream):
    """Find the location where the message begins"""
    current_window = ["" for _ in range(14)]
    has_duplicate_flag = True
    idx = 14
    while has_duplicate_flag and idx < len(datastream):
        current_window = slide_window(current_window, datastream, idx)
        has_duplicate_flag = has_duplicate(current_window)
        idx += 1

    return idx


with open("day_6.txt", "r", encoding="utf8") as file:
    CONTENT = str(file.read())
    MARKER_IDX = find_marker(CONTENT)
    print("The message will begin at index:", MARKER_IDX)
