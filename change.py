list = [1, 2, 5, 10, 20, 50, 100, 200, 500]

amount = (50)
def change(amount):
    money = []
    values = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    values.reverse()
    count = []
    for i in values:
        num = amount / i
        money += (i,) * num
        amount -= i * num
    return money
    #print(str(amount))

#change(amount)

def change(cost, bill):
    amount= bill - cost
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
    coins.reverse()
    coinsReturned = []
    for i in coins:
        while amount >=i:
            coinsReturned.append(i)
            amount = amount - i
    print('\n'.join(map(str, coinsReturned))) 

change(149, 200)


