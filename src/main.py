def happy_number(n):
    """
        Determine if a number is a Happy Number.

        A Happy Number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy numbers.

        Args:
        n (int): A positive integer to check.

        Returns:
        bool: True if n is a Happy Number, False otherwise.

        Example:
        >>> happy_number(19)
        True
        >>> happy_number(4)
        False

        Note:
        This function uses a set to detect cycles and prevent infinite loops.
        """
    senn_number = set()
    while n != 1 and (n not in senn_number):
        senn_number.add(n)
        n = sum([int(i)**2 for i in str(n)])
    return n == 1

if __name__ == "__main__":
    assert happy_number(7) is True
    assert happy_number(44) is True
    assert happy_number(45) is False
    assert happy_number(8) is False