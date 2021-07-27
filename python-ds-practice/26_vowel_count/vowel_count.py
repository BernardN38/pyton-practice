def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    result = {}
    used_letters = []
    phrase = phrase.lower()
    for char in phrase:
        if char in 'aeiou' and char not in used_letters:
            result[char] = phrase.count(char)
    return result