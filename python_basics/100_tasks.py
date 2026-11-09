import random

# Task 1

print("Welcome to Python!")

# Task 2

name = input("What is your name? ")
print(f"Hello, {name}!")

# Task 3

a = int(input())
b = int(input())
print(a + b)

# Task 4

a = int(input("Enter an integer: "))
if a % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Task 5

for x in range(1, 11):
    print(x)

# Task 6

question = None
while question != "finish":
    question = input()
print("Goodbye!")

# Task 7

list_a = ["orange", "apple", "pear"]
list_a.append("banana")
print(list_a)

# Task 8

liczby = [4, 7, 2, 10, 5]
suma = 0
for x in liczby:
    suma += x
print(suma)

# Task 9

word = input("Enter a word: ")
print(len(word))

# Task 10

current_year = 2026
year = int(input("What is your birthday year? "))
print(f"You are {current_year - year} years old this year")

# Task 11

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_list = [number_1, number_2, number_3]
biggest_number = 0
if number_1 > number_2 and number_1 > number_3:
    biggest_number = number_1
elif number_2 > number_1 and number_2 > number_3:
    biggest_number = number_2
else:
    biggest_number = number_3

# Task 12

for x in range(2, 21, 2):
    print(x, end=" , ")

# Task 13

word = input("Enter a word: ").lower()
if "a" in word:
    print("There is a letter A")
else:
    print("There is no letter A")

# Task 14

sentence = input("Enter a sentence: ")
sentence = sentence.replace("e", "*").replace("E", "*")
print(sentence)

# Task 15

scores = [4, 5, 3, 4, 5, 2]
average_score = sum(scores) / len(scores)

# Task 16

product = {"name": "plushie",
           "price": 5,
           "availability": True}
print(f"Product {product['name']} costs {product['price']} $.")

# Task 17

password = input("Enter a new password: ")
if len(password) < 8:
    print("Password is too short.")
else:
    print("Password created successfully.")

# Task 18

for x in range(1, 21):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

# Task 19

sentence = input("Enter a sentence: ")
reverse_sentence = sentence[::-1]
print(reverse_sentence)

# Task 20

while True:
    generated_number = random.randint(1, 10)
    user_number = int(input("Guess a number between 1 and 10."))
    if user_number == generated_number:
        print("You won!")
        break
    else:
        print(f"Try again! The number was {generated_number}.")
        continue

# Task 21

def calculate_square(number):
    return number ** 2
print(calculate_square(5))

# Task 22

def can_vote(age):
    if age >= 18:
        return True
    else:
        return False
print(can_vote(16))
print(can_vote(20))

# OR

def can_vote(age):
    return age >= 18

# Task 23

list_a = [1, 2, 3, 4, 5, 6, 7, 8]
def filter_odds(numbers):
    numbers = [number for number in numbers if number % 2 == 1]
    return numbers
list_b = filter_odds(list_a)

# Task 24

def find_common(list_1, list_2):
    list_3 = []
    for x in list_1:
        if x in list_2:
            list_3.append(x)
    return list_3
list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]
list_3 = find_common(list_a, list_b)

# OR

def find_common(list_1, list_2):
    return list(set(list_1) & set(list_2))
list_a = [1, 2, 3, 4, 5, 6]
list_b = [4, 5, 6, 7, 8, 9]
list_3 = find_common(list_a, list_b)

# Task 25

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

try:
    quotient = number_1 / number_2
    print(f"The result is {quotient}")
except ZeroDivisionError:
    print("You cannot divide by zero!")

# Task 26

try:
    number_1 = int(input("Enter the first number: "))
    number_2 = int(input("Enter the second number: "))
    quotient = number_1 / number_2
    print(f"The result is {quotient}")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("The input value has to be a number.")

# Task 27

while True:
    try:
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        quotient = number_1 / number_2
        print(f"The result is {quotient}")
        break
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        continue
    except ValueError:
        print("The input value has to be a number.")
        continue

# Task 28

with open("movies.txt", "w") as file:
        for x in range (0,3):
            movie = (input("What is your favourite movie?"))
            file.write(movie + "\n")
with open("movies.txt", "r") as file:
    print("\n Saved movies")
    print(file.read())


