from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list0 = [rock, paper, scissors]
list1 = ['rock', 'paper', 'scissors']
choice = input("Please make a choice: rock, paper or scissors. ").lower()
if choice == 'rock':
  print(f"Your choice is:\n{rock}")
elif choice == 'paper':
  print(f"Your choice is:\n{paper}")
else:
  print(f"Your choice is:\n{scissors}")

number = int(randint(0, 2))
list_random = list0[number]
print(f"Computer choice is:\n{list_random}")

if choice == list1[number]:
  print('Draw game')
elif choice == 'rock' and list1[number] == 'paper':
  print('Ohhhhhh, so sad... You\'re lose!')
elif choice == 'rock' and list1[number] == 'scissors':
  print("Congratulations! You're a winner!!!")
elif choice == 'paper' and list1[number] == 'scissors':
  print('Ohhhhhh, so sad... You\'re lose!')
elif choice == 'paper' and list1[number] == 'rock':
  print("Congratulations! You're a winner!!!")
elif choice == 'scissors' and list1[number] == 'rock':
  print('Ohhhhhh, so sad... You\'re lose!')
elif choice == 'scissors' and list1[number] == 'paper':
  print("Congratulations! You're a winner!!!")
