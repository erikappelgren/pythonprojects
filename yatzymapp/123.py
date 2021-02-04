def _init_(self, player):
        player = 0
        self.player = player
        self.lista = {"Ones" : 0, "Dueces" : 0, "Threes" : 0, "Fours" : 0, "Fives" : 0,
                        "Sixes" : 0, "Bonus" : 0, "Pairs" : 0, "Two pairs" : 0, "Three of a kind" : 0,
                        "Four of a kind" : 0, "Small straight" : 0, "Large straight" : 0, "Full house" : 0, "Chance" : 0,
                        "Yatzy" : 0, "Total" : 0}
def add(self):
        """Add points to the player"""
        moment = input("Where do you want to put your points: ")
        points = input("How many points did you get: ")
        self.lista[moment][1] = points
        print (self.lista)
def welcome(self):
        """Asks for names"""
        print ("Welcome to the yatzy")
        players = input("How many players: ")
        self.names = []
        rounds = 0
        while players != rounds:
            player = input("What is your name?: ")
            self.names.append(player)
            rounds = rounds + 1
def visa(self):
        for i in self.names:
            print (i)
def main():
    #play = player(name)
    welcome()
    visa()
main()