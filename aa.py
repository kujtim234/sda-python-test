name = "Ana Tot"
x = name.split()
print(x)

name = "Ana Tot"[::-1]
print(name)

name = "Ana Tot"
x = name.replace("Ana","Frasheri")
print(x)

name = "Ana Tot"
count = name.lower().count("a")
print(f"Shkronja 'A' është përmendur {count} herë.")

name = "Ana Tot"
surname = "Frasheri"
new_name = name + " " + surname
print(new_name)

# "Ana" vendosi te mbaje nje emer te mesit, emer pagezimi... => "Ana (Anastasia) Toti"

original_string = "Ana Tot"
string_to_insert = ("Anastasia")
middle_index = len(original_string) // 2  # Gjej pozitën e mesme
new_string = original_string[:middle_index]+ " " + string_to_insert + original_string[middle_index:]
print(new_string)