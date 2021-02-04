
def printCost(dict):
    sumofitems = []
    for k, v in dict.items():
        sumofitems.append(v)
    x = sum(sumofitems)
    moms = x * 0.12
    print('Total kostnad: ' + str(x) + ' kr')
    print('Varav moms: ' + str(moms) + ' kr')

printCost({'majs':21,
                'korv':35,
                'matolja':25,
                'toapapper':40})