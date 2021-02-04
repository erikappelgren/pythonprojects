import random

def __start_round__(self):
        self.round += 1
        rolls = 1
        dice_reroll = ["r","r","r","r","r"]
        dice = [1,5,2,3,4]
        print("\nRound: " + str(self.round) + "\n")
        print("\n\n")
        self.scoreCard.__get_score__()
        self.scoreCard.__showOpenSlots__()
        print("\n")
        while rolls < 4:
            print("Roll: " + str(rolls))
            print("=============================")
            i = 0
            while i < 5:
                if(dice_reroll[i] == "r"):
                    dice[i] = random.randint(1,6)
                    #Fixing the roll remove later
                    #dice[i] = 5
                    # END fixing the game
                    dice_reroll[i] = 'q'
                #print("Dice " + str(i+1) + ": " + str(dice[i]))
                i += 1
            dice.sort()
            print(dice)
            if(self.__yahtzee__(dice) == True):
                print("YAHTZEE!")
                self.yahtzee_count += 1
            print("=============================")
            if rolls < 3:
                i = 0
                while i < 5:
                    dice_reroll[i] = input("Dice " + str(i+1) + " value: " + 
                    str(dice[i]) + " - Type r to re-roll, w to keep, e to re-roll all, q to keep all\n")
                    if dice_reroll[i] == "q":
                        a = 0
                        for x in dice_reroll:
                            dice_reroll[a] = "w"
                            a += 1
                        rolls=2
                        break
                    elif dice_reroll[i] == "e":
                        a = 0
                        for x in dice_reroll:
                            dice_reroll[a] = "r"
                            a += 1
                        break
                    elif dice_reroll[i] == "w" or dice_reroll[i] == "r":
                        i += 1
                    else:
                        print("Please enter a valid input");
            else:
                self.scoreCard.__update_score__(dice)
            rolls += 1
        print("Total rounds: " + str(self.round) + "\n" + "Total yahtzees: " + str(self.yahtzee_count))

#__start_round__(self)