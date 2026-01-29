mark = int(input("What was the student's assessment mark (0-100)"))
if 0 <= mark <= 39:
    grade = "f"
elif 40 <= mark <= 49:
    grade = "d"
elif 50 <= mark <= 59:
    grade = "c"
elif 60 <= mark <= 69:
    grade = "b"
elif 70 <= mark <= 100:
    grade = "a"
else:
    print("Please enter a number between 0 and 100")