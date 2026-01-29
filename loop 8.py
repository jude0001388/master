#ask a user to enter the height and width
height = int(input("Enter a height of a rectangle:"))
width = int(input("Enter a width of a rectangle:"))
for i in range(height):
    for j in range(width):
        print("*",end=" ")
    print()