# Initial Resturant menu
resturant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Task 1: Add a new category called "Beverages" with at least two items.
resturant_menu["Beverages"] = {"Coke": 1.99, "Coffee": 2.50}

# Task 2: Update the price of "Steak" to 17.99.
resturant_menu["Main Course"]["Steak"] = 17.99

# Task 3: Remove "Bruschetta" from "Starters"
resturant_menu["Starters"].pop("Bruschetta")

# Updated Menu
print(resturant_menu)