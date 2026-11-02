environments = ["DEX", "TEST", "UAT"]
print(environments)
print(environments[0])
print(environments[1])
print(environments[2])

for environment in environments:
    print(environment + " from loop")

# Task 1

list_1 = [x for x in range (6)]

# Task 2

list_2 = [x for x in range (1, 11)]

# Task 3

list_3 = [x ** 2 for x in range (1, 6)]

# Task 4

list_4 = [x for x in range (1, 11) if x % 2 == 0]

# Task 5

list_5 = [x for x in range (1, 11) if x % 2 == 1]

# Task 6

list_6 = [x for x in range (0, 21) if x % 5 == 0 and x != 0]

# Task 7

list_7 = [[x, y] for x in range (0, 2) for y in range (0, 2)]

# Task 8

list_8 = [[x, y] for x in range (0,3) for y in range (0, 3) if x + y != 2]

# Task 9

list_9 = [user[0] for user in users]

# Task 10

list_10 = [user[0] for user in users if user[1] > 23]

# Task 11

list_11 = [fruit[0] for fruit in shop if fruit[1] == 3.50]

# Task 12

list_12 = [present_student[0] for present_student in attendance if present_student[1] == True]

# Task 13

list_13 = [it_staff[0] for it_staff in staff if it_staff[1] == "IT"]

# Task 14

target_height = int(input())
list_14 = [player[0] for player in players if player[1] == target_height]

# Task 15

worst_rating = 3.5
list_15 = [product[0] for product in products if product[1] <= worst_rating]

# Task 16

list_16 = [city[0].capitalize() for city in cities if city[1] == "France"]

# Task 17

target_animal = "dog"
list_17 = [animal_class[1] for animal_class in animals if animal_class[0] == target_animal]

# Task 18

top_score = 85
list_18 = ["Laureat: " + top_students[0] for top_students in exams if top_students[1] == top_score]