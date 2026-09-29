banner=r"""

 _____ ___   ___  ____     ____ ___  _   _ ____ _____ 
|  ___/ _ \ / _ \|  _ \   / ___/ _ \| | | |  _ \_   _|
| |_ | | | | | | | | | | | |  | | | | | | | |_) || |  
|  _|| |_| | |_| | |_| | | |__| |_| | |_| |  _ < | |  
|_|   \___/ \___/|____/   \____\___/ \___/|_| \_\|_|  
 
"""



greeting=r"""

_   _| | | |  / \  | \ | | |/ / \ \ / / _ \| | | |
  | | | |_| | / _ \ |  \| | ' /   \ V / | | | | | |
  | | |  _  |/ ___ \| |\  | . \    | || |_| | |_| |
  |_| |_| |_/_/   \_\_| \_|_|\_\   |_| \___/ \___/ 
  
"""



feedback_box=r"""
 _____ _____ _____ ____  ____    _    ____ _  __  ____   _____  __
|  ___| ____| ____|  _ \| __ )  / \  / ___| |/ / | __ ) / _ \ \/ /
| |_  |  _| |  _| | | | |  _ \ / _ \| |   | ' /  |  _ \| | | \  / 
|  _| | |___| |___| |_| | |_) / ___ \ |___| . \  | |_) | |_| /  \ 
|_|   |_____|_____|____/|____/_/   \_\____|_|\_\ |____/ \___/_/\_

"""



info=r"""

| |   | ____|_   _/ ___|   / ___|  _ \| ____|  / \|_   _| ____|
| |   |  _|   | | \___ \  | |   | |_) |  _|   / _ \ | | |  _|  
| |___| |___  | |  ___) | | |___|  _ <| |___ / ___ \| | | |___ 
|_____|_____| |_| |____/   \____|_| \_\_____/_/   \_\_| |_____|

"""


visit=r"""
__   _(_)___(_) |_    __ _  __ _  __ _(_)_ __  
\ \ / / / __| | __|  / _` |/ _` |/ _` | | '_ \ 
 \ V /| \__ \ | |_  | (_| | (_| | (_| | | | | |
  \_/ |_|___/_|\__|  \__,_|\__, |\__,_|_|_| |_|
                           |___/              
"""

employee=r""" 
_____ __  __ ____  _     _____   _______ _____   _____ _   _ ____  
| ____|  \/  |  _ \| |   / _ \ \ / / ____| ____| | ____| \ | |  _ \ 
|  _| | |\/| | |_) | |  | | | \ V /|  _| |  _|   |  _| |  \| | | | |
| |___| |  | |  __/| |__| |_| || | | |___| |___  | |___| |\  | |_| |
|_____|_|  |_|_|   |_____\___/ |_| |_____|_____| |_____|_| \_|____/ 
"""

welcome_user=r"""
/ ___|| | | / ___\ \      / / \  / ___|  / \|_   _|/ \  |  \/  |
\___ \| | | \___ \\ \ /\ / / _ \| |  _  / _ \ | | / _ \ | |\/| |
 ___) | |_| |___) |\ V  V / ___ \ |_| |/ ___ \| |/ ___ \| |  | |
|____/ \___/|____/  \_/\_/_/   \_\____/_/   \_\_/_/   \_\_|  |_|
"""

import sqlite3

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Connect or create the database file
conn = sqlite3.connect('foodcourt.db')
cursor = conn.cursor()

