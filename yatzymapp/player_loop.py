import random
players = []
def remainingThrows():
    userinput = int(input("Hur många spelar? "))
    players.extend(range(1, userinput +1))
    print(players)
    throws = 3
    list = []
    for i in players:
        list2 = []
        while throws > 0:
            test = input("Kasta? ")
            if test == "ja":
                for x in range(0, 5):
                    dice = random.randint(1, 6)
                    list2.append(dice)
                print(list2)
            throws = throws - 1
            print(str(throws) + " kast kvar")
            if test == "stop":
                break
            if throws == 0:
                print("Next player")
                i = i -1
                list.append(list2)
                print(list)
                throws = 3

remainingThrows()