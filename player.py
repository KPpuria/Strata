class Player:
    
    def __init__(self, name) -> None:
        self.name = name
        self.runs_scored = 0

    def add_runs(self,run: int)-> None:
        self.runs_scored += int(run)