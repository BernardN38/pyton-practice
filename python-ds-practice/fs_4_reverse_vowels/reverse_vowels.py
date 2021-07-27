def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    string = list(s)
    vowel_locations = []
    locations = []
    i = 0
    for char in string:
        if char in 'aeiouAEIOU':
            vowel_locations.append(char)
            locations.append('.')
        else:
            locations.append(char)
    vowel_locations.reverse()
    for idx,char in enumerate(locations):
        if char == '.':
            locations[idx] = vowel_locations[i]
            i +=1
    print(''.join(locations))
