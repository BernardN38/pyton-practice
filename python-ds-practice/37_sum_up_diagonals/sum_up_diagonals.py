def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73
m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> m2 = [
      [1, 2, 3, 9],
       [4, 5, 6, 3],
          [7, 8, 9,4],
                [4, 3, 9,8]
         ]
        >>> sum_up_diagonals(m2)
        30
    """
    i = 0
    sum = 0
    while i < len(matrix):
        sum += matrix[i][i]
        sum += matrix[i][-i-1]
        i+=1
    return sum

    [0][-1]
    [1][-2]
    [2][-3]
    [3][-4]