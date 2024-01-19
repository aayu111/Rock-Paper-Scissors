import random

def play():
    user  = input("\n'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer =  random.choice(['r','p','s'])

    if  user not in ['r', 'p', 's']:
        return 'invalid  input'
        
    

    if user == computer:
        return 'Tie'
    
    if is_win(user,computer):
        return 'You won!'
    
    return "You Lost"
    

def is_win(player, opponent):
    if(player  == 'r' and opponent == 's')  or (player  == 's' and opponent == 'p') or  (player == 'p' and opponent == 'r'):
        return True
     
print(play())
        