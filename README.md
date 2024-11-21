
# BestBuy Store Application

A Python-based application to manage products, promotions, and orders for a fictional store. Users can view product listings, check the total quantity of items in the store, place orders, and more.
This project demonstrates the concept of OOP (Object-Oriented Programming

## Features

- **List Products**: View all available products in the store.
- **Show Total Amount**: Check the total quantity of all items in the store.
- **Make an Order**: Place an order by selecting products.
- **Promotions**: Apply special promotions like discounts and bundle deals.

## Product Promotion System

This system allows the application of different promotions to products. The core class is `Promotion`, an abstract base class, which defines the structure for applying discounts. Three types of promotions are implemented:

- **SecondHalfPrice**: Every second product is at half price.
- **ThirdOneFree**: Every third product is free.
- **PercentDiscount**: A percentage discount is applied to the total price.

### Product Types:
- **Product**: Basic product with quantity and price.
- **LimitedProduct**: A product with a maximum order limit.
- **NonStockedProduct**: A product that does not have a stock quantity but can still be ordered.

Each product can have associated promotions, and the total price of an order reflects the discount, if applicable.

### **Store**
Represents a store that manages products and processes orders. It includes:
- Adding, removing, and retrieving products.
- Calculating total quantities and total costs of orders.
- Validating orders to ensure they meet quantity and order limits.

### Helper Functions

- **`print_products`**: Displays active products in the store and returns them as a dictionary for ordering.
- **`order_product`**: Prompts the user to select products and specify quantities to create an order.
- **`validate_order_util`**: Validates the order and processes the payment if successful.

## 🛠️ Technologies Used  
- **Python**  


## 🚀 Installation  

1. **Clone the repository**:  
   ```bash  
   git git@github.com:masterschool-weiterbildung/bestbuy.git  
   cd weiterbildung-best-buy 
   ```  

2. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```  

3. **Run the application**:  
   ```bash  
   python main.py  
   ```  

## 📁 Project Structure  
```plaintext  
weiterbildung-best-buy/
│
├── .github/
│   └── workflows/               # GitHub workflow configurations
│
├── __pycache__/                 # Python bytecode cache (auto-generated)
│
├── tests/                       # Unit tests and test cases
│
├── .gitignore                   # Files to ignore in Git
├── main.py                      # Entry point of the program
├── products.py                  # Defines product classes like Product, LimitedProduct, NonStockedProduct
├── promotions.py                # Defines promotion classes like Promotion, SecondHalfPrice, etc.
├── store.py                     # Defines Store class for managing products
├── util.py                      # Utility functions used throughout the project
```  
