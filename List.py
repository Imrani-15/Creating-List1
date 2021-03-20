# Using extend function
list = [10,'uma','naga',30,40]
print("\n Initial list:")
print(list)

# addition of multiple elements to the list at the end using extend method
list.extend([5,'durga','geeks',15])
print("\n list after perfoming extend operations:")
print(list)

# using index of the list
l1 = [15,22,55,21,62]
# accessing a element from the list using index number
print(l1[2])
print(l1[3])
print(l1[0])

#creating a multi demensional list by using  nested a list inside a list
l2 = [['guntur','andhra','hyd'],['goa','karnataka']]
# accessing a element from the multidemsional list using index numbers
print("\n acessing a element from the a multi dimensional list")
print(l2[0][2])
print(l2[1][0])

#negative indexing

List1 = [1, 11.01, 'dog', 'donk_john', True]
print("Accessing element using negative index")
print(List1[-1])
print(List1[-4])

# Remove element from the list
list1 = []
for i in range(0,10):
    list1.append(i)
print(list1)
# Removing elements from list using remove() method
list1.remove(9)
list1.remove(5)
print("\n list after remove of two elements")
print(list1)

# Removing element from list using iterator method
for i in range(0,4):
    list1.remove(i)
print("\n list after removing a range of elements:")
print(list1)

# Remove element from the list by using pop() function
li = [1,2,3,4,5]
print("\n Initial list:")
print(li)
# using a pop method and remove the element form the list
li.pop()
print("\n list after popping an element:")
print(li)

# Removing element at a specific location from the set using the pop() method
li.pop(0)
print("\n list after popping a spicific elements:")
print(li)

# using slicing of list
sli = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("\n Initial List:")
print(sli)

sliced_list = sli[2:5]
print("\n slicing element in the range of 2-5:")
print(sliced_list)

sliced_list = sli[:]
print("\n printing all elements using slice operation:")
print(sliced_list)

sliced_list = sli[::-1]
print("\n printing all elements display reverse using slice operation:")
print(sliced_list)





