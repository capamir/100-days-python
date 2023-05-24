def report(machine):
    print(f"Water: {machine['ingerdients']['water']}ml")
    print(f"Milk: {machine['ingerdients']['milk']}ml")
    print(f"Water: {machine['ingerdients']['coffee']}g")
    print(f"Money: ${machine['money']}")

def take_coins(coins):
    print('Please insert coins')
    money = 0.00
    money += int(input('How many quarters: ')) * coins['quarter']
    money += int(input('How many dimes: ')) * coins['dime']
    money += int(input('How many nickles: ')) * coins['nickle']
    money += int(input('How many pennies: ')) * coins['penny']

    return round(money, 2)

def take_order(resourses, order, coffee, money):
    if coffee['price'] > money:
        print('not enough money')
        return
    
    for key in coffee['ingerdients'].keys():
        print(key)
        if coffee['ingerdients'][key] > resourses['ingerdients'][key]:
            print(f'sorry not enough {key}')
            return

    for key in coffee['ingerdients'].keys():
        resourses['ingerdients'][key] -= coffee['ingerdients'][key]

    change = round(money - coffee['price'], 2)
    if change > 0:
        print(f'Here is ${change} change')

    resourses['money'] += coffee['price']
    print(f'Here is your {order}')
    return resourses

COFFEES = {
    'espeso': { 'ingerdients': {'water': 50, 'coffee': 18, 'milk': 0}, 
               'price': 1.50 },
    'latte': { 'ingerdients': {'water': 200, 'coffee': 24, 'milk': 150}, 
              'price': 2.50 },
    'cappuccino': { 'ingerdients': {'water': 250, 'coffee': 24, 'milk': 100}, 
                   'price': 3.00 },
}
COINS = { 'penny': 0.01, 'nickle': 0.05, 'dime': 0.10, 'quarter': 0.25,  }

resourses = {'ingerdients': {'water': 300, 'coffee': 100, 'milk': 200}, 'money': 0}

order = ''
while order != 'exit':
    order = input('what would you like?(espreso/latte/cappuccino): ')

    if order == 'report':
        report(resourses)

    elif order in COFFEES:
        payment = take_coins(COINS)
        print('$', payment)
        resourses = take_order(resourses, order, COFFEES[order], payment)
    else:
        print('wrong order', order)
