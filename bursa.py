# Lista e numrave
grades = [7, 8, 8, 7]
name = ("ana")

# Llogaritja e mesatares
average = sum(grades) / len(grades)

# Printo rezultatin
print(f"Mesatarja e numrave është: {average:.2f}")


if(average < 4):
    print("ti nuk perfiton burse")

if(average >= 7):
    print("perfiton 50% burse")

if(average >= 9):
    print("perfiton burse te plote")
