# 🍔 Food Court Management System

---

## 💡 Project Overview

The **Food Court Management System** is a console-based application designed to simulate the operations of a food court. It provides functionalities for both **Users (Customers)** to place orders and give feedback, and **Employees** to manage and analyze customer profiles and order data.

The system uses an **SQLite database** to persistently store customer profiles and their corresponding orders. It also features **data visualization** using **Matplotlib** to help employees gain insights into popular menu items, customer demographics, and order bill distribution.

---

## ✨ Features

### For Users (Customers)

* **Create Profile:** New users can create a profile (name, age, city, country) which is saved to the database.
* **View Menu:** Customers can view the complete menu with prices before placing an order.
* **Place Order:** Customers can select multiple items and quantities from the menu.
* **Generate Bill:** The system calculates and displays the total bill amount.
* **Provide Feedback:** Users can rate the service after placing an order.

### For Employees

* **Data Retrieval:** Fetch and view all stored customer **Profiles** and **Orders** from the database.
* **Data Visualization (Matplotlib):** Employees can analyze data through visual charts:
    * **Popular Menu Item:** A bar chart showing the most frequently ordered items.
    * **Customer Distribution:** A pie chart illustrating the distribution of customers by city.
    * **Order Bill Distribution:** A histogram visualizing the range of total bill amounts.

---

## 🛠️ Technologies/Tools Used

* **Python 3.x:** The core programming language.
* **SQLite:** A lightweight, file-based database for persistent storage of profiles and orders.
* **Matplotlib:** A plotting library used for generating data visualizations and analytics.

---

## 💻 Steps to Install & Run the Project

### Prerequisites

You must have **Python 3.x** installed on your system.

1.  **Save the Code:**
    * Save the provided Python code into a file named, for example, `foodcourt_system.py`.

2.  **Install Required Libraries:**
    * The project requires the `matplotlib` library for visualization. Open your terminal or command prompt and install it using pip:

    ```bash
    pip install matplotlib
    ```

3.  **Run the Application:**
    * Navigate to the directory where you saved the Python file in your terminal and run the script:

    ```bash
    python foodcourt_system.py
    ```

    *The system will automatically create the `foodcourt.db` SQLite database file and the necessary tables upon its first run.*

---

## 🧪 Instructions for Testing

When you run the script, you will be prompted to specify your role: **`user` OR `employee`**.

### 1. Testing as a User

This simulates a customer placing an order.

1.  Enter **`user`** when prompted for the category.
2.  Follow the prompts to enter **`yes`** for a new user, create your profile, and place an order by specifying the item name and quantity.
3.  Complete the process by providing feedback.
4.  Repeat this process a few times to generate sufficient data for employee analysis.

### 2. Testing as an Employee

This simulates management accessing data and analytics.

1.  Enter **`employee`** when prompted for the category.
2.  You will see the following menu of options:

    | Option | Description | Output Type |
    | :--- | :--- | :--- |
    | **1** | FETCH PROFILES | Text output |
    | **2** | FETCH ORDERS | Text output |
    | **3** | POPULAR MENU ITEM VISUALIZATION | Bar Chart (Matplotlib) |
    | **4** | DISTRIBUTION OF CUSTOMERS | Pie Chart (Matplotlib) |
    | **5** | ORDER BILL DISTRIBUTION | Histogram (Matplotlib) |

3.  Select an option (1-5) and review the resulting data or visualization window.
4.  Enter **`yes`** when prompted to continue testing more features, or **`no`** to exit.
