"""
In this activity, we are going to be learning about the debugger, and
then testing our debugging skills with some
practice problems. As you work through the problems, remove the
multiline comments around the problem you want to work on next, and add the multiline comments back to the previous problem so it's out of the way.
"""
"""""
# let's practice the debugger!
n = 5
for x in range(1, 11):
 print(str(x) + ' * ' + str(n) + ' = ' + str(n * x))
 """""
# a function example to use with the debugger
import random
def random_greeting(name):
 greetings = ["hi", "hello", "howdy", "what's up", "good morning"]
 greeting = random.choice(greetings)
 print(greeting + " " + name + "!")
random_greeting("Alberto")
random_greeting("Jonah")
random_greeting("Malcolm")
random_greeting("Ryder")

"""
# a warm up that shouldn't require the debugger
greeting = input("Hello, possible pirate! What's the password?)
if greeting in ["Arrr!"):
print("Go away, pirate.")
elif
print("Greetings, hater of pirates!")
"""
"""
# average calculation problem
num_tests = input("How many test scores would you like to average: ")
tests_sum = 0
for i in range(num_tests):
 new_test = int(input("What is the test score: "))
 tests_sum = new_test
print("The average is " + str(tests_sum/num_tests) + ".")
"""
"""
def add_underscores(word):
 new_word = "_"
 for i in range(len(word)):
 new_word = word[i] + "_"
 print(new_word)
phrase = "hello"
add_underscores(phrase)
"""
"""
def calculate_bmi(weight, height):
 return weight / (height ** 2)

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]
for patient in patients:
 weight, height = patients[0]
 bmi = calculate_bmi(height, weight)
 print("Patient's BMI is: " + str(bmi))
"""