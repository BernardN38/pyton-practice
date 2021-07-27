def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_list_one = list(str(num1))
    num_list_two = list(str(num2))
    used_numbers = []
    counts_one = {}
    counts_two = {}
    for number in num_list_one:
        if number not in used_numbers:
            counts_one[number] = num_list_one.count(number)
            used_numbers.append(number)
        used_numbers = []
    for number in num_list_two:
        if number not in used_numbers:
            counts_two[number] = num_list_two.count(number)
            used_numbers.append(number)
        used_numbers = []
    sorted_count_one = sorted(counts_one.items(), key=lambda x: x[0], reverse=True)
    sorted_count_two = sorted(counts_two.items(), key=lambda x: x[0], reverse=True)
    return sorted_count_one == sorted_count_two