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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You walk on the forest and see a bifurcation. So, what you do? Left or Right? Please write. ').lower()
if direction == 'right':
    print('Fall into a Hole. Game Over!!!')
elif direction == 'left':
    print('You are walking a straite path around the forest.')
    direction = input('Now, you arrived a lake. In this path, you have two choices: Swim or Wait. What to do now? Please write. ').lower()
    if direction == 'swim':
        print('Attacked by trout. Game over!!!')
    elif direction == 'wait':
        print('So, you wait and then see a boat. You get in into a boat and navigate across the lake. In the end, there is a empty house. So you enter on the house.')
        direction = input('Then you see three doors on your front. They have three different collors: blue, yellow and red. Make your choice... What door you open it? ').lower()
        if direction == 'red':
            print('Burned by fire. Game over!!!')
        elif direction == 'yellow':
            print('You win!!! You taked a beautiful treasure chest!')
        else:
            print('Eaten by beasts. Game over!!!')
