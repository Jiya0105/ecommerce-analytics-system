# 🛒 E-Commerce Analytics System

## 📌 Project Overview

The **E-Commerce Analytics System** is an end-to-end data analytics project developed using **Python, Pandas, SQLite, and SQL**. The system generates realistic e-commerce datasets, introduces intentional inconsistencies, cleans and validates the data, loads it into a relational database, performs advanced SQL analytics, and generates business reports.

The project demonstrates the complete data analytics workflow—from raw data generation to business insight generation.

---

# 🎯 Objective

To design and develop an end-to-end e-commerce analytics system that:

- Generates realistic e-commerce datasets
- Introduces intentional inconsistencies
- Cleans and validates data using Pandas
- Ensures referential integrity across multiple tables
- Loads cleaned data into an SQLite database
- Performs advanced SQL analysis
- Generates business reports automatically

---

# 🛠 Technologies Used

- Python 3.x
- Pandas
- Faker
- SQLite3
- SQL
- VS Code

---

# 📂 Project Structure

```
ECOMMERCE-ANALYTICS-SYSTEM
│
├── data
│   ├── raw
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   └── order_items.csv
│   │
│   └── cleaned
│       ├── customers_clean.csv
│       ├── products_clean.csv
│       ├── orders_clean.csv
│       └── order_items_clean.csv
│
├── output
│   ├── total_revenue.csv
│   ├── revenue_by_category.csv
│   ├── top_customers.csv
│   ├── top_products.csv
│   ├── customer_ranking.csv
│   ├── running_revenue.csv
│   ├── cohort_analysis.csv
│   └── repeat_customers.csv
│
├── script
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_database.py
│   └── report_cli.py
│
├── sql
│   ├── schema.sql
│   ├── aggregations.sql
│   ├── window_functions.sql
│   └── cohort_analysis.sql
│
├── ecommerce.db
└── README.md
```

---

# 📊 Dataset

The project generates four datasets automatically:

### Customers

Contains customer information such as:

- Customer ID
- Name
- Email
- City
- Signup Date

### Products

Contains product information:

- Product ID
- Product Name
- Category
- Price

### Orders

Contains order details:

- Order ID
- Customer ID
- Order Date
- Payment Method
- Order Status

### Order Items

Contains purchased products:

- Item ID
- Order ID
- Product ID
- Quantity

---

# ⚠ Intentional Data Issues

The generated dataset includes intentional inconsistencies for cleaning practice:

- Missing email addresses
- Duplicate records
- Invalid customer IDs
- Negative prices
- Negative quantities
- Future order dates
- Missing values

---

# 🧹 Data Cleaning

The cleaning process performs:

- Removing duplicate records
- Filling missing values
- Correcting data types
- Removing negative prices
- Removing negative quantities
- Removing future dates
- Validating customer IDs
- Validating product IDs
- Validating order IDs

Cleaned datasets are stored in:

```
data/cleaned/
```

---

# 🗄 Database

SQLite database used:

```
ecommerce.db
```

Tables:

- Customers
- Products
- Orders
- Order_Items

---

# 📈 SQL Analytics

The project performs:

## Joins

- Customers ↔ Orders
- Orders ↔ Order Items
- Products ↔ Order Items

## Aggregations

- Total Revenue
- Revenue by Category
- Top Customers
- Top Products

## Window Functions

- Customer Ranking
- Running Revenue

## CTE

- First Purchase Analysis

## Cohort Analysis

- Monthly Customer Cohorts
- Repeat Customers

---

# 📑 Reports Generated

The following reports are generated automatically:

- Total Revenue
- Revenue by Category
- Top Customers
- Top Products
- Customer Ranking
- Running Revenue
- Cohort Analysis
- Repeat Customers

Reports are saved inside:

```
output/
```

---

# ▶ How to Run

## Step 1

Install dependencies

```bash
pip install pandas faker
```

---

## Step 2

Generate Dataset

```bash
python script/generate_data.py
```

---

## Step 3

Clean Dataset

```bash
python script/clean_data.py
```

---

## Step 4

Load Database

```bash
python script/load_database.py
```

---

## Step 5

Generate Reports

```bash
python script/report_cli.py
```

---

# 📁 Output

The system automatically generates:

- Raw CSV files
- Cleaned CSV files
- SQLite Database
- Analytical Reports

---

# 📌 Features

- Automatic dataset generation
- Data validation
- Data cleaning
- SQLite database integration
- SQL analytics
- Revenue analysis
- Customer analysis
- Product analysis
- Window functions
- Cohort analysis
- Report generation

---

# 🚀 Future Enhancements

- Interactive Dashboard using Power BI
- Streamlit Web Application
- MySQL/PostgreSQL Support
- Sales Forecasting using Machine Learning
- Customer Segmentation (RFM Analysis)
- Automated Email Reporting

---

# 👩‍💻 Author

**Jiya**

B.Tech Computer Science Engineering

---

# 📄 License

This project is created for educational purposes as part of an academic data analytics assignment.
