# ##### misc ##########
# Binary with fixed length, W.J. van der Laan, 2003/11/05
# Python Cookbook


def tobin(x, count=8):
    """
    Integer to binary
    Count is number of bits
    """
    return "".join(map(lambda y: str((x >> y) & 1), range(count - 1, -1, -1)))


def todec(s):
    count = len(s)
    return sum(
        map(
            lambda y: int(s[count - 1 - y]) * (2 ** y),
            range(count - 1, -1, -1),
        )
    )
