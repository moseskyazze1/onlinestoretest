name="moses"
print(name)
age =27

if age < 100:
    print("you are young")
    print("im inside the if statement")
elif age>100:
    print("that is awesome")
    print("im outside the if statement")

def sayHello():
    print("hello there")
    sayHello()

    #thiss is the array/list
    colors=["blue","yellow","green"]
    colors.append("pink")
    print(colors[1])

#dictionary
me={
    "age":27,
    "firstname":"moses",
    "lastname": "ky",
}
print(me)
#modify
me["age"]


#creater a calculartor

def printMenu():
    print("[1] Sum")
    print("[2] Multiplication")
    print("[3] Subtract")
    print("[4] Division")

# Call the function to print the menu options
printMenu()

# Get user input for menu selection
opt = input("Select an option: ")

# Check if the input is a valid option (1, 2, 3, or 4)
if opt in ['1', '2', '3', '4']:
    # Get user input for two numbers
    number1 = float(input("Please enter the first number: "))
    number2 = float(input("Please enter the second number: "))

    # Perform the selected operation based on the user's choice
    if opt == "1":
        total = number1 + number2
        print("The sum is:", total)
    elif opt == "2":
        total = number1 * number2
        print("The product is:", total)
    elif opt == "3":
        total = number1 - number2
        print("The difference is:", total)
    elif opt == "4":
        if number2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            total = number1 / number2
            print("The division result is:", total)
else:
    print("Invalid option selected. Please select 1, 2, 3, or 4.")
###

print ()