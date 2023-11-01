def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    d=""
    for i in range(len (s)):
        d+=s[i]+" "
    return d
    
s="56789876"
print(main(s))  