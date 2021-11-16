last_a = 0
last_b = 1
output = ""
for i in range(0, 50):
    if i < 2:
        output += f"{i} "
    else:
        actual = last_a + last_b
        output += f"{actual} "
        last_a = last_b
        last_b = actual
print(output)
        