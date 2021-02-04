from collections import Counter

def check_combinations(dices):
    """Takes a set of dices as a list and checks if it contains any valid combinations.
    """
    combinations = {
        "Pairs": check_one_pairs(dices),
        "Two pairs": check_two_pairs(dices),
        "Three of a kind": check_three_of_a_kind(dices),
        "Four of a kind": check_four_of_a_kind(dices),
        "Small straight": check_small_straight(dices),
        "Large straight": check_large_straight(dices),
        "Full house": check_full_house(dices),
        "Yatzy": check_yatzy(dices)
    }
    return combinations


def check_one_pairs(dices):
    """Takes a set of dices as a list and checks if it contains any pairs.
    If found, returns the pairs found as a tuple in a list.
    """
    pairs = []
    for i in range(1, 7):           # Look for pairs
        if dices.count(i) >= 2:     # Add the pair to the pairs list 
            pairs.append((i, i))
    if len(pairs) != 0:
        return pairs
    return False

def check_two_pairs(dices):
    """Takes a set of dices as a list and checks if it contains any pairs.
    If found, returns the three of a kind found as a tuple in a list.
    """
    if len(Counter(dices)) <= 3:        # If the length is higher than three, it cannot contain any two pairs
        two_pair = []
        for key, value in Counter(dices).items():       # Check if it is actually a pair and not a three of a kind
            if value == 2 or value == 3:
                two_pair.extend([int(key), int(key)])
        if len(two_pair) == 4:
            return [tuple(two_pair)]
    return False
    
def check_three_of_a_kind(dices):
    """Takes a set of dices as a list and checks if it contains any pairs.
    If found, returns the three of a kind found as a tuple in a list.
    """
    for i in range(1, 7):           # Look for three of a kind
        if dices.count(i) >= 3:     # Add the pair to the pairs list 
            return [(i,i,i)]
    return False

def check_four_of_a_kind(dices):
    """Takes a set of dices as a list and checks if it contains four of a kind.
    If found, returns the four of a kind found as a tuple in a list.
    """
    for i in range(1, 7):           # Look for four of a kind
        if dices.count(i) >= 4:     # Return the four of a kind if found
            return [(i, i, i, i)]
    return False

def check_small_straight(dices):
    """Takes a set of dices as a list and checks if it contains a small straight.
    If found, returns the small straight as a tuple in a list.
    """
    if len(set(dices)) == 5:        # If the length of a set is 5, it contains no pairs
        if sorted(dices) == [1,2,3,4,5]:
            return [(1,2,3,4,5)]
    return False    

def check_large_straight(dices):
    """Takes a set of dices as a list and checks if it contains a large straight.
    If found, returns the large straight as a tuple in a list.
    """
    if len(set(dices)) == 5:        # If the length of a set is 5, it contains no pairs
        if sorted(dices) == [2,3,4,5,6]:
            return [(2,3,4,5,6)]
    return False

def check_full_house(dices):
    """Takes a set of dices as a list and checks if it contains a full house.
    If found, returns the full house as a tuple in a list.
    """
    if len(set(dices)) == 2:        # Length of the set must be exactely 2 for a full house to be valid
        for value in Counter(dices).values():
            if value == 2:          # If the set contains a value of two, we know the other set must be a three
                return [tuple(sorted(dices))]
    return False

def check_yatzy(dices):
    """Takes a set of dices as a list and checks if it contains a yatzy.
    If found, returns the yatzy as a tuple in a list.
    """
    if len(Counter(dices)) == 1:       # For a valid yatzy the set of dices must only be of one and only one value
        return [(dices)]
    return False

def calculate_chance(dices):
    """Takes a set of dices and returns the som of them.
    """
    sum = 0
    for dice in dices:
        sum += dice
    return sum

def calculate_ones(dices):
    return dices.count(1) * 1

def calculate_twos(dices):
    return dices.count(2) * 2

def calculate_threes(dices):
    return dices.count(3) * 3

def calculate_fours(dices):
    return dices.count(4) * 4

def calculate_fives(dices):
    return dices.count(5) * 5

def calculate_sixes(dices):
    return dices.count(6) * 6

