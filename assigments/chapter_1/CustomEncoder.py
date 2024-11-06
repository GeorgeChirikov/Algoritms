
def custom_encoder(inputString):
    positionList = []
    referenceString = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(inputString)):
        inputString = inputString.lower()
        if inputString[i] in referenceString:
            positionList.append(referenceString.index(inputString[i]))
        else:
            positionList.append(-1)
    return positionList


print(custom_encoder("My house is beautiful")) # [12, 24, -1, 7, 20, 18, 4, -1, 8, 18, -1, 1, 0, 19, 5, -1, 1, 2, 21, 20, 9, 6, 21, 12]