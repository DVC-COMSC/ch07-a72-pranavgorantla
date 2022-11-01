def sublist(sublist, lst):
    if not isinstance(sublist, list):
        raise ValueError("sublist must be a list")
    if not isinstance(lst, list):
        raise ValueError("lst must be a list")

    sublist_len = len(sublist)
    k=0
    s=None

    if (sublist_len > len(lst)):
        return False
    elif (sublist_len == 0):
        return True

    for x in lst:
        if x == sublist[k]:
            if (k == 0): s = x
            elif (x != s): s = None
            k += 1
            if k == sublist_len:
                return True
        elif k > 0 and sublist[k-1] != s:
            k = 0

    return False
