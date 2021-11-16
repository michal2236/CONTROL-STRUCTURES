numbers = []
is_end = False
sum = 0
while is_end == False:
    input_n = int(input("Enter number: "))
    if input_n == 0:
        is_end = True
    else:
        numbers.append(input_n)
for i in range(0, len(numbers)):
    sum += numbers[i]

print(f"RESULT: Quantity={len(numbers)}, Sum={sum}. Mean={sum/len(numbers)}")