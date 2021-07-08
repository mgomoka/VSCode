print("Enter an integer and return the tens digit:")
inputFromUser = str(input())

if len(inputFromUser) >= 2:
    tensDigit = inputFromUser[(len(inputFromUser)-2)]
    print("The tens digit is " + tensDigit + ".")
else:
    print("NO TENS DIGIT PRESENT.")
