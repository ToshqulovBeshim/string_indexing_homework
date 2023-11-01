def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    a=0
    for i in range(len(s)):
        if s[i]=="*":
            a+=1
    if a==0:
        return False
    else:
        return a
s="UHYHJGhgdbh"
print(main(s))
            
        
    
        