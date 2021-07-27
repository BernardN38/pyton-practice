def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    result = {}
    used_letters = []
    for letter in phrase:
        if letter not in used_letters and letter != ' ':
            result[letter] = phrase.count(letter)
            used_letters.append(letter)
    return result