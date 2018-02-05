
from __future__ import print_function

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Cyberchase' # Only 10 chars displayed.
strategy_name = 'CopyCat'
strategy_description = 'For the first round it colludes then if the opponent betrayed in the last 10 moves then it will betray, otherwise it will copy the last move of the opponent'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    
    if len(my_history) == 0: #first move = 'c'
        return 'c'
    elif 'b' in their_history[-10:]: # if 'b' in their last 10 moves then return 'b'
        return 'b'
    else:
        return their_history[-1] #otherwise return opponent's last move


def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Collude on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print('Test passed')
     # Test 2: Copy opponent's last move
    test_move(my_history='ccc',
              their_history='ccc', 
              my_score=0, 
              their_score=0,
              result='c')  
    #Test 3 if betray is in last opponent's 10 moves don't copy opponent's last move, betray instead
    test_move(my_history= 'cbb', 
            their_history= 'cbc', 
              their_score=0,
              my_score=0,
              result='b')               
