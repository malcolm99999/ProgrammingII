"""
The user will enter a number, and we will tell them whether or not it is prime.
Author: Ms. Ifft
"""

# take an input from the user
# number = int(input("Please enter your number: "))

# prime = True
#
# # check if it's divisible by 2
# if number % 2 == 0:
#     print("This is not prime.")
#     prime = False
# else:
#     # loop through numbers up to input divided by 2
#     for i in range(3, number, 2):
#         # check if it's divisible by current number (if it is, we're done)
#         if number % i == 0:
#             print("This is not prime.")
#             prime = False
#             break
#
# # if at end of loop there is no factor, print that it's prime
# if prime:
#     print("This number is prime.")

# is_prime will return True if number is prime, and False if it is not
def is_prime(number):

    # check if it's divisible by 2
    if number % 2 == 0:
        print("This is not prime.")
        return False

    # loop through numbers up to input divided by 2
    for i in range(3, number, 2):
        # check if it's divisible by current number (if it is, we're done)
        if number % i == 0:
            print("This is not prime.")
            return False

    # if at end of loop there is no factor, print that it's prime
    print("This number is prime.")
    return True

is_prime(int(input("Please enter your number: ")))
