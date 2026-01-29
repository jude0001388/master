#student grade program
#ask for student score
marks = int(input("enter your marks: "))
if marks <=39:
    grade = "f"
elif marks <=49:
    grade = "d"
elif marks <=59:
    grade = "c"
elif marks <=69:
    grade = "b"
else:
    grade = "A"
print (grade)
