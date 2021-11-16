a = 4
b = 15
for i in range(0, a):
    output = ""
    for j in range(0, b):
        if i == 0 or i == a-1:
            output += "*"
        else:
            if j == 0 or j == b-1:
                output += "*"
            else:
                output += " "
    print(output)