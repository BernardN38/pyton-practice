def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    phrase = phrase.split(' ')
    for idx,word in enumerate(phrase):
        phrase[idx] = word.capitalize()
    result = ' '
    return result.join(phrase)