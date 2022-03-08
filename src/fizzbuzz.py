def fizzbuzz(n):
    """
    :param n: Integer
    :return: List of integers or substitutes based on multiples of 3 and/or 5
    """
    return ['Fizz' * (not x % 3) + 'Buzz' * (not x % 5) or str(x) for x in range(1, n)]


print()
print('\n'.join(fizzbuzz(51)))
