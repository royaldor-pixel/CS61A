def twenty_twenty_two():
    """Come up with the most creative expression that evaluates to 2022,
    using only numbers and the +, *, and - operators.

    >>> twenty_twenty_two()
    20223
    """
    return (20 + 20) ** 2 + 20 ** 2 + 22


if __name__ == '__main__':
    print(twenty_twenty_two())
