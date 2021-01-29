# Inputs
priceOfJeans = [2, 3]
priceOfShoes = [4]
priceOfSkirts = [2, 3]
priceOfTops = [1, 2]
budgeted = 10

num_ways = 0

def number_of_ways(options, budget, idx):
    global num_ways

    if budget < 0:
        return
    
    if idx >= len(options):
        num_ways += 1
        return

    for product in options[idx]:
        number_of_ways(options, budget-product, idx+1)


number_of_ways([priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops], budgeted, 0)
print(num_ways)