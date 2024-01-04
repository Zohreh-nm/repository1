import random

choices = ['s', 'r', 'p']

choice_meaning = {
    's' : 'scissors',
    'r' : 'rock',
    'p' : 'paper',
}

user_score = 0
ai_score = 0

for i in range(5):
    user_choice = input('Enter your choice (scissor, rock, paper): ')
    
    ai_choice = random.choice(choices)
    
    if user_choice in choices:
        print(f'your choice is {choice_meaning[user_choice]}, ai_choice is {choice_meaning[ai_choice]}')
        if user_choice == ai_choice:
            print('Tie')
        elif user_choice == 'r' and ai_choice == 's':
            print('You got it!')
            user_score += 1
        elif user_choice == 's' and ai_choice == 'p':
            print('You got it!')
            user_score += 1
        elif user_choice == 'p' and ai_choice == 'r':
            print('You got it!')
            user_score += 1
        else:
            print('You missed it')
            ai_score += 1
    else:
        print('Invalid input!')
        
    print(f'user score: {user_score}/ ai score:{ai_score}')
    
    print('-' * 20)
    
if user_score > ai_score:
    print(f"User won the game. User Score:{user_score} | AI Score:{ai_score}")
elif user_score < ai_score:
    print(f"Ai won the game. User Score:{user_score} | AI Score:{ai_score} ")
else:
    print(f"Tie! User Score:{user_score} | AI Score:{ai_score}")
            
            
        