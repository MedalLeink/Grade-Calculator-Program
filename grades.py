#Ask the user for the grade
grade = float(input("What is the grade percent? "))

letter = ""

#Figure out the letter associated with the grade
if grade >= 90:
    # print("The grade is an A")
    letter = "A"
elif grade >=80:
    # print("The grade is a B")
    letter = "B"
elif grade >= 70:
    # print("The grade is a C")
    letter = "C"
elif grade >= 60:
    # print("The grade is a D")
    letter = "D"
else:
    # print("The grade is an F")
    letter = "F"


#Get the last digit
last_digit = grade % 10

#Determine the sign
 

#Display the letter grade to the user at the end
print(f"You have earned the grade {letter}")

if grade >= 70:
    print("Congratulations! You have passed the course.🥳")
else:
    print("Sorry, please try the course again.")

