"""
Functions Practice

** Functions with no parameters and no return value **
1.  Write a function called dice_roll that will print the result of one random 6-sided dice roll.
2.  Write a function called tell_me_a_joke that will randomly generate a joke and print it.
3.  Write a function called current_date_and_time that will print out the current date and time
    in a nicely formatted way.
"""
"""
#1.
import random

def diceroll():
    print(random.randint(1,6))
diceroll()
"""
"""
#2.
import random

def joke_list():
    joke = ["What do you call a cow with no legs? ground beef.", "Where are cows from? Moo Zealand"]
    print(random.choice(joke))
joke_list()
"""

"""
** Functions with parameter(s), but no return value **
1.  Write a function called is_even that will accept a number as a parameter.
    It should print out "even" if the function is even, and "odd" if it is odd.
2.  Write a function called max that will accept three numbers as parameters.
    It should find the max of the three numbers and print it out.
3.  Write a function called list_sum that will accept a list of numbers as a parameter.
    It should sum up all the numbers in the list and print the sum.

"""
"""
def max(num_1,num_2,num_3):
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_1 and num_2 > num_3:
        return num_2
    else:
        return num_3
max(5, 7, 10)
"""
"""
def max(x,y,z):
    nums = [x,y,z]
    nums.sort()
    print(nums[-1])
"""
"""
** Functions with parameter(s) and a return value **
1.  Write a function called in_range that will check whether or not a number falls within a range.
    The function should return True if it does, and False if it does not.
    The function should accept three parameters: the first is the number, the second is the lowest value
    of the range, and the third is the highest value of the range.
2.  Write a function called find_evens that will accept a list of numbers as a parameter.
    The function should loop through the list and determine if each number is even. If it is, add it to a new list
    of only even numbers. Return the list of even numbers.
3.  Write a function called is_palindrome that will accept a string and return True if it is a palindrome,
    and False if it is not.
"""
def is_palindrome():
    entered = input("Enter a palindrome ")
    palindrome = ["racecar", "mom", "dad",]

"""
If you're finished, look up and read about what default parameters are. Then try one of the following function
challenges with default parameters:

1.  Write a function called greet_me that requires a name as a parameter, and has an optional greeting as a parameter.
    If a greeting is not passed, the function will greet the person with Hello. If a greeting is passed, it
    will use that greeting instead.
2.  Write your own function using a good use case for default parameters :)
"""