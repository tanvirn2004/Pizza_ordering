from price_lists import s_pizza, m_pizza, l_pizza, s_pep, l_m_pep, cheese_price

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
