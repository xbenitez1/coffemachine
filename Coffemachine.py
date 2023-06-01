from main import MENU

# TODO: REPORT RESOURCES
water = 300
milk = 200
coffee = 100
money = 0
espresso_counter = 0
latte_counter = 0
cappuccino_counter = 0
total_bill = float()


def pay(bill = total_bill, count = money):
    print(f"Your total to pay is $ {bill}")
    quarter = int(input("how meny quarters '25 cents': "))
    dime = int(input("how meny dime '10 cents': "))
    nikel = int(input("how meny nikel '5 cents': "))
    peny = int(input("how meny peny '1 cents': "))
    total_pay = float(((quarter * 25) + (dime * 10) + (nikel * 5) + peny) / 100)
    print(f"your bill is $ {bill}")
    print(f"Total pay $ {total_pay}")
    if bill > total_pay:
        return f"“Sorry that's not enough money. Money refunded, mis {(bill - total_pay) * 100} cents"
    else:
        print (f"Your {choice} is in progress\n")

machine = "on"

while machine == "on":
    choice = input("""What would you like
    Espresso

    Latte
    Cappuccino
    
    Whrite you option: """).lower()
    if choice != "report" and choice != "off":
        if choice == "espresso" or choice == "cappuccino" or choice == "latte":
            total_bill = float(MENU[choice]["cost"])
        else:
            continue

    if choice == "espresso" or choice == "cappuccino" or choice == "latte":
        water_c = int(MENU[choice]["ingredients"]["water"])
        milk_c = int(MENU[choice]["ingredients"]["milk"])
        coffee_c = int(MENU[choice]["ingredients"]["coffee"])

        if water_c < water and milk_c < milk and coffee_c < coffee:
            water -= water_c
            milk -= milk_c
            coffee -= coffee_c
        elif water_c > water:
            print("Sorry there is not enough Water")
        elif milk_c > milk:
            print("Sorry there is not enough Milk")
        elif coffee_c > coffee:
            print("Sorry there is not enough water")

    if choice == "espresso":
        print(pay(bill=total_bill))
        espresso_counter += 1
    elif choice == "cappuccino":
        print(pay(bill=total_bill))
        cappuccino_counter += 1
    elif choice == "latte":
        print(pay(bill=total_bill))
        latte_counter += 1
    elif choice == "report":
        print(f"water {water} ml")
        print(f"milk {milk} ml")
        print(f"coffee {coffee} g")
        print(f"money $ {money}")
        print(f"expresso {espresso_counter}")
        print(f"capuccinno {cappuccino_counter}")
        print(f"latte {latte_counter}")
    elif choice == "off":
        machine = "off"
    else:
        continue




