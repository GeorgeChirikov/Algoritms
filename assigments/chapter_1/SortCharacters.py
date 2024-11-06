# read input from user
inputString = input("Enter a string: ")
resultString = ""
inputStringUnicodeArray = []

# sort the string by unicode
def sort_by_unicode(inputstring):
    sorted_string = sorted(inputstring)
    resultString = ''.join(sorted_string)
    print(resultString)


# check character's unicode
def check_unicode(inputstring):
    for char in inputstring:
        inputStringUnicodeArray.append(ord(char))


sort_by_unicode(inputString)

check_unicode(inputString)
print(inputStringUnicodeArray)