number = int(input("Enter your number: "))
output = ""
for i in range(1, number+1):
    div = 0
    for j in range(1, i+1):
        if i % j == 0:
            div += 1
    if div == 2:
        output += f"{i} "
print(f"Prime numbers: {output}")