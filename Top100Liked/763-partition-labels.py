# 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
# a  b  a  b  c  b  a  c  a  d  e   f   e    g   d   e   h   i   j   h   k   l   i  j


# ababcbaca  defegde  hijhklij


def partition_labels(S):
    rightmost = {c: i for i, c in enumerate(S)}
    left, right = 0, 0

    result = []
    for i, letter in enumerate(S):

        right = max(right, rightmost[letter])

        if i == right:
            result += [right - left + 1]
            left = i + 1

    return result


partition_labels("ababcbacadefegdehijhklij")
