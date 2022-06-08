my_list = [1,2,3]
my_list = ["String", 100, 23.56]

print(my_list)
print(len(my_list))

my_list = ["one", "two", "three"]
print(my_list[0])
print(my_list[1:])
another_list = ["four", "five"]
new_list = my_list + another_list
print("------DODAWANIE LIST-----------")
print(my_list)
print(another_list)
print(new_list)
new_list[0] = "ONE ALL CAPS"
print(new_list)
new_list.append("six")
print(new_list)
new_list.append("seven")
print(new_list)

print(new_list.pop())
print(new_list)
print(new_list.pop(0))
print(new_list)

print("-----------------SORTOWANIE-------------------------------")
new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,9,3]
new_list.sort()
print(new_list)
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.pop(1)
print(num_list)
