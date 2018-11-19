def anagramSolution1(s1,s2):
    if len(s1) != len(s2):
        stillOK = False

    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

def anagramSolution2(s1,s2):
    isMatch = True
    if len(s1) != len(s2):
        isMatch = False

    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    while pos < len(s1) and isMatch:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            isMatch = False

    return isMatch  

    

print(anagramSolution2('abcd','dcbsdsdsfa'))
