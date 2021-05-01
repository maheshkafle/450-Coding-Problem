total = 0
for x in range(1000):
    if x%3==0 and x%5==0:
        total=x+total
print("total",total)