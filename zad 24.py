stars = ""
for i in range(1,10):
    if i < 6:
        stars += "*"
    else:
        stars = ""
        for j in range(0, 10-i):
            stars += "*"
    print(stars)
