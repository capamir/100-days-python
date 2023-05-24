from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_obj = Menu()
options = menu_obj.get_items()
coffee = CoffeeMaker()
money = MoneyMachine()


order = ''
while order != 'exit':
    order = input(f'What would you like?({options}): ')

    if order == 'exit':
        pass

    elif order == 'report':
        coffee.report()
        money.report()

    else:
        drink = menu_obj.find_drink(order) 
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)

