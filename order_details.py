import time
import random

from price_lists import s_pizza, m_pizza, l_pizza

def print_welcome_message():
    print("Congratulations! You've got a job at Python Pizza! Your first task is to build an automatic pizza ordering program.")
    time.sleep(1)
    print("Welcome to Python Pizza, the best pizza in town!\n")
    time.sleep(1)
def calculate_pizza_price(size):
    if size == "S":
        return s_pizza
    elif size == "M":
        return m_pizza
    elif size == "L":
        return l_pizza


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


    while True:
        phone = input("Phone Number: ")
        # Check if the phone number is exactly 11 digits and contains only numbers
        if phone.isdigit() and len(phone) == 11:
            break
        else:
            print("\nInvalid input. Please enter a valid 11-digit phone number.")

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