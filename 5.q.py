def count_pattern_occurrences(text):
    pattern_count: int = 0
    index = 0

    # Iterate through the text
    while index < len(text):
        # Find the next occurrence of "C"
        while index < len(text) and text[index] != "C":
            index += 1

        # If "C" is not found, break the loop
        if index == len(text):
            break

        # Check if the pattern starts with "C" and ends with "jeb"
        pattern_found = True
        jeb_index = 0

        while index < len(text) and jeb_index < 3 and text[index] == ("Cjeb"[jeb_index]):
            index += 1
            jeb_index += 1

        if jeb_index < 3:
            pattern_found = False

        if pattern_found:
            pattern_count += 1

    return pattern_count