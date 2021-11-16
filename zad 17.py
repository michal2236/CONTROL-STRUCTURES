x = int(input("X:"))
y = int(input("Y:"))
if x<0 and y>0:
    print(f"Punkt p({x},{y}) jest w pierwszej ćwiartce")
elif x>0 and y>0:
    print(f"Punkt p({x},{y}) jest w drugiej ćwiartce")
elif x>0 and y<0:
    print(f"Punkt p({x},{y}) jest w trzeciej ćwiartce")
elif x<0 and y<0:
    print(f"Punkt p({x},{y}) jest w czwartej ćwiartce")