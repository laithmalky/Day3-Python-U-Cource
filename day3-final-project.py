print(''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')



print('Welcome to Treasure Island\n'
      'Your mission is to find the Treasure')

direction = input('You\'re at a cross road. where do you want to go?\n'
                  '   "Right" or "Left"   \n').lower()

if direction == "left":
    wait_boat = input('You come to a lake'
                      ' there is an island in the middle of the lake\n'
                      'Type "wait" for wait the boat.'
                      ' Type "swim" to swim across\n').lower()
    
    if wait_boat == "wait":
        door = input('You arrive at the island unharmed.\n'
                     ' There is a house with 3 doors.'
                     'One "red", one "yellow" and one "blue".\n'
                     ' Which color do you choose?\n').lower()
        
        if door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over!")
        elif door == "red":
            print("It's a room full of fire. Game Over!")
        else: 
            print("You typed a wrong color. Game Over!")

    elif wait_boat == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You typed a wrong text. Game over!")

elif direction == "right":
    print("You fell into a hole. Game Over.")
else:
    print("You typed a wrong text. Game Over!")
