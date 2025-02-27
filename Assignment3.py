# 1). Data Types and Variables
#Task: Create a python program To convert Temprachures beetween Celsius and Fahrenhit. 

# Temperature Converter Program

def convert_temperature():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    
    # Get user's choice
    choice = input("Choose an option (1 or 2): ")
    
    if choice == '1':

        # Convert Celsius to Fahrenheit

        celsius = float(input("Enter temperature in Celsius: "))

        fahrenheit = celsius * 9/5 + 32

        print(f"{celsius} °C is equal to {fahrenheit:.2f} °F")

    elif choice == '2':

        # Convert Fahrenheit to Celsius

        fahrenheit = float(input("Enter temperature in Fahrenheit: "))

        celsius = (fahrenheit - 32) * 5/9
        
        print(f"{fahrenheit} °F is equal to {celsius:.2f} °C")
    else:
        print("Invalid choice. Please choose 1 or 2.")

# Run the program
if __name__ == "__main__":
    convert_temperature()

################################################################################################################

#2). String and String Operation
# Task :  Write a program that checks if a word is a Palindrome.


# Palindrome Checker Program
def check_palindrome():
    print("Palindrome Checker")
    
    # Get input from the user
    word = input("Enter a word: ").strip().lower()
    
    # Check if the word is a palindrome
    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Run the program
if __name__ == "__main__":
    check_palindrome()

###################################################################################################################

#3). Lists
#Task: Create a Program That takes a list of integers and returns the largest number in the list.

# Program to find the largest number in a list
def find_largest_number():
    print("Find the Largest Number")
    
    # Get a list of integers from the user
    try:
        numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
        
        # Check if the list is not empty
        if not numbers:
            print("The list is empty. Please provide some numbers.")
            return
        
        # Find the largest number
        largest_number = max(numbers)  # Using max() function
        print(f"The largest number in the list is: {largest_number}")
        
        # Alternatively, use a loop to find the largest number
        # largest_number = numbers[0]
        # for num in numbers:
        #     if num > largest_number:
        #         largest_number = num
        # print(f"The largest number in the list is: {largest_number}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the program
if __name__ == "__main__":
    find_largest_number()

##############################################################################################################

# 4). Tuple
#Task: Write a program that swaps the first and last element of a tuple.

# Program to swap the first and last elements of a tuple
def swap_first_last_elements():
    print("Swap First and Last Elements of a Tuple")
    
    # Get input tuple from the user
    try:
        input_tuple = tuple(map(int, input("Enter the elements of the tuple separated by spaces: ").split()))
        
        # Check if the tuple has at least two elements
        if len(input_tuple) < 2:
            print("The tuple must have at least two elements to swap.")
            return
        
        # Swap the first and last elements
        swapped_tuple = (input_tuple[-1],) + input_tuple[1:-1] + (input_tuple[0],)
        print(f"Original tuple: {input_tuple}")
        print(f"Swapped tuple: {swapped_tuple}")

    except ValueError:
        print("Invalid input. Please enter integers only.")

# Run the program
if __name__ == "__main__":
    swap_first_last_elements()

###############################################################################################################

#5). Dictionaries
#Task: Write a program that counts the frequency of words in a sentences.

# Program to count the frequency of words in a sentence
def count_word_frequency():
    print("Word Frequency Counter")
    
    # Get a sentence from the user
    sentence = input("Enter a sentence: ").strip().lower()
    
    # Split the sentence into words
    words = sentence.split()
    
    # Create a dictionary to store word frequencies
    word_frequency = {}
    
    # Count the frequency of each word
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    # Display the word frequency dictionary
    print("Word frequencies:")
    print(word_frequency)

# Run the program
if __name__ == "__main__":
    count_word_frequency()

##################################################################################################################

#6).Sets 
#Task: Write a program to find the intersection of two sets.

def find_intersection(set1, set2):
    # Use the intersection method to find common elements
    intersection = set1.intersection(set2)
    return intersection

# Input sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

# Find intersection
result = find_intersection(set1, set2)

# Output the result
print("The intersection of the sets is:", result)

####################################################################################################################

#7). If/Else Statement
#Task: Create a program that determines whether a given number is positive , Negetive , or zero.

