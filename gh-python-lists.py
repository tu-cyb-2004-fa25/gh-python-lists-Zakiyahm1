# in-class exercise for Lecture 03 List

# 1. Fill in the missing code to produce the output: ['honda', 'yamaha', 'suzuki', 'kawasaki']
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
#<<insert your missing code here>>
motorcycles[-1] = 'kawasaki'
print(motorcycles)


# 2. Please double each element in the list 
my_list = [1, [4, 6, 12], 7, 8]
#<<insert your missing code here>>
print(my_list * 2)

# 3. Fill in the code to produce the following output:  [3, 6, 99, 45, 29, 34] 
#    You can insert multiple lines of code, obtain target_list based on list1 and list2
list1 = [3,6,99,12]
list2 = [64,45,29,34]
#<<Insert your code here>>
target_list = list1 + list2
target_list.remove(12)
target_list.remove(64)
print(target_list)

# Try it yourself exercise
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit
# (1) Store the locations in a list
visit_later = ['Tokyo','Barcelona','Vancouver','Beijing','Orlando']

# (2) Print your list in its original order
print(visit_later)

# (3) Print your list in alphabetical order without modifying the actual list
temp_good = sorted(visit_later)
print(temp_good)

# (4) Show that your list is still in its original order by printing it
print(visit_later)


# (5) Change the order of your list in reverse order and print it
visit_later.reverse()
print(visit_later)

# (6) Change your list so it’s stored in reverse-alphabetical order, and print it 
visit_later.sort()
visit_later.reverse()
print(visit_later)

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive. 
for numbers in range(1, 21):
    print(numbers)

# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list. 
multiples_3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
for multiples_3 in multiples_3:
    print(multiples_3)

# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube. 
cubed_numbers = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10,]
for number in range(1, 11):
    cubed_numbers = number ** 3
    print(cubed_numbers)
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes = [nums ** 3 for nums in range(1, 11)]
print(cubes)

# in-class code
import copy

list1 = [1, 2, 3, 4, ["a", "b"]]
list2 = list1 
list3 = list1[:]
list4 = list1.copy()
list5 = copy.copy(list1) 
list6 = copy.deepcopy(list1) 

list2.append(5)
list3[4].append("c") 
list4[0] = 100
list5[4][-1] = "w" 
list6[-1].append("c")

'''
# discuss the answers befor runing the following code
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")
print(f"list4: {list4}")
print(f"list5: {list5}")
print(f"list6: {list6}")
'''