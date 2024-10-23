import time
import random

def print_welcome_message():
    print("Congratulations! You've got a job at Python Pizza! Your first task is to build an automatic pizza ordering program.")
    time.sleep(1)
    print("Welcome to Python Pizza, the best pizza in town!\n")
    time.sleep(1)

def print_pizza_menu():
    print("\nPizza Prices:")
    print(f"Small Pizza: ${s_pizza}")
    print(f"Medium Pizza: ${m_pizza}")
    print(f"Large Pizza: ${l_pizza}")

def print_add_ons():
    print("\nAdd-ons:")
    print(f"Pepperoni for Small Pizza: ${s_pep}")
    print(f"Pepperoni for Medium/Large Pizza: ${l_m_pep}")
    print(f"Extra Cheese: ${cheese_price}")

def get_order():
    order = input("\nDo you want to order a pizza? Type Yes or No: ").lower()
    if order == "yes":
        return True
    elif order == "no":
        print("\nOkay, take your time! If you decide to order later, please let us know.")
        return False
    else:
        print("\nInvalid input. Please type 'Yes' or 'No'.")
        return get_order()

def get_pizza_size():
    print("\nWhat size of pizza would you like?")
    print("For Small Pizza type: S")
    print("For Medium Pizza type: M")
    print("For Large Pizza type: L")
    size = input("\nEnter your choice (S, M, L): ").upper()
    if size in ["S", "M", "L"]:
        return size
    else:
        print("\nInvalid input. Please enter 'S', 'M', or 'L'.")
        return get_pizza_size()

def calculate_pizza_price(size):
    if size == "S":
        return s_pizza
    elif size == "M":
        return m_pizza
    elif size == "L":
        return l_pizza

def add_pepperoni(size, bill):
    add_pep = input("\nWould you like to add pepperoni to your pizza? Type Yes or No: ").lower()
    if add_pep == "yes":
        if size == "S":
            bill += s_pep
        elif size in ["M", "L"]:
            bill += l_m_pep
    elif add_pep != "no":
        print("\nInvalid input. Please type 'Yes' or 'No'.")
        return add_pepperoni(size, bill)
    return bill

def add_cheese(bill):
    cheese = input("\nWould you like to add extra cheese? Type Yes or No: ").lower()
    if cheese == "yes":
        bill += cheese_price
    elif cheese != "no":
        print("\nInvalid input. Please type 'Yes' or 'No'.")
        return add_cheese(bill)
    return bill

def order_more_pizzas():
    more = input("\nWould you like to order another pizza? Type Yes or No: ").lower()
    if more == "yes":
        return True
    elif more == "no":
        return False
    else:
        print("\nInvalid input. Please type 'Yes' or 'No'.")
        return order_more_pizzas()

def get_customer_details():
    print("\nPlease enter your details for the order:")
    name = input("Name: ")
    phone = input("Phone Number: ")
    address = input("Delivery Address: ")
    return name, phone, address

def generate_order_id():
    return random.randint(1000, 9999)

def print_order_summary(order_details):
    print("\nOrder Summary:")
    for i, order in enumerate(order_details):
        print(f"Pizza {i + 1}:")
        print(f"  Size: {order['size']}")
        print(f"  Pepperoni: {'Yes' if order['pepperoni'] else 'No'}")
        print(f"  Extra Cheese: {'Yes' if order['cheese'] else 'No'}")
        print(f"  Price: ${order['price']}")

def main():
    print_welcome_message()
    print_pizza_menu()
    print_add_ons()

    customer_name, customer_phone, customer_address = get_customer_details()
    order_details = []
    total_bill = 0

    while True:
        if get_order():
            pizza_size = get_pizza_size()
            bill = calculate_pizza_price(pizza_size)
            pepperoni = False
            extra_cheese = False

            # Adding Pepperoni
            add_pep = input("\nWould you like to add pepperoni to your pizza? Type Yes or No: ").lower()
            if add_pep == "yes":
                if pizza_size == "S":
                    bill += s_pep
                elif pizza_size in ["M", "L"]:
                    bill += l_m_pep
                pepperoni = True
            elif add_pep != "no":
                print("\nInvalid input. Please type 'Yes' or 'No'.")

            # Adding Cheese
            add_cheese = input("\nWould you like to add extra cheese? Type Yes or No: ").lower()
            if add_cheese == "yes":
                bill += cheese_price
                extra_cheese = True
            elif add_cheese != "no":
                print("\nInvalid input. Please type 'Yes' or 'No'.")

            print(f"\nYour total bill for this pizza is: ${bill}.")
            time.sleep(1)

            order_details.append({
                'size': pizza_size,
                'pepperoni': pepperoni,
                'cheese': extra_cheese,
                'price': bill
            })

            total_bill += bill

            if not order_more_pizzas():
                break
        else:
            break

    if order_details:
        order_id = generate_order_id()
        print_order_summary(order_details)
        print(f"\nCustomer Name: {customer_name}")
        print(f"Phone Number: {customer_phone}")
        print(f"Delivery Address: {customer_address}")
        print(f"Order ID: {order_id}")
        print(f"\nYour total bill is: ${total_bill}.\n")
        print("Thank you for ordering from Python Pizza! Your delicious pizza will be delivered shortly.")

# Prices for pizzas and add-ons
s_pizza = 15
m_pizza = 20
l_pizza = 25
s_pep = 2
l_m_pep = 3
cheese_price = 1

# Start the pizza ordering process
main()
