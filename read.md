# Python Pizza Ordering System

This project is an automated pizza ordering system developed in Python. It allows customers to order pizzas of various sizes, choose additional toppings, and provides a summary with the total cost for easy management of orders.

## Project Structure

- **main.py**: Main program file to run the pizza ordering system.
- **order.py**: Contains functions related to order management, such as displaying the pizza menu, taking the pizza order, and selecting the pizza size.
- **order_details.py**: Manages customer details, order summaries, and generates unique order IDs.
- **Pizza_ingredients.py**: Contains functions to add optional ingredients (pepperoni and cheese) to the pizza.
- **price_lists.py**: Defines the base prices for pizzas and additional ingredients.

## How to Use

1. Run the `main.py` file to start the pizza ordering program.
2. The program will:
   - Display a welcome message.
   - Show the available pizza sizes and their prices.
   - Prompt the user to order a pizza, choose its size, and select add-ons (pepperoni or extra cheese).
3. After selecting options, the program will:
   - Display an order summary.
   - Show the total bill for the order.
   - Generate a unique order ID.

## Detailed Module Documentation

### main.py
- **Functions**:
  - `main()`: Initializes the ordering process, gathers user choices, and generates an order summary with the final bill.

### order.py
- **Functions**:
  - `print_pizza_menu()`: Displays available pizza sizes and prices.
  - `print_add_ons()`: Shows add-on options and their respective prices.
  - `get_order()`: Asks the user if they want to place an order.
  - `get_pizza_size()`: Prompts the user to select a pizza size.

### order_details.py
- **Functions**:
  - `print_welcome_message()`: Displays a welcome message.
  - `calculate_pizza_price(size)`: Returns the price based on pizza size.
  - `get_customer_details()`: Collects customer name, phone, and address for delivery.
  - `generate_order_id()`: Generates a random order ID for each new order.
  - `print_order_summary(order_details)`: Prints the details of each pizza in the order.

### Pizza_ingredients.py
- **Functions**:
  - `add_pepperoni(size, bill)`: Adds the cost of pepperoni based on pizza size.
  - `add_cheese(bill)`: Adds the cost of extra cheese to the bill.

### price_lists.py
- **Constants**:
  - `s_pizza`, `m_pizza`, `l_pizza`: Prices for small, medium, and large pizzas.
  - `s_pep`, `l_m_pep`: Prices for pepperoni based on pizza size.
  - `cheese_price`: Price for adding extra cheese.

## Example Workflow

1. The user starts the program and is greeted with a welcome message.
2. They view the pizza menu and decide to order a pizza.
3. They select the pizza size, choose optional toppings, and confirm the order.
4. The program calculates the cost, displays the summary, and thanks the customer.

## Requirements

- Python 3.x

## Running the Project

```bash
python main.py
