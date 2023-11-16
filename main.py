#TERM 1 RESULTS
Math1 = int(input("what is your score in math term 1? "))
AES1 = int(input("what is your score in AES term 1? "))
Physics1 = int(input("what is your score in physics term 1? "))
Computerprogramming1 = int(input("what is your score in Computer programming term 1? "))


#  Checking if the grades are between 0 and 100
if Math1 < 0 and AES1 < 0 and Physics1 < 0 and Computerprogramming1 < 0 :
    print("That is not a valid score")
elif Math1 > 100 and AES1 > 100 and Physics1 > 100 and Computerprogramming1 > 100 :
    print(" That is also not a valid score")
quit()

#TERM 2 RESULTS
Math2 = int(input("what is your score in math term 2? "))
AES2 = int(input("what is your score in AES term 2? "))
Physics2 = int(input("what is your score in physics term 2? "))
Computerprogramming2 = int(input("what is your score in Computer programming term 2? "))

#  Checking if the grades are between 0 and 100
if Math2 < 0 and AES2 < 0 and Physics2 < 0 and Computerprogramming2 < 0 :
    print("That is not a valid score")
elif Math2 > 100 and AES2 > 100 and Physics2 > 100 and Computerprogramming2> 100 :
    print(" That is also not a valid score")
quit()

#TERM 3 RESULTS
Math3 = int(input("what is your score in math term 3? "))
AES3 = int(input("what is your score in AES term 3? "))
Physics3 = int(input("what is your score in physics term 3? "))
Creativedesign= int(input("what is your score in creative design term 3? "))

#  Checking if the grades are between 0 and 100
if Math3 < 0 and AES3 < 0 and Physics3 < 0 and Creativedesign < 0 :
    print("That is not a valid score")
elif Math3 > 100 and AES3 > 100 and Physics3 > 100 and Creativedesign > 100 :
    print(" That is also not a valid score")
quit()

# Checking if the student progressed
TotalAverage = (Math1+AES1+Physics1+Computerprogramming1+Math2+AES2+Physics2+Computerprogramming2+Math3+AES3+Creativedesign)/12
MathAverage = (Math2+Math3)/2

# THIS CHECKS IF THEY SCORED AN AVERGRE OF 40% IN EACH SUBJECT
if Math1 < 40 and AES1 < 40 and Physics1 < 40 and Computerprogramming1 < 40 and Math2 < 40 and AES2 > 40 and Physics2 < 40 and Computerprogramming2 < 40 and Math3 < 40 and AES3 < 40 and Physics3 < 40 and Creativedesign < 40:
    print("Sorry, you didnt score the required grades for you to progress")

# THIS CHECKS FOR THE STUDENTS TOTAL AVERAGE
elif TotalAverage < 60 :
    print("Sorry, you did not pass")

# THIS CHECKS FOR THE STUDENTS AVERGRE IN MATH
elif MathAverage < 65 :
    print("sorry you did not pass")

# THIS CHECKS IF THE STUDENT SCORED AN AVERGRE OF 60% IN AES3
elif AES3 < 60 :
    print(" Sorry, you did not pass ")

else :
    print("CONGRATS!! YOU PASED")


# Prints Special Message
if TotalAverage == 100:
    print("WOW! GREAT JOB")

# QUIT!
quit()















#Failure if > 40%
if AES < 40 and math < 40 and physics < 40 and computerprogramming < 40:
    print(" Sorry, you failed ")





 #Overallscore

if AES >= 60 and math >= 60 and physics >= 60 and computerprogramming >= 60:
    print("Congrats, you progressed")



elif Math2 and Math3 >= 65:
    print("wow")

elif AES3 >= 60:
    print(" good")
else:
    print(" you progressed, congrats")






















