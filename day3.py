# if else 
print("Welcome to the Game!")
height = int(input("What is your height in CM? "))

if height >= 120 : 
    print("You can play the game :)")
    age = int(input("Whats your age? "))
    if age >= 18:
        print("You have to pay $12 U.S.D. for a ticket!")
    elif age <= 12:
        print("You have to pay $5 U.S.D. for the ticket!")
    else:
        print("You have to pay $7 U.S.D. for a ticket!")
else :
    print("For sadly you cant play the Game :(") 


# > bigger
# < smaller
# >= bigger or equail
# <= smaller or equail
# == equail to 
# != not equail to



# odd or even task

number = int(input("enter a number!"))

if number % 2 == 0 :
    print("This number is even")
else :
    print("This number is odd")

