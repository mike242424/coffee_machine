water = 300
milk = 200
coffee_grounds = 100

money = 0.0
keep_going = True


def insert_coins(price):
    penny = .01
    nickel = .05
    dime = .10
    quarter = .25

    print('Please insert coins.')
    num_of_quarters = int(input("How many quarters? "))
    num_of_dimes = int(input("How many dimes? "))
    num_of_nickels = int(input("How many nickels? "))
    num_of_pennies = int(input("How many pennies? "))

    total = (num_of_quarters * quarter) + (num_of_dimes * dime) + (num_of_nickels * nickel) + (num_of_pennies * penny)

    if total < price:
        print("Not enough money! Money refunded.")
    else:
        change = round((total - price), 2)
        print(f"Here is your change: ${change}")
        return change


print("Welcome to the coffee machine.")
while keep_going:
    order = input("What would you like? Type 'Espresso', 'Latte', or 'Cappuccino'. ").lower()

    if order == "report":
        print(f"Water left: {water}mL\nMilk left: {milk}mL\nCoffee grounds left: {coffee_grounds}g\nMoney left: ${money}")
    elif order == 'espresso':
        if water < 50 :
            print("Insufficient resources: Water.")
        elif coffee_grounds < 18:
            print("Insufficient resources: Coffee Beans.")
        else:
            water -= 50
            coffee_grounds -= 18
            print("Here is your espresso. Enjoy!")
            money = insert_coins(1.50)
    elif order == 'latte':
        if water < 200:
            print("Insufficient resources: Water.")
        elif coffee_grounds < 24:
            print("Insufficient resources: Coffee Beans.")
        elif milk < 150:
            print("Insufficient resources: Milk.")
        else:
            water -= 200
            coffee_grounds -= 24
            milk -= 150
            print("Here is your latte. Enjoy!")
            money = insert_coins(2.50)
    elif order == 'cappuccino':
        if water < 250:
            print("Insufficient resources: Water.")
        elif coffee_grounds < 24:
            print("Insufficient resources: Coffee Beans.")
        elif milk < 100:
            print("Insufficient resources: Milk.")
        else:
            water -= 250
            coffee_grounds -= 24
            milk -= 100
            print("Here is your latte. Enjoy!")
            money = insert_coins(3.00)
    elif order == 'off':
        keep_going = False
    else:
        print("Sorry, that is not a valid option.")
