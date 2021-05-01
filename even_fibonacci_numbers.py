def evenfbnum(limit):
    if limit<2:
        return 0
    ef1=0
    ef2=2
    sm=ef2+ef1
    while (ef2 <= limit):
        ef3 = 4 * ef2 + ef1
        if ef3 >= limit:
            break
        ef1=ef2
        ef2=ef3
        sm = sm + ef3
    return sm

# Driver Code
limit=4000000
print(evenfbnum(limit))
