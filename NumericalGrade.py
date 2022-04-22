#Numerical Grade Calculator

#User Info
name = input("What is your name: ")
print("Hello " + name + "!" )
grade = int(input("What numerical percentage did you receive?: "))


if grade >= 93 and grade <= 100:
    print("Congratulations " + name + "!" " Your Grade is A!")
elif grade >= 85 and grade <= 92:
    print("Nice Job " + name + "!" " Your Grade is B!")
elif grade >= 77 and grade <= 84:
    print("Pretty average " + name + "." " Your Grade is C.")
elif grade >= 70 and grade <= 76:
    print("Well, it looks like you've passed " + name + "." " Your Grade is D.")
elif grade>=0 and grade <=69:
    print("Sorry " + name + "," " you have failed"  "." " You have received a F.")