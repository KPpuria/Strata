from typing import DefaultDict
import team 
import player

class Game:
    def __init__(self,no_overs=0) -> None:

        self.overs = no_overs
        self.balls_played = 0
        self.playing_batsmen = list()
        self.balls_per_over = 6

    #integer type validator
    def is_valid_input(self,data: int) -> bool:
        return int(data) and int(data)>0

    #check if score entered is valid
    def is_valid_run(self,data: int) -> bool:
        if(data == '0'):
            return True
        return data.isdigit() and int(data) <= 6 and int(data) >=0 and int(data) != 5

    
    def create_team(self,no_of_players,batting_order):
        team_created = team.Team(no_of_players,batting_order)
        return team_created


    # get all required information of teams players and overs
    def gather_information(self):
        
        #Get valid data for no of players 
        invalid_input = True
        while invalid_input:
            no_of_players = input("No of players in the Game: ")
            if(self.is_valid_input(no_of_players) and int(no_of_players)>=2):
                no_of_players = int(no_of_players)
                invalid_input = False
            else:
                print("No of players must be an integer greater than 1. Please try again")

        #Get valid data for no of overs
        invalid_input = True
        while invalid_input:
            no_of_overs = input("No of over in the Game: ")
            if(self.is_valid_input(no_of_overs)):
                self.overs = int(no_of_overs)
                invalid_input = False
            else:
                print("No of over in the Game must be an integer greater than 0. Please try again")

        #Get valid data for batting order
        batting_order = []
        invalid_input = True
        while invalid_input:
            print("Enter batting order by putting player number in front of P")
            for i in range(0,no_of_players):
                invalid_player = True
                while invalid_player:
                    player_orderin = input("P")
                    if(self.is_valid_input(player_orderin)):
                        if(int(player_orderin)<=no_of_players):    
                            batting_order.append(player.Player(player_orderin))
                            invalid_player = False
                        else:
                            print("player entered not within team size. Try again")
                    else:
                        print("invalid player entry")
            invalid_input = False

        new_team = self.create_team(no_of_players,batting_order)
        return new_team

        
    def play_over(self,batting_team) -> None:
        self.balls_played = 0
        scoring_in_over = []
        while self.balls_played < self.balls_per_over and batting_team.wickets < batting_team.team_no_players -1:
                runs_scored = input()
                if runs_scored == 'w':
                    batting_team.wickets += 1
                    self.balls_played += 1
                    scoring_in_over.append(runs_scored)
                    
                elif self.is_valid_run(runs_scored):
                    self.balls_played += 1
                    scoring_in_over.append(int(runs_scored))
                    
                else:
                    print("entered value needs be a valid score or a w")
        batting_team.team_scoring(scoring_in_over)

        if batting_team.wickets == batting_team.team_no_players - 1:
            return True

    def play_game(self):
        batting_team = self.gather_information()
        batting_team.match_start()
        for i in range(0,self.overs):
            print("\nOver ",i+1,end=":\n")
            game_state = self.play_over(batting_team)
            if game_state:
                print("\nMatch Ended by all out")
                break
            batting_team.overs_played += 1
            batting_team.swap_striker()
            if i+1 < self.overs:
                batting_team.scorecard_end_over()
        batting_team.scorecard_end_match(self.balls_played)






