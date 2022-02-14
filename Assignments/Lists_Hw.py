"""
INSTRUCTIONS

Below there are 6 problems that require you to write a function that will manipulate a list. For this assignment,
choose at least 3 out of 6. The problems get progressively more challenging as you go. Below the multiline comment
for a problem, write your solution and then make sure you call your function at least once to test it!

Try these on your own with what we've learned about lists and functions in class first! If you do have to use outside
sources, DON'T FORGET TO CITE THEM; otherwise it's plagiarism, and we'll have to have a conversation I don't want to have...
"""



"""
Problem 0:

Choose at least three things from lessons that other classmates taught and incorporate them into a function that has
at least one parameter that is a list, and that returns something meaningful.
"""


#def number_order():

"""
1. Create function
1.5. Create list
2. for i in range (5)
3. Add numbers to the list
4. Sort the list
5. Add the list together
6. Produce min and max
"""

"""

num_list = []
for i in range(5):
    num = input("Pick a number? ")
    num_list.append(num)
"""
"""
Problem 1:

Write a function called unique_append that will take in a list and an element to append as parameters.
If the element to append does not already exist in the list, it should append it to the list and return True.
If the element does exist in the list, it should not append it and return False. 
"""
"""
1. create the function with broad list, and element
2.   If elem in the list, return false
3.      else return true and append element to list

"""
"""
color_list = ["daisy", "rose", "tulip"]
def broad_list_function(flower_list):
    new = input("Name anything for my broad list of colors: ")
    if new in (color_list):
        print("thats already in there")
    else:
        new.append(color_list)
    print(color_list)
"""

"""
Problem 2:

Write a function called find_max that takes in a list as a parameter and returns the maximum value in the list.
Sorry.... but you're not allowed to use the max function.
"""
"""
1. def find_max(num_list)
2. current max = num_list[0]
3. for i in range(len(numlst)):
4.  if current_max < numlist[i]:
5.      current_max = numlist[i]
6. return current_max
7. nums = [1, 5, 10, 11,]
8. printfind_max(num_list)


"""
def find_max(num_list):
    current_max = num_list[0]
    for i in range(len(num_list)):
        if current_max < num_list[i]:
            current_max = num_list
    return current_max
num_list = [1, 4, 8, 12]
print(find_max(num_list))
"""
Problem 3:

Write a function called get_item that takes in a list and a (positive) index number as parameters. If the index number 
is not out of range for the given list, return the list item at that index. Otherwise, return None. 
"""


"""
Problem 4:

Write a function called list_overlap that takes in two lists as parameters. This function should return a list that 
contains all the list items that exist in both of the lists passed in. 
P.S. You shouldn't use any built in functions for this.
"""


"""
Problem 5:

Write a function called index_wise_sum that takes in two lists (of the same length) as parameters. This function 
should return a new list (also of the same length) where each element is the result of the sum of the elements at that
same position in the two lists that were passed as parameters. For example, if the two lists passed in were
[1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] then the list returned would be [7, 9, 11, 13, 15]. You can choose how your 
function should behave if the lists passed in are not the same length.
"""
