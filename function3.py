# function to calculate total
def calc_total(num1,num2,num3):
    total = num1 + num2 + num3
    return total
#function to calculate average
def calc_avg(sum, number_of_numbers):
    average = sum/number_of_numbers
    return average

#function to sort and print numbers
def sort_nums(num1, num2, num3):
    num_list = [num1, num2, num3]
    num_list.sort()
print(sort_nums)

#main programs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
result = calc_total(num1,num2,num3)
print(result)
average=calc_avg(result,3)
print(average)