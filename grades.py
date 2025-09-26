#Ask the user for the grade
grade = float(input("What is the grade percent? "))

#Figure out the letter associated with the grade
if grade >= 90:
    print("The grade is an A")
elif grade >=80:
    print("The grade is a B")
elif grade >= 70:
    print("The grade is a C")
elif grade >= 60:
    print("The grade is a D")
else:
    print("The grade is an F")

#Display the letter grade to the user at the end


