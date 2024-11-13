from price_lists import s_pep, l_m_pep, cheese_price
from order import get_order, print_add_ons, print_pizza_menu, get_pizza_size
from order_details import time,print_order_summary, print_welcome_message, generate_order_id,calculate_pizza_price,get_customer_details, order_more_pizzas
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
            add_pep = input("\nWould you like to add pepperoni to your pizza? Type Yes or No: ").lower()
            if add_pep == "yes":
                if pizza_size == "S":
                    bill += s_pep
                elif pizza_size in ["M", "L"]:
                    bill += l_m_pep
                pepperoni = True
            elif add_pep != "no":
                print("\nInvalid input. Please type 'Yes' or 'No'.")
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

main()
