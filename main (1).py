from random import randint


def find_round_winner(computer_finger, player_finger):
    if total==guess:
        return "Player"
    elif total!=guess:
        return "Computer"
    

player_wins=0
computer_wins=0

########################## END FUNCTION DEFINITIONS ######################


game_rules = """
    Welcome to Morra! In this game, you'll decide how many fingers
    to hold up (from one hand) and then the computer will randomly
    do the same. You'll need to guess the total number of fingers
    to win the round, before seeing how many fingers the computer
    has decided to hold up!
"""
print(game_rules)


name=input("What is your name? ")
rounds=int(input("How many rounds do you want to play? "))
for round in range(rounds):
    player_finger=int(input("How many fingers will you hold up? "))
    computer_finger=randint(1,5)
    guess=int(input("Guess the total number of fingers: "))
    total= player_finger + computer_finger
    round_winner=find_round_winner(computer_finger, player_finger)
    if round_winner=="Player":
        print("Thats correct!")
        print(f"{name} wins this round!")
        player_wins += 1
               
        
    elif round_winner=="Computer":
        print(f"Thats incorrect the total was {total}")
        print("Computer wins this round!")
        computer_wins += 1
            
            
        
            
print("Game over!")
print(f"{name} won {player_wins} rounds!")
print(f"Computer won {computer_wins} rounds!")
if player_wins > computer_wins:
    print(f"{name} wins the game!")
    
else:
    print("Computer wins the game!")
        
        
            
        
        
    
    

