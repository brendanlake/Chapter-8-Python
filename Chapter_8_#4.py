def print_fruit_prices():
    print('Fruit Prices')
    for fruit, price in fruit_prices.items():
        print('%s: $%.2f' % (fruit, price))
fruit_prices = {}
num = int(input('How many different kinds of fruit would you like to enter?'))
for i in range(num):
    fruit = input('Enter a fruit: \n')
    price = input('Enter the price of that fruit: \n')
    fruit_prices[fruit] = float(price)
print_fruit_prices()
while True:
    more = input('Would you like to enter any more fruits? (yes or no)\n')
    if more == 'no':
        break
    fruit = input('Enter a fruit: \n')
    price = input('Enter the price of that fruit: \n')
    fruit_prices[fruit] = float(price)
print_fruit_prices()
while True:
    less = input('Would you like to remove any fruits? (yes or no)\n')
    if less == 'no':
        break
    fruit = input('Enter a fruit to remove: \n')
    del fruit_prices[fruit]
print_fruit_prices()

