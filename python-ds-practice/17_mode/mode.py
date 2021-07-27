def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    result = {}
    used_numbers = []
    for number in nums:
        if number not in used_numbers:
            result[number] = nums.count(number)
            used_numbers.append(number)
    modes = []
    for key, value in result.items():
        max_val = max(result.values())
        if value == max_val:
            modes.append(key)
    return modes