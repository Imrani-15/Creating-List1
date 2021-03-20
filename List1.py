# Pratice on List Methods
# Creating a list
# Creating a empty list
List = []
print('Blank list')
print(List)

# Creating a number of list
List1 = [10,20,30,40]
print("\n List of numbers")
print(List1)

# Creating a list of strings and accessing using a index
List2 = ["apple", "grapes", "papaya"]
print("\n List of items")
print(List2[1])
print(List2[2])

# Creating a nested list inside a list
List3 = [["pg","college"],["school"]]
print("\n Nested list inside a list:")
print(List3)

# Knowing size of the list
# Creating a empty list
list = []
print(len(list)) #0

# creating a number of list
list1 = [10,20,30,40,50]
print(len(list1)) #4

#Adding a element to a list

Add = []
print("Initial blank list:")
print(Add)

# Using a append function and addition of elements in the list
Add.append(20)
Add.append(30)
Add.append(40)
print("\n Add after addition of three elements:")
print(Add)

# Adding element of the list using iterator
List_itr = []
for i in range(1,6):
    List_itr.append(i)
print("\n list after addition of elements from 1-5")
print(List_itr)

# Adding tuples to the list
List_itr.append((5,6))
print("\n List after Addition of a tuple:")
print(List_itr)

# Addition of list to a list
L_I = ['ink','pen']
Add.append(L_I)
print("\n list after addition of the list:")
print(Add)

# using a insert function
# creating a list
L1 = [1,2,3,4,5,6]
print("\n Initial list:")
print(L1)

# Addition of element at specific position using insert method
L1.insert(4,20)
L1.insert(0,100)
print("\n list after performing insert operation:")
print(L1)