# Create tables for profiles and orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city TEXT,
    country TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    profile_id INTEGER,
    item TEXT,
    quantity INTEGER,
    FOREIGN KEY (profile_id) REFERENCES profiles(id)
)
''')

conn.commit()

def save_profile(profile):
    cursor.execute('''
    INSERT INTO profiles (name, age, city, country) VALUES (?, ?, ?, ?)
    ''', (profile['NAME'], profile['AGE'], profile['CITY'], profile['COUNTRY']))
    conn.commit()
    return cursor.lastrowid  # Return the profile ID for linking orders

def save_order(profile_id, order_dict):
    for item, quantity in order_dict.items():
        cursor.execute('''
        INSERT INTO orders (profile_id, item, quantity) VALUES (?, ?, ?)
        ''',(profile_id, item, quantity))
    conn.commit()


menu= {
    "Pizza slice":75,
    "Burger with fries":90,
    "Chicken teriyaki bowl":110,
    "Vegetable stir-fry":50,
    "Fish and chips":120,
    "Taco salad":80,
    "Grilled cheese sandwich":70,
    "Hot dog":40,
    "Calzone":100,
    "Chocolate chip cookie":150,
    "Spring rolls":50,
    "Sandwich wrap":50,
    "Pasta Alfredo":120,
    "Fried chicken":150,
    "Salad bowl":40,
    "Shawarma":70,
    "Paneer tikka":80,
    "Ice cream cone":30,
    "Smoothie":50,
    "Fruit salad":40
}

def place_order(profile_id=None):
    print(banner)
    cust_name=input('Enter customer name\n')
    see_menu=input('Do you want to refer menu?"yes"or"no"\n').lower()
    if see_menu=='yes':
        for key,value in menu.items():
            print(key,value,'')
    print('\n'*4)
    order_dict={}
    place='yes'
    bill=0
    while place=='yes':
        order=input('Enter your order from the menu list')
        if order not in menu:
            print(f'Sorry  the item {order} is not in the menu')
            continue
        quant=int(input('Enter the quantity'))

        order_dict[order]=quant
        place=input('Do you want to place more order?"yes"or"no"').lower()
    print('\n'*4)
    print('Thank you.Your order has been placed as follows:')
    for key,value in order_dict.items():
        print(key,value,'')
    print('\n' * 4)
    for item,quant in order_dict.items():
        bill+=menu[item] * quant
    print(f'Dear {cust_name} your bill is:{bill}')
    print('\n'*4)
    if profile_id:
        save_order(profile_id, order_dict)


def create_profile():
    print(info)
    profile={}
    name=input('Enter your name').upper()
    age=int(input('Enter your age'))
    city=input('Enter your city name').upper()
    country = input('Enter your country name').upper()
    profile['NAME']=name
    profile['AGE']=age
    profile['COUNTRY']=country
    profile['CITY']=city
    print('Hurray! Your profile has been created and saved successfully.')
    see_profile=input('Want to see your profile?').lower()
    if see_profile=='yes':
        for key ,value in profile.items():
            print(key,value,'  ',end='  ')
    profile_id = save_profile(profile)
    return profile_id


def feedback():
    print(feedback_box)
    print('Dear customer,kindly provide us rating')
    give_rating=input('Do you want to give us rating?\n')
    if give_rating=='yes':
        print('\n' * 4)
        rating=float(input('How you like the service provided?\nGive ratings out of 5.0'))
        print('\n' * 4)
        print(f'FOOD COURT RATING:{rating}/5.0')
        print(greeting)

category=input('Are you user OR employee?\nkindly specify\n').lower()
if category=='user':
    print(welcome_user)
    more_order='yes'
    while more_order=='yes':
        print('\n'*7)
        new_user=input('Are you a new user?')
        if new_user=='yes':

            profile_id=create_profile()
            print('\n' * 4)
            place_order(profile_id)
            print('\n' * 4)
            feedback()
            print('\n' * 4)
        else:
            place_order()
            print('\n' * 4)
            feedback()
            print('\n' * 4)
        print('\n'*4)
        more_order=input('Is there any other user OR do you want to proceed again?\n"yes"OR"no": ')
    print(visit)



if category=='employee':
    print(employee)
    conn = sqlite3.connect('foodcourt.db')
    cursor = conn.cursor()

    should_continue='yes'

    while should_continue == 'yes':
        print(
            '1.FETCH PROFILES\n2.FETCH ORDERS\n3.POPULAR MENU ITEM VISUALIZATION\n4.DISTRIBUTION OF CUSTOMERS\n5.ORDER BILL DISTRIBUTION')
        fetch = input('Kindly select the appropriate option by number: ').strip()

        if fetch == '1':
            cursor.execute("SELECT * FROM profiles")
            profiles = cursor.fetchall()
            print("Profiles:")
            for p in profiles:
                print(p)

        elif fetch == '2':
            cursor.execute("SELECT * FROM orders")
            orders = cursor.fetchall()
            print("\nOrders:")
            for o in orders:
                print(o)

        elif fetch == '3':
            cursor.execute("SELECT item, SUM(quantity) FROM orders GROUP BY item ORDER BY SUM(quantity) DESC")
            order_data = cursor.fetchall()
            items = [row[0] for row in order_data]
            quantities = [row[1] for row in order_data]
            plt.figure(figsize=(10, 6))
            plt.bar(items, quantities, color='skyblue')
            plt.title('Most Popular Menu Items')
            plt.xlabel('Menu Item')
            plt.ylabel('Total Quantity Ordered')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif fetch == '4':
            cursor.execute("SELECT city, COUNT(*) FROM profiles GROUP BY city")
            city_data = cursor.fetchall()
            cities = [row[0] for row in city_data]
            counts = [row[1] for row in city_data]
            plt.figure(figsize=(8, 8))
            plt.pie(counts, labels=cities, autopct='%1.1f%%', startangle=140)
            plt.title('Customer Distribution by City')
            plt.show()

        elif fetch == '5':
            cursor.execute("SELECT profile_id, SUM(quantity) FROM orders GROUP BY profile_id")
            bills = cursor.fetchall()
            bill_values = []
            for profile_id, _ in bills:
                cursor.execute("SELECT item, quantity FROM orders WHERE profile_id=?", (profile_id,))
                orders_for_profile = cursor.fetchall()
                total_bill = 0
                for item, quantity in orders_for_profile:
                    price = menu.get(item, 0)
                    total_bill += price * quantity
                bill_values.append(total_bill)

            plt.figure(figsize=(8, 6))
            plt.hist(bill_values, bins=10, color='lightgreen', edgecolor='black')
            plt.title('Distribution of Customer Bills')
            plt.xlabel('Total Bill Amount')
            plt.ylabel('Number of Orders')
            plt.show()

        else:
            print("Invalid input, please enter a number between 1 and 5.")

        print('\n' * 4)
        should_continue = input('Do you want to continue further? "yes" OR "no"').lower()

    print(visit)





























