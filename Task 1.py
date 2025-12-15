import random
from collections import Counter


choices = ['rock', 'paper', 'scissors']
user_history = []


def get_ai_choice():
if len(user_history) < 3:
return random.choice(choices)
most_common = Counter(user_history).most_common(1)[0][0]
if most_common == 'rock':
return 'paper'
elif most_common == 'paper':
return 'scissors'
else:
return 'rock'


print("--- Smart Rock Paper Scissors AI ---")


while True:
user_choice = input("Enter rock, paper, scissors (or quit): ").lower()
if user_choice == 'quit':
break
if user_choice not in choices:
print("Invalid input")
continue


user_history.append(user_choice)
ai_choice = get_ai_choice()
print(f"AI chose: {ai_choice}")


if user_choice == ai_choice:
print("It's a tie")
elif (user_choice == 'rock' and ai_choice == 'scissors') or \
(user_choice == 'paper' and ai_choice == 'rock') or \
(user_choice == 'scissors' and ai_choice == 'paper'):
print("You win")
else:
print("AI wins")