from main import resources
from main import MENU
from main import coins

def generate_report():
    for hoofd_key, sub_dictionary in resources.items():
        print(f"{hoofd_key}: {sub_dictionary["quantity"]}{sub_dictionary["unit"]}")

def check_resources(choice_customer):
    """Gets choice customer as input and returns if there
    are sufficient resources."""
    missing_ingredients = []
    for i_m, m in MENU[choice_customer]["ingredients"].items():
        ingredient = i_m
        value_ingredient = m
        if resources[ingredient]["quantity"] < value_ingredient:
            missing_ingredients.append(ingredient)
    if missing_ingredients:
        print(f"Sorry there is not enough {missing_ingredients}")
        return False
    else:
        return True

# TODO: 7. Make Coffee
def deduct_resources(choice_drink):
    for sleutel, waarde in MENU[choice_drink]["ingredients"].items():
        ingredient = sleutel
        hoeveelheid = waarde
        resources[ingredient]["quantity"] -= hoeveelheid


# TODO: 1. Make an input function for the choice
continue_dispensing = True
while continue_dispensing:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Puts off coffee machine
    if choice == "off":
        continue_dispensing = False
        print("Machine has been turned off")

    # TODO: 3 Make generate_report function
    elif choice == "report":
         generate_report()

    # TODO: 4.& 5. Process coins & check if transaction successful
    elif choice in MENU:
        sufficient_resources = check_resources(choice)
        if sufficient_resources == True:
            total_amount = 0
            print("Please insert coins.")
            for i in coins:
                amount = int(input(f"How many {i}?: ")) * coins[i]
                total_amount += amount
            if total_amount < MENU[choice]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["Money"]["quantity"] += MENU[choice]["cost"]
                if total_amount - MENU[choice]["cost"] > 0:
                    change = total_amount - MENU[choice]["cost"]
                    change = round(change, 2)
                    print(f"Here is ${change} in change")
                deduct_resources(choice)
                print(f"Enjoy your {choice}!")
    else:
        print("You've typed a wrong input, please try again")