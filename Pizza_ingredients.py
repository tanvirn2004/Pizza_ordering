from price_lists import s_pep, l_m_pep, cheese_price


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
