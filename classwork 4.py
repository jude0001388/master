#ask the user for input
num = int(input("Enter a number greater than 1: "))
total = 0
for i in range(1, num + 1):
    total += i
print(total)