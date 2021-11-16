dogAgeHuman = int(input("Enter the dog's age in human years: "))
dogAge = 0;
for year in range(dogAgeHuman):
    year+=1
    if 0<year<3:
        dogAge += 10.5
    else:
        dogAge += 4
print(f"The dog's age in dog’s years is {dogAge} years.")