
class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w
    def getValue(self):
        return self.value
    def getCost(self):
        return self.calories
    def density(self):
        return self.getValue()/self.getCost()
    def __str__(self):
        return self.name + ': <' + str(self.value)\
                 + ', ' + str(self.calories) + '>'

def buildMenu(items):
    """items is a list of tuples containing name, value, and calories.
       returns list of Foods"""
    menu = []
    for item in items:
        menu.append(Food(item[0] , item[1],
                          item[2]))
    return menu

def greedy(items, maxCost, chosenMetric):
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = chosenMetric, reverse = True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for item in itemsCopy:
        if totalCost + item.getCost() <= maxCost:
            result.append(item)
            totalCost += item.getCost()
            totalValue += item.getValue()
    return (result, totalValue)

def testGreedy(items, constraint, chosenMetric):
    taken, val = greedy(items, constraint, chosenMetric)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
#    print('Use greedy by value to allocate', maxUnits,'calories')
#    testGreedy(foods, maxUnits, Food.getValue)

#    print('\nUse greedy by cost to allocate', maxUnits,'calories')
#    testGreedy(foods, maxUnits, lambda x: -Food.getCost(x))

    print('\nUse greedy by density to allocate', maxUnits,'calories')
    testGreedy(foods, maxUnits, Food.density)


items = [('wine', 89, 123),('beer', 90, 154),('pizza', 95, 258),
         ('burger', 100, 354), ('fries', 90, 365),('cola', 79, 150),
         ('apple', 50, 95),('donut', 10, 195)]
foods = buildMenu(items)
testGreedys(foods, 1000)