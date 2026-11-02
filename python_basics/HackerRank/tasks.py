# Task 1

n = int(input().strip())

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")

# Task 2

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)


# Task 3

a = int(input())
b = int(input())

print(a // b)
print(a / b)

# Task 4

n = int(input())
for i in range (n):
    if i < n:
        print(i ** 2)

# Task 5

def is_leap(year):
    leap = False
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = int(input())
print(is_leap(year))

# Task 6

n = int(input())

for i in range(1, n + 1):
    print(i, end="")

# Task 7

x = int(input())
y = int(input())
z = int(input())
n = int(input())

lista_ijk = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if i + j + k != n]

print(lista_ijk)

# Task 8

n = int(input())
arr = map(int, input().split())
unique_scores = set(arr)
sorted_scores = sorted(list(unique_scores))
print(sorted_scores[-2])

# Task 9

records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])
scores = []
for record in records:
    scores.append(record[1])
sorted_unique = sorted(set(scores))
second_lowest = sorted_unique[1]
names = [record[0] for record in records if record[1] == second_lowest]
names.sort()
for name in names:
    print(name)

# Task 10

