s = input()

s = s.lower()

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for i in s:
    if i in vowels:
        count += 1

print("Number of vowels:" , count)