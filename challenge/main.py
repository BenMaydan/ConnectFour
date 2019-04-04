def longest_streak(input_string):
    """
    Return the longest streak <int> of repeated characters in `input_string`
    """
    string = 'aaaabbbcccdddd'


    character = input_string[0]
    streak = 1
    longest = 0

    for letter in input_string[1:]:
        if letter == character:
            streak += 1
        else:
            streak = 1
            character = letter

        if streak > longest:
            longest = streak

    return longest
