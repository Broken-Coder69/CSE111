class HackathonTeam:
    def __init__(self, team, *participants):
        self.team = team
        self.participants = participants
        
    def information(self):
        print(f"Team name: {self.team}")
        print(f"Participants")
        for i in self.participants:
            print(i)


team_1 = HackathonTeam("Atlantean", "Aquaman")
team_1.information()
print("=================")
team_2 = HackathonTeam("Avengers", "Ironman", "Thor",
"Hulk")
team_2.information()
print("=================")
team_3 = HackathonTeam("X-Men", "Storm", "Mystique")
team_3.information()

# Team name: Atlantean
# Participants:
# Aquaman
# =================
# Team name: Avengers
# Participants:
# Ironman
# Thor
# Hulk
# =================
# Team name: X-Men
# Participants:
# Storm
# Mystique