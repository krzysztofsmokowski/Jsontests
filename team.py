class Player(object):
###    '''Class that is representing player with their statistics like attack, defence, gank etc'''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.stats = {}

    def statadd(self, stat, value):
        self.stats[stat] = value

class TeamManager(object):
    '''Class that will manage dota team '''

    def __init__(self):
        self.team = []

    def adder(self, player):
        self.team.append(player)

    def remover(self, firstname):
        for player in self.team:
            if player.firstname == firstname:
                self.team.remove(player)

    def get_players(self):
        return(self.team)

teammanager = TeamManager()


gracz = Player("krzychenko", "smok")
gracz.statadd("str", "50")
teammanager.adder(gracz)
gracz2 = Player("macienko", "strzelenko")
gracz2.statadd("str", "40")
teammanager.adder(gracz2)
print(teammanager.team)
teammanager.remover("macienko")

for player in teammanager.get_players():
    print player.firstname


