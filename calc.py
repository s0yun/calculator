#while loop to ensure a calc function is selected
while True:
    print("Please choose: 1 - Addition 2 - Subtraction 3 - Multiplication 4 - Division: ")
    calctyp = input()
    try:
        calctyp = int(calctyp)
        if calctyp not in [1,2,3,4]:
            raise ValueError
    except ValueError:
        print("Please use 1-4 to choose your calculator function")
        continue
    else:
        break

#Get user inputs
print("This calculator supports floating point numbers")
number1 = input("First number:  ")
number2 = input("Second number:  ")

#Select method and run
if calctyp == 1: 
    print("You've chosen addition")
    answer = float(number1) + float(number2)
    print("Your sum was "+ number1 + " plus  " + number2)
elif calctyp == 2:
    print("You've chosen subtraction")
    answer = float(number1) - float(number2)
    print("Your sum was "+ number1 + " minus " + number2)
elif calctyp == 3:
    print("You've chosen mulitplication")
    answer = float(number1) * float(number2)
    print("Your sum was "+ number1 + " multiplied by " + number2)
elif calctyp == 4:
    print("You've chosen division")
    answer = float(number1) / float(number2)
    print("Your sum was " +  number1 + " divided by " + number2)
else:
    print("Incorrect input, exiting")
print("Your answer is " + str(answer))