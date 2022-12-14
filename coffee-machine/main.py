MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report(resources):
    print(f'Water : {resources["water"]}ml')
    print(f'Milk : {resources["milk"]}ml')
    print(f'Coffee : {resources["coffee"]}g')
    print(f'Money : ${resources["money"]}')

def check_resources(ingredients, resources):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def insert_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_coins = (0.25 * quarters) + (0.1 * dimes) + (0.05 * dimes) + (0.01 * pennies)
    return total_coins

def enough_coins(total_price, user_coins, resources):
    refund_amount = user_coins - total_price
    if refund_amount < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif refund_amount > 0:
        resources["money"] += total_price
        print(f"Here is ${refund_amount:.2f}")
        return True

def make_coffee(ingredients, resources, flavor):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {flavor} ☕. Enjoy!")

def order_coffee(MENU, resources):
    is_on = True
    while is_on:
        coffee_machine = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_machine != "off":
            if coffee_machine == "report":
                report(resources)
            elif check_resources(MENU[coffee_machine]["ingredients"], resources):      
                user_coins = insert_coins() 
                have_coins = enough_coins(MENU[coffee_machine]["cost"], user_coins, resources)
                if have_coins:
                    make_coffee(MENU[coffee_machine]["ingredients"], resources, coffee_machine)
        else:
            is_on = False

resources["money"] = 0
    
is_on = True

order_coffee(MENU, resources)