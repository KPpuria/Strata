import player

from collections import deque

class Team:

     # Initialize team props
    def __init__(self,no_players, batting_order) -> None:
        self.team_score = 0
        self.wickets = 0
        self.overs_played = 0
        self.team_no_players = no_players
        self.team_unplayed = batting_order
        self.team_playing = deque()
        self.team_out = []
        
    def match_start(self):
        self.team_playing.append(self.team_unplayed.pop(0))
        self.team_playing.append(self.team_unplayed.pop(0))

    def player_wicket(self):
        self.team_out.append(self.team_playing.popleft())
        if len(self.team_unplayed) > 0:
            self.team_playing.appendleft(self.team_unplayed.pop(0))

    def swap_striker(self):
        self.team_playing[0],self.team_playing[1] = self.team_playing[1],self.team_playing[0]
                    
    def team_scoring(self,scores):
        for score in scores:
            if score == 'w':
                self.player_wicket()
            else:
                self.team_score += score
                self.team_playing[0].add_runs(score)
                if score % 2 == 1:
                    self.swap_striker()

    def scorecard_end_over(self,over_balls_delivered = 0):
        
        print("\nTotal: ",self.team_score,end="")
        print("/",self.wickets)

        print("Overs: ",end='')
        print(self.overs_played,end='')
        if over_balls_delivered > 0:
            print('.',over_balls_delivered)

    def scorecard_end_match(self,over_balls_delivered = 0):

        print("Score for Team 1")
        print("Player Name\tScore")
        for player in self.team_out:
            print('P',player.name,end='')
            print('\t\t',player.runs_scored)
        for player in self.team_playing:
            print('P',player.name,end='')
            print('*\t\t',player.runs_scored)
        for player in self.team_unplayed:
            print('P',player.name,end='')
            print('\t\t',player.runs_scored)

        self.scorecard_end_over(over_balls_delivered)

        print("\n\nInnings Ended [runs/wickets/overs]")
        print("Final score",end=" ")
        overs_played = self.overs_played
        if over_balls_delivered > 0: overs_played = str(overs_played)+"."+str(over_balls_delivered)
        print(self.team_score,self.wickets,overs_played,sep="/")
