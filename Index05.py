def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    print(len(s))
    for i in range(len(s)):
        if s[i].isdigit():
            a+=1
    return a
s="3yhu3e839euhiy389ugbhnjmk,34567890-09876543234567890-=-09876543234567890-=-0987654321i"
print(main(s))