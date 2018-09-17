# Basic practice on first day.
# Print name and age
print("hello there")
name = "ed"
number = 25
print(name, number)


# Simple converter (KM to Miles)
distance = input("\nEnter your distance in Km:\n")
dis = float(distance)
miles = 0.6214
print("converted into miles is", dis*miles)


# Getting student average out of 3 subjects
studentFirstName = input("\nEnter your first name:\n")
studentSecondName = input("\nEnter your second name:\n")
grade1 = int(input("Enter your first subject"))
grade2 = int(input("Enter your second subject"))
grade3 = int(input("Enter your third subject"))
average = grade1+grade2+grade3/3
print(studentFirstName, studentSecondName, "your average is ", average)


# Calculating someones BMI
weight = float(input("\nEnter your weight(in pounds) :\n"))
height = float(input("\nEnter your height(in inches):\n"))
square = height*height
bmi = (weight/square)*703
print(bmi)

# Getting basic total of tickets
ticketA = int(input("\nEnter number of tickets sold in A :\n"))
ticketB = int(input("\nEnter number of tickets sold in B :\n"))
ticketC = int(input("\nEnter number of tickets sold in C :\n"))
priceA = 25
priceB = 20
priceC = 30
total = ticketA*priceA + ticketB*priceB + ticketC*priceC
print(total)