def check_number(num):
    # Check if the number is positive, negative, or zero
    if num > 0:
        print("The number is Positive.")
    elif num < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

# Input: Get a number from the user
number = float(input("Enter a number: "))

# Call the function to check the number
check_number(number)

######################################################################################################################

#8). Loops
#Task: Write a program that calculates the sum of all even numbers from 1 to a given number.

# Get input from the user
n = int(input("Enter a number: "))

# Initialize the sum
even_sum = 0

# Loop through all numbers from 1 to n
for i in range(1, n + 1):
    # Check if the number is even
    if i % 2 == 0:
        even_sum += i

# Print the result
print(f"The sum of all even numbers from 1 to {n} is {even_sum}.")

####################################################################################################################

#9). Functions
#Task: Write a function that takes a list of numbers and returns the avrages of the list.

def calculate_average(numbers):
    # Calculate the sum of the numbers and the number of elements
    total = sum(numbers)
    count = len(numbers)
    
    # Calculate the average
    average = total / count
    
    return average

# Example usage
numbers = [2, 4, 6, 8, 10]
average = calculate_average(numbers)
print(f"The average of the numbers is {average}.")

##########################################################################################################################

#10). List Comprehension
#Task: Write a program that generates  List of sqares of number from 1 to 10 using list comprehension.

# Using list comprehension to generate squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Print the result
print(squares)

##########################################################################################################################

#11). Lambda Function 
# Task: Create a program that sorts a list of tuples by the second element using a lambda function.

# Input: List of tuples
tuples_list = [(1, 2), (3, 1), (5, 4)]

# Sorting using a lambda function
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Output the sorted list
print("Sorted list:", sorted_list)


# Input list of tuples
tuples_list = [(1, 2), (3, 1), (5, 4)]

# Sorting the list by the second element of each tuple
sorted_list = sorted(tuples_list, key=lambda x: x[1])

# Output the sorted list
print("Sorted list:", sorted_list)

##################################################################################################################################

#12). Exception Handling
#Task: : Write a program that handles a division by zero error.













#####################################################################################################################################

#13). File handling
#Task: : Write a program that reads a text file and counts the number of lines and words.












#####################################################################################################################################

#14). Classes & Object
#Task: Create a class Car with attributes like make, model, and year. 
#Add methods to display the car's information and to calculate the car's age.

from datetime import datetime

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Information:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}")

    def calculate_age(self):
        current_year = datetime.now().year
        age = current_year - self.year
        return age


# Instantiate a Car object with specific values
my_car = Car("Toyota", "Corolla", 2015)

# Display the car's information
my_car.display_info()

# Calculate and display the car's age
car_age = my_car.calculate_age()
print(f"The car is {car_age} years old.")

###############################################################################################################

#15). Modules & libraries
#Task: Create a Python program that uses the math library to calculate the factorial of a given number.

import math

# Function to calculate factorial
def calculate_factorial(n):
    return math.factorial(n)

# Input: A number n
try:
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Output: The factorial of n
        result = calculate_factorial(n)
        print(f"The factorial of {n} is: {result}")
except ValueError:
    print("Please enter a valid integer.")



#################################################################################################################

#16). Recursion
#Task: Write a recursive function to calculate the factorial of a number.

# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

# Input: A number n
try:
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Output: The factorial of n
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")
except ValueError:
    print("Please enter a valid integer.")

####################################################################################################################

#17). Regular Exprestions
#Task: Write a program to check if a given string is a valid email address using a regular expression.

import re

# Function to validate email address
def is_valid_email(email):

    # Regular expression pattern for a valid email address
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email) is not None

# Input: A string
email = input("Enter an email address: ")

# Output: Check if the string is a valid email
if is_valid_email(email):
    print(f"'{email}' is a valid email address.")
else:
    print(f"'{email}' is NOT a valid email address.")


##################################################################################################################

#18). Working with Dates & Times
#Task:  Write a program that displays the current date and time in the format: YYYY-MM-DD HH:MM:SS.

import datetime

x = datetime.datetime.now()

print(x) 

###################################################################################################################

#19). Decorators
# Task: Write a decorator that measures the time taken to execute a function.







#######################################################################################################################

#20). Web Screping
#Task: Use the requests and BeautifulSoup libraries to scrape the titles of articles from a website (e.g., a news website).











