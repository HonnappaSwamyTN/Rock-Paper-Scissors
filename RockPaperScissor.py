# n number of games.
# Stop once one out of 2 wins or meets the winning comdition.
# Play again option at the last.

import random
import os #For clearing screen
import time #For time delay
class RockPaperScissors:
    def __init__(self):
        os.system('cls') #cleans the screen once the object is created
        self.players_score={'player_1':0,'player_2':0}
        self.i=0
        self.beats={'rock':'scissors','paper':'rock','scissors':'paper'}
        self.wrong_input=0
        self.user1_name=""
        self.user2_name=""
        self.user_common_moves={'rock':0,'paper':0,'scissors':0}
    
    def delay_message(self,str):
        for ch in str:
                print(ch,end="")
                time.sleep(0.050)

    def computer_choice(self):

        max_key = max(self.user_common_moves, key=self.user_common_moves.get)
        if self.i>=2:
            return self.beats[self.beats[max_key]]


        return random.choice(['rock','paper','scissors'])
    
    def determine_winner(self,player1_name,player2_name,player1_value,player2_value):
        if(player1_value==player2_value):
            self.delay_message("It's a draw match\n")
        elif self.beats[player1_value] == player2_value :
            self.players_score['player_1']+=1
            self.delay_message(f"{player1_name} wins round {self.i+1}.\n")
        else:
            self.players_score['player_2']+=1
            self.delay_message(f"{player2_name} wins round {self.i+1}.\n")
    
    def play(self,n,num):

        self.i=0  
        self.user_common_moves={'rock':0,'paper':0,'scissors':0}
        mapping = {
                    'r': 'rock',
                    'p': 'paper',
                    's': 'scissors',
                    'scissor': 'scissors'
                }     
        self.user1_name=input("\nEnter player 1 name : ")
        
        if num==2:
            self.user2_name=input("Enter player 2 name : ")

        else:
            self.user2_name="Computer"    

        while(True):
            win_cond=(n//2)+1
            if self.players_score['player_2'] == win_cond or self.players_score['player_1'] == win_cond :
                break
            else:
                user1_value=input(f"\n👤 {self.user1_name} Enter your choice : ").lower()

                user1_value = mapping.get(user1_value, user1_value)

                if user1_value not in mapping.values():
                    print("Invalid choice. Enter rock, paper or scissors.")
                    continue

                self.user_common_moves[user1_value] += 1

                if num==1:

                    user2_value=self.computer_choice()
                    print(f"🤖 Computer choice : {user2_value}")
                
                else:
                
                    user2_value=input(f"👤 {self.user2_name} Enter your choice : ").lower()

                user2_value = mapping.get(user2_value, user2_value)
                if user2_value not in mapping.values():
                    print("Invalid choice. Enter rock, paper or scissors.")
                    continue

                self.determine_winner(self.user1_name,self.user2_name,user1_value,user2_value)
                self.i+=1
            
    
    def display_result(self):
        print('\n\n---------------------------------------------------\n')
        print('                    --MATCH RESULTS--\n')
        print('---------------------------------------------------\n')

        print(f"SCORES \n\n{self.user1_name} : {self.players_score['player_1']}\n{self.user2_name} : {self.players_score['player_2']}\n")

        if self.players_score['player_1'] == self.players_score['player_2']:
            self.delay_message("Its a draw.")
        elif self.players_score['player_1'] > self.players_score['player_2'] :
            self.delay_message(f"🏆 {self.user1_name} WINS THE MATCH! 🎉🎉🎉")
            self.delay_message("\n🌟 Congratulations! 🌟\n")
        else:
            self.delay_message(f"💀 {self.user2_name} WINS THE MATCH! Better luck next time! 🤖\n")

        self.players_score['player_1']=0
        self.players_score['player_2']=0

game=RockPaperScissors()

while(True):
    try:
        os.system('cls')
        game.delay_message("WELCOME\n\n")
        num_player=int(input("1.Player vs Computer\n2.Player vs Player\n\nEnter your choice : "))
        game.wrong_input=0
    except ValueError:
        
        if game.wrong_input<2:
                print("🙄 Enter a proper choice (1 or 2 only).\n")
        elif game.wrong_input<3:
            print("😠 what's wrong with you.\nEnter a proper choice (1 or 2 only).\n")
        else:
            game.delay_message("You know what I am done with you 🙂, just fuck off... 🖕")
            time.sleep(1)
            game.delay_message("\n💀 Exiting the game... 💀") 
            time.sleep(1.5)
            os.system('cls')
            exit(0)
        game.wrong_input+=1        
        time.sleep(2)
        continue

    if num_player not in [1,2]:
        if game.wrong_input<2:
            print("🙄 Enter a proper choice (1 or 2 only).\n")
        elif game.wrong_input<3:
            print("😠 what's wrong with you.\nEnter a proper choice (1 or 2 only).\n")
        else:
             game.delay_message("You know what I am done with you 🙂, just fuck off... 🖕")
             time.sleep(1)
             game.delay_message("\n💀 Exiting the game... 💀") 
             time.sleep(1.5)
             os.system('cls')
             exit(0)
        game.wrong_input+=1
        time.sleep(1)
        continue

    while(True):
        try:
            num=int(input("\n🎮 Enter the number of rounds(3,5,7,9.....) : "))

            if num%2==0 :
                print("\n\nEnter the proper number of rounds.")
                game.wrong_input+=1
                continue
            
            else:
                break

        except ValueError:
            if game.wrong_input<2:
                print("🙄 Enter a proper choice .\n")
            elif game.wrong_input<3:
                print("😠 what's wrong with you.\nEnter a proper choice.\n")
            else:
                game.delay_message("You know what I am done with you 🙂, just fuck off... 🖕")
                time.sleep(1)
                game.delay_message("\n💀 Exiting the game... 💀") 
                time.sleep(1.5)
                os.system('cls')
                exit(0)
            game.wrong_input+=1        
            time.sleep(2)
            continue    
    break

def game_run():
    game.play(num,num_player)
    game.display_result()

while(True) :
    game_run()
    try:
        replay=int(input("\n1. 🔄Play again\n2. 🚪Exit\n"))

        if replay==2:
            game.delay_message("Exitting the game....\n")
            
        elif replay==1:
            game.delay_message("🔄 STARTING A NEW GAME...\n")
            time.sleep(1.5)
            continue
        else:
            print("Select 1 or 2 only.")
            continue
        game.delay_message("Thanks for playing 🎉")
        time.sleep(1.5)#3 sec time delay before clearing the screen before ending the program
        os.system('cls')#Clears the screen before ending the program.
    

    except ValueError:
        print("Select a proper choice.")
        game.wrong_input+=1
        continue
    break