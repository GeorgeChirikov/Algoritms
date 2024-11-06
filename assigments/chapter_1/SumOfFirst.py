number = int(input())
og_number = number

for i in range(1, number):
    number += i

print(f"The sum of the first {og_number} positive integers is {number}")
