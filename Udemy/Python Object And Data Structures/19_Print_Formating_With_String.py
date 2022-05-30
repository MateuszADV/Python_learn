print('To jest string {}'.format('Wstawianie'))

print("The {2} {1} {0} ".format("fox", "brown", "quick"))
print("The {0} {0} {0} ".format("fox", "brown", "quick"))
print("The {q} {b} {f} ".format(f = "fox", b = "brown", q ="quick"))
print("------------------------------------------------------")

# Float Formatting fallows

result = 100/777
print(result)
print("The result was {:1.3f}".format(result))
print("The result was {r:1.5f}".format(r = result))

print("------------------------------------------------------")

name = "Mateusz"
print(f"Hello, his name is {name}")

name = "Sam"
age = 3
print(f"{name} is {age} years old.")