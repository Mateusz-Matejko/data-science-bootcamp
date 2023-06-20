import random
import pprint
# ppl_in_team = 3

# list_of_participants = ["EwelinaU", "IzabelaR", "KacperD", "MagdalenaM", "MartynaS", "MateuszM",
#  "MateuszB", "Mikołaj", "MiłaD", "MonikaG", "MonikaK", "NataliaP",
#  "PatrycjaK", "PatrykŚ", "PatrykS", "PawelA", "PawwelŻ", "SebastianŻ"]
# print("Length of list:",len(list_of_participants))
# print("Length of set:",len(set(list_of_participants)))
#
# random.shuffle(list_of_participants)
#
# list_of_teams = []
# team = []

# for participant in list_of_participants:
#     team.append(participant)
#     if len(team) == ppl_in_team:
#         list_of_teams.append(team)
#         team = []
#     if not list_of_participants:
#         list_of_teams.append(team)
#         break

class RandomTeams:
    def __init__(self, team_size=3):
        self.list_of_participants = ["EwelinaU", "IzabelaR", "KacperD", "MagdalenaM", "MartynaS", "MateuszM",
                                     "MateuszB", "Mikołaj", "MiłaD", "MonikaG", "MonikaK", "NataliaP",
                                     "PatrycjaK", "PatrykŚ", "PatrykS", "PawelA", "PawwelŻ", "SebastianŻ"]
        self.team_size = team_size
        self.list_of_teams = []

    def create_teams(self):
        random.shuffle(self.list_of_participants)
        self.list_of_teams = []
        team = []
        for human in self.list_of_participants:
            team.append(human)
            if len(team) == self.team_size:
                self.list_of_teams.append(team)
                team = []
            if human == self.list_of_participants[-1] and len(self.list_of_participants) % self.team_size != 0:
                self.list_of_teams.append(team)
        pprint.pprint(self.list_of_teams)


z = RandomTeams(6)
z.create_teams()
