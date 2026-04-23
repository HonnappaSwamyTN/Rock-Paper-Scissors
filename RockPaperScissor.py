# n number of games.
# Stop once one out of 2 wins or meets the winning comdition.
# Play again option at the last.

import random

class RockPaperScissors:
    def __init__(self):
        self.player_score=0
        self.computer_score=0
        self.number_of_rounds=0
        self.i=0
        self.beats={'rock':'scissors','paper':'rock','scissors':'paper'}
    
    def computer_choice(self):
        return random.choice(['rock','paper','scissors'])
    
    def determine_winner(self,user,computer):
        if(user==computer):
            print("It's a draw match\n")
        elif self.beats[user] == computer :
            self.player_score+=1
            print(f"Player wins round {self.i+1}.\n")
        else:
            self.computer_score+=1
            print(f"Computer wins round {self.i+1}.\n")
    
    def play(self,n):

        while(True):
            win_cond=(n//2)+1
            if self.computer_score == win_cond or self.player_score == win_cond :
                break
            else:
                user_value=input("Enter your choice : ").lower()

                mapping = {
                    'r': 'rock',
                    'p': 'paper',
                    's': 'scissors',
                    'scissor': 'scissors'
                }
                user_value = mapping.get(user_value, user_value)

                computer_value=self.computer_choice()
                print(f"Computer choice : {computer_value}")
                self.determine_winner(user_value,computer_value)
                self.i+=1
            
    
    def display_result(self):
        print('\n\n---------------------------------------------------\n')
        print('                    --MATCH RESULTS--\n')
        print('---------------------------------------------------\n')

        print(f"SCORES :\nPlayer : {self.player_score}\nComputer : {self.computer_score}")

        if self.player_score == self.computer_score:
            print("Its a draw.")
        elif self.player_score > self.computer_score :
            print("Player wins.")
        else:
            print("Computer wins.")

while(True):
    try:
        num=int(input("Enter the number of rounds(3,5,7,9.....) : "))

    except ValueError:
        print("Please enter a valid number")
        continue
    if num%2==0 :
        print("Enter the proper number of rounds.")
    else:
        break
def game_run():
    game=RockPaperScissors()
    game.play(num)
    game.display_result()

while(True) :
    game_run()

    replay=int(input("1.Play again\n2.End\n"))

    if replay==1:
        continue
    break
