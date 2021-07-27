def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    indices = []
    for number in nums:
        if goal - number in nums:
            indices.append((nums.index(goal-number),nums.index(number)))
    temp_last = 'initial'
    result = []
    for a,b in indices:
        if temp_last == 'initial':
            temp_last = max(a,b)
        if max(a,b) < temp_last:
            temp_last = max(a,b)
            result = (a,b)
  

    return result