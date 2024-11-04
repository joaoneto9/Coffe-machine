from coffe_types import MENU
from coffe_types import resources
from coffe_types import secretwords
from coffe_types import coins 
money = 0

def make_coffe(pay, choice, resources, menu):
    change = pay - menu[choice]["cost"]
    ingredients = menu[choice]["ingredients"]
    for elem in ingredients:
        resources[elem] -= ingredients[elem]
    
    if change > 0: return change
    
def payment(coins):
    pay = 0
    for coin in coins:
        times = int(input(f"How many {coin}: "))
        pay += coins[coin] * times

    return pay

def check(resources, ingredients):
    for ingrd in ingredients:
        if ingredients[ingrd] > resources[ingrd]: 
            return (f"Sorry there is not enough {ingrd}.")
    
    return "ok"

def report(resources, money):
    for elem in resources:
        if elem != "coffee": print(f"{elem}: {resources[elem]}ml")
        else: print(f"{elem}: {resources[elem]}g")

    print(f"money: ${money:.2f}")

while True:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ") 
    if choice == secretwords[0]: break
    elif choice == secretwords[1]: report(resources, money)
    elif choice in MENU: 
        check_ingredients = check(resources, MENU[choice]["ingredients"])
        if check_ingredients == "ok": 
            pay = payment(coins)
            if pay < MENU[choice]["cost"]: print("Sorry that's not enough money. Money refunded.")
            else:
                money += MENU[choice]["cost"]
                change = make_coffe(pay, choice, resources, MENU)
                if change is not None: print(f"\nHere is ${change:.2f} dollars in change")
                print(f"Here is your {choice}. Enjoy!")

        else: print(check_ingredients)


         