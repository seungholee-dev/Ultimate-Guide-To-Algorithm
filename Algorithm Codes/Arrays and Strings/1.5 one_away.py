def if_one_away(s1, s2):
    # Length check
    if abs(len(s1) -  len(s2)) > 1:
       return False

    # Always make s2 longer than s1
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    
    # Flag for checking if there are more than one difference
    different_flag = False

    i, j = 0, 0

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            if different_flag:
                return False
            different_flag = True
            j += 1
    return True
    

# driver code
if __name__ == "__main__":
    print(if_one_away("pale", "plee"))