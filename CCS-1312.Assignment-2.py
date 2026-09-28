def Info(Name):
    #To take the name from the user
    Name = input("Enter your name: ")
    #To take the age from the user
    Age = input("Enter your age: ")
    #To take the email from the user
    Email = input("Enter your email: ")


    #Make the name variable uppercase
    NameUpper = Name.upper()
    #Convert the age variable from string to integer
    AgeInt = int(Age)
    #Make the email variable lowercase
    EmailLower = Email.lower()


    #Remove any extra spaces from the beginning and the end of the variable
    NameUpperStrip = NameUpper.strip()
    # Remove any extra spaces from the beginning and the end of the variable
    EmailLowerStrip = EmailLower.strip()


    #To print the full name and the email after the changes, and print the age and the length of the full name
    print("\nYour name is:", NameUpperStrip,"\nYour age is:", AgeInt,"\nYour email is:", EmailLowerStrip,"\nThe number of letters in your name is :", len(NameUpperStrip))
    print("=" * 50)


print("=" * 20,"Welcome","=" * 20 )
#Variable to start the code
Start = 0
#To call the function
Call1 = Info(Start)

def Expenses(Lst, Mn, Mx):
    #To make a list of the expenses that the user enters
    Lst = [Expenses1, Expenses2, Expenses3, Expenses4]
    #Variable for the maximum value
    Mx = List[0]
    # Variable for the minimum value
    Mn = List[0]

    #Loop to detect which is the maximum value and the minimum
    for i in range(len(Lst)):
        if List[i] > Mx:
            Mx = List[i]
        elif List[i] < Mn:
            Mn = List[i]
    return Mn, Mx

#Variables for the Loop
Expenses1 = int(input("\nEnter your JAN expenses: "))
Expenses2 = int(input("Enter your FEB expenses: "))
Expenses3 = int(input("Enter your MAR expenses: "))
Expenses4 = int(input("Enter your APR expenses: "))

#Here we make the list
List = [Expenses1, Expenses2, Expenses3, Expenses4]
#Here we call the function
Mn, Mx = Expenses(List, list[0], list[0])

#Print the maximum and minimum value
print(f"\nThe maximum amount of expenses is:", {Mx})
print(f"The minimum amount of expenses is:", {Mn})

print("=" * 50)