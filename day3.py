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



height = int(input("What is your height in CM? "))
bill = 0

if height >= 120 : 
    print("You can play the game :)")
    age = int(input("Whats your age? "))
    if age <= 12:
        print("Child tickets are $5 USD!")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7 USD!")
        bill = 7
    elif 45 <= age <= 55: # Its the same of but with less words better for effecint age >= 45 and age <= 55
        print("everything gonna be fine! have a free ride on us ")
    else:
        print("Adult tickets are $12 USD!")
        bill = 12

    photo = input("Do you wanna pick a photo? Press Y for yes and N for No!")
    if photo == "Y" or photo == "y":
        # add 3 usd to the bill
        bill += 3 
    
    print(f"Your bill is ${bill}!")

else :
    print("For sadly you cant play the Game :(") 



# > bigger
# < smaller
# >= bigger or equail
# <= smaller or equail
# == equail to 
# != not equail to



# odd or even task

number = int(input("enter a number! "))

if number % 2 == 0 :
    print("This number is even")
else :
    print("This number is odd")

