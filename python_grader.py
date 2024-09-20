points_possible = int(input("What is the maximum amount of points possible?  "))
points_achieved = int(input("What are the points achieved?  "))
student_name = str(input("What is the student's name (optional):  "))

if not student_name == "Drew": #This is just a fun little joke
    if points_achieved / points_possible <= 50 / points_possible: 
        #The a/b <= 50/b is basically the percent compared to the desired percent
        print("The grade is an F!")
    elif points_achieved / points_possible <= 60 / points_possible:
        print("The grade is a D!")
    elif points_achieved / points_possible <= 75 / points_possible:
        print("The grade is a C!")
    elif points_achieved / points_possible <= 88 / points_possible:
        print("The grade is a B!")
    elif points_achieved / points_possible <= 100 / points_possible:
        print("The grade is an A!")
else:
    print("This student deserves an A!")
