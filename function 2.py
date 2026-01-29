#functions to calculate the total of three numbers
def calc_total(number1,number2,number3):
#add the three numbers and store the result in total
    total = number1 + number2 + number3
# return the three numbers to the main program
    return total



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

#call the calc_total function and pass the three entered numbers
result = calc_total(num1,num2,num3)
print(result)