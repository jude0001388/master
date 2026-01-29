#ask the user to enter a number
numbers = []
for i in range(1,6):
    num = int(input("Enter a number:"))
    numbers.append(num)

lowest = min(numbers)
highest = max(numbers)
print(lowest)
print(highest)