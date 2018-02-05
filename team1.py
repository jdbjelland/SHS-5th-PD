####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
#	  This is a test change wow
####
import random

team_name = 'GloblKarma' # Only 10 chars displayed.
strategy_name = 'Karma'
strategy_description = 'If you win, stay. If you lose, switch.'

def flip():
    if random.randint(1, 101) >=50:
        return 'b'
    else:
        return 'c'

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0: #First round collude
        return 'c'
    if my_history[-1]=='c' and their_history[-1]=='b': #If we lost, counter back with a 50% chance 'b' or 'c'.
        flip()
    if my_history[-1]=='b' and their_history[-1]=='c': #If we won, keep the same strategy
        return 'b'
    if my_history[-1]=='c' and their_history[-1]=='c':# If both sides colluded, keep colluding.
        return 'c' 
    else:
        return 'b'
    