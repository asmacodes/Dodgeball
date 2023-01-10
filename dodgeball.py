import random


def point_gained(human_action, computer_action):
    '''(str,str)-> str
    Returns the name of the player that gained a point

    '''
    if human_action == 'throw' and computer_action == 'throw':
        return 'human and computer'
    elif human_action == 'throw' and computer_action!= 'dodge':
        return 'human'
    
    elif computer_action == 'throw' and human_action != 'dodge':
        return 'computer'
    
    else:
        return ''
   
    
def get_computer_action(num_player_balls, num_opponent_balls):
    '''(int,int)-> str
    This function will decide what action the computer will take
    '''
    
    if num_player_balls >= 2:
        return 'dodge'
    
    elif num_opponent_balls == 0:
        computer_option = random.choice(('pickup' , 'dodge'))
        return computer_option
    
    elif num_opponent_balls ==3:
        computer_option = random.choice(('throw' , 'dodge'))
        return computer_option
    
    elif num_opponent_balls == 1 or num_opponent_balls == 2:
        computer_option = random.choice(('throw' , 'dodge', 'pickup'))
        return computer_option


def get_human_action(num_player_balls, num_opponent_balls):
    '''(int,int)-> str
    Returns the action the user chooses 
    '''
    
    action = 0
    while action == 0:
        action = input("\nHUMAN: Which action do you want to take? ")   
        
        if num_player_balls ==0 and action == 'throw':
            print('You dont have a ball to throw, Please pickup a ball')
        
        elif action == "throw" :
            print('The human is throwing the ball')
            return action
            
        elif action == "dodge":
            print('The human is dodging a ball')
            return action
        
        elif action == "pickup" and num_player_balls >= 3:
            print('You have already picked the maximum number of balls')
        
        
        elif action == "pickup" and num_player_balls <3:
            print('The human is picking up a ball')
            return action
             
        else:
            print("Please enter a valid response.")
            action = 0 
        
    
    
   
def play_game():
    human_points = 0
    computer_points = 0
    num_human_balls = 0
    num_computer_balls = 0
    
    while human_points < 5 and computer_points <5: #the game stops when one of the players reaches 5 points
        human_action = get_human_action(num_human_balls, num_computer_balls)
        computer_action = get_computer_action(num_human_balls, num_computer_balls)
       
        
        if human_action == 'pickup' and num_human_balls != 3:
            
            num_human_balls += 1
        
        if computer_action == 'pickup': #and num_computer_balls != 3:
            print('The computer is picking up a ball')
            num_computer_balls += 1
            
        if human_action == 'throw':
            num_human_balls -= 1
        
        if computer_action == 'throw':
            print('The computer is throwing a ball ')
            num_computer_balls -= 1
        
        if computer_action == 'dodge':
            print ('The computer is dodging a ball')
        
        if point_gained(human_action, computer_action) == 'human and computer':
            human_points +=1
            computer_points +=1
            print('Both players win a point!')
        
        if point_gained(human_action, computer_action) == 'human':
            human_points +=1
            print ('The computer did not dodge the players throw \nThe player wins a point!')
        if point_gained(human_action, computer_action) == 'computer':
            computer_points +=1
            print('The player did not dodge the computers throw \nThe computer wins a point!')
        
            
        print('\nNumber of human player points:',human_points)
        print('Number of computer points:',computer_points)
        print('Number of human player balls:', num_human_balls)
        print('Number of computer player balls:', num_computer_balls)
        
        if human_points == 5 and computer_points == 5 : #incase both players get 5 points at the same time
            print('\nBOTH PLAYERS WIN AT THE SAME TIME')
        
        elif human_points == 5:
            print('\nTHE WINNER IS THE HUMAN PLAYER')
        
        elif computer_points ==5:
            print('\nTHE WINNER IS THE COMPUTER')
            
        

play_game()











































