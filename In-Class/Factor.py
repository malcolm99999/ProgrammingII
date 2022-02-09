"""
This program will ask the user for a number to factor and print out all the sorted numbers.
Repeat as much as they can
"""


# Get the factors for a user number and returns them as a sorted list
def factors(number):
    final_factors = [number]
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:  # i is a factor of number
            final_factors.append(i)
            #final_factors.append(number / i)

    final_factors.sort(reverse=True)
    print(final_factors)

while True:
    user_number = int(input("Please enter a number "))
    factors(user_number)