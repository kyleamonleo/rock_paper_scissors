import random
from paper import Paper
from rock import Rock
from scissors import Scissors

options = set[Paper, Rock, Scissors]

def random_option(list):
    for i in random.randint(len(list)):
        p = list[i]

    return p

def same():
    print('SAME CHOICE')

def win_checker(my_option, rand_option):
    user_score, bot_score= 0,0
    if my_option == Paper:
        if rand_option == Rock:
            Paper.beats_rock()
            user_score=+1
            print("PLAYER WINS")
        
        elif rand_option == Scissors:
            Scissors.beats_paper()
            bot_score=+1
            print("PLAYER LOSE")
        else:
            same()

    
    elif my_option == Rock:
        if rand_option == Paper:
            Paper.beats_rock()
            bot_score=+1
            print("PLAYER LOSE")
        
        elif rand_option == Scissors:
            Rock.beats_scissor()
            user_score=+1
            print("PLAYER WINS")
        else:
            same()


    elif my_option == Scissors:
        if rand_option == Paper:
            Scissors.beats_paper()
            user_score=+1
            print("PLAYER WINS")
        
        elif rand_option == Rock:
            Rock.beats_scissor()
            bot_score=+1
            print('PLAYER LOSE')
        
        else:
            same()

    return user_score, bot_score


def get_user_input():

    user = ""
    while True:


        user = input("r - p - s? ")

        if user == 'r':
            return Rock

        elif user == 'p':
            return Paper
        
        elif user == 's':
            return Scissors

        else:
            print("try again")
            continue
        
def get_bot_input():

    user = {'r', 's', 'p'}

    p = random.randint(1,len(user))

    
    if p == 1:
        print('r')
        return Rock

    elif p == 2:
        print('p')
        return Paper
            
    else:
        print('s')
        return Scissors



def main():

    user_score_main = 0
    bot_score_main = 0
    
    win = 0
    lose = 0
    
    while True:

        my_opt = get_user_input()
        bot_opt = get_bot_input()

        user_score, bot_score = win_checker(my_opt,bot_opt)
        user_score_main += user_score
        bot_score_main += bot_score

        if user_score_main == 5:
            print("you WIN")
            break

        elif bot_score_main == 5:
            print("you LOSE")
            break

        print(f'your score is {user_score_main}')
        print(f'bot score is {bot_score_main}')


main()
