def reverseRecursion(given_string):

    stringLen = len(given_string)

    if stringLen == 1:
        return given_string
    else:
        return reverseRecursion(given_string[1:]) + given_string[0]

givenstring = input("Please Enter string: ")
print('The original given string:', givenstring)
print('The provided string was modified After reversing:', reverseRecursion(givenstring))