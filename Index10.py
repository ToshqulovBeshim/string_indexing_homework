def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    for i in range(len(s)):
        a+=int(s[i])
    return a
s="2345676543"
print(main(s))