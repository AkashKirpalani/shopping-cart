# shopping_cart.py
# Works Cited: https://github.com/prof-rossetti/intro-to-python/
import datetime


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" 
#$12,000.71

selected_products = []

id = ""
# TODO: write some Python code here to produce the desired output

number = 0
subtotal_price = 0
selected_ids = []

while id != "DONE": 
    id = input("Please input product identifier: ")
    if(id == "DONE"):
        break
    if(id.isdigit()): 
        int_id = int(id)
        if(int_id < 0):
            print("Hey, are you sure that product id is correct? Please try again!")
        if(int_id > 20):
            print("Hey, are you sure that product id is correct? Please try again!")
        else:
            selected_ids.append(id)

    else: 
         print("Hey, are you sure that product id is correct? Please try again!")


print("-----------------------------------")
print("WHOLEPAYCHECK GROCERY")
print("WWW.WHOLEPAYCHECK.COM")
print("-----------------------------------")
d = datetime.datetime.today()
print("CHECK OUT AT: ", d.strftime("%Y-%m-%d %I:%M %p"))
print("-----------------------------------")
print("SELECTED PRODUCTS:")
for id in selected_ids:  
    matching_products = [p for p in products if str(p["id"]) == str(id)]
    matching_product = matching_products[0]
    subtotal_price =  subtotal_price + matching_product["price"]
    print("...", matching_product["name"], "", "("+str(to_usd(matching_product["price"]))+")")

print("-----------------------------------")
print("SUBTOTAL: ", to_usd(subtotal_price))
tax = subtotal_price * 0.0875
print("TAX: ", to_usd(tax))
total_price = subtotal_price + tax
print("TOTAL PRICE: ", to_usd(total_price))
print("-----------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("-----------------------------------")





