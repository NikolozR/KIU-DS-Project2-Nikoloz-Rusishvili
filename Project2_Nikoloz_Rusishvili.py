import pandas as pd
import os

# Task 1: Start
print("====================== TASK 1 START ======================")
# Part A: Data Loading and Validation
customers_df = pd.read_csv('data/original/customers.csv')
print("Validating Customers CSV Reading...")
print(f"It should be 205 rows, there is {len(customers_df)}. {"Valid" if 205 == len(customers_df) else "Not Valid"}")
print("====================================================================================================================")

products_df = pd.read_csv('data/original/products.csv')
print("Validating Products CSV Reading...")
print(f"It should be 50 rows, there is {len(products_df)}. {"Valid" if 50 == len(products_df) else "Not Valid"}")
print("====================================================================================================================")

transactions_df = pd.read_csv('data/original/transactions.csv')
print("Validating Products CSV Reading...")
print(f"It should be 508 rows, there is {len(transactions_df)}. {"Valid" if 508 == len(transactions_df) else "Not Valid"}")
print("====================================================================================================================")


# Part B: Data Exploration
# Function to see basic information about data frame
def basic_information(df: pd.DataFrame, name_of_df):
    print(f"First 5 rows of {name_of_df} data frame:")
    print(df.head())
    print("====================================================================================================================")
    print(f"Last 5 rows of {name_of_df} data frame:")
    print(df.tail())
    print("====================================================================================================================")
    print(f"Shape of {name_of_df} data frame:")
    print(df.shape)
    print("====================================================================================================================")
    print(f"Columns and types of {name_of_df} data frame:")
    print(df.dtypes)
    print("====================================================================================================================")
    print(f"Memory usage of {name_of_df} data frame:")
    print(df.memory_usage())
    print("====================================================================================================================")

basic_information(customers_df, "Customers")
basic_information(products_df, "Products")
basic_information(transactions_df, "Transactions")

# Function to see summary of all columns (categorical or numerical) of data frame
def statistical_summary(df: pd.DataFrame, name_of_df):
    print(f"======Statistical Summary for {name_of_df} data frame======")
    columns_dtypes = df.dtypes
    for column_name, dtype in columns_dtypes.items():
        print(f"Statistical Summary for column '{column_name}'")
        if dtype == 'object' or dtype == 'category':
            print(df[column_name].describe(include='object')) # type: ignore
            print(f"Unique value count: {df[column_name].nunique()}")
        else:
            print(df[column_name].describe())
        print("====================================================================================================================")

statistical_summary(customers_df, "Customers")
statistical_summary(products_df, "Products")
statistical_summary(transactions_df, "Transactions")

# Function to analyze missing values and duplicates for data frame
def data_quality_check(df: pd.DataFrame, name_of_df):
    print(f"Missing values in each column for {name_of_df} data frame:")
    print(df.isna().sum())
    print("====================================================================================================================")
    print(f"Duplicated rows for {name_of_df} data frame:")
    print(df[df.duplicated()])
    print(f"Total number of duplicate rows: {df.duplicated().sum()}")
    print("====================================================================================================================")
    print(f"Identifying unusual values and patterns in {name_of_df} data frame:")
    
    for col in df.select_dtypes(include='object').columns:
        print(f"\nUnique values in '{col}' column:")
        print(df[col].value_counts())
        print(f"  -> Check for inconsistent naming, formatting, or whitespace issues")
    
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        print(f"\nValue range for '{col}' column:")
        print(f"  Min: {df[col].min()}, Max: {df[col].max()}, Mean: {df[col].mean():.2f}")
        print(f"  -> Check if min/max values seem realistic (negatives, outliers, etc.)")
    
    print("====================================================================================================================")



data_quality_check(customers_df, "Customers")
data_quality_check(products_df, "Products")
data_quality_check(transactions_df, "Transactions")

# Part C: Basic Analysis
def customer_analysis():
    df = customers_df.copy()
    print("Customers number per each country:")
    print(df.groupby(by='country').count()['customer_id'])
    print("====================================================================================================================")
    print(f"Minimum age: {df['age'].min()}")
    print("====================================================================================================================")
    print(f"Maximum age: {df['age'].max()}")
    print("====================================================================================================================")
    print(f"Mean age: {pd.to_numeric(df['age'], errors='coerce').dropna().mean():.2f}")
    print("====================================================================================================================")
    print(f"Median age: {pd.to_numeric(df['age'], errors='coerce').dropna().median():.2f}")
    print("====================================================================================================================")
    df['registration_date'] = pd.to_datetime(df['registration_date'])
    df['month'] = df['registration_date'].dt.month_name()
    print("Month with most new registrations:")
    print(df['month'].value_counts().head(1))
    print("====================================================================================================================")

def product_analysis():
    df = products_df.copy()
    print("Products in each category:")
    print(df.groupby(by='category').count()['product_id'])
    print("====================================================================================================================")
    df['price_clean'] = df['price'].abs()
    print("Average price per category:")
    print(df.groupby(by="category")['price_clean'].mean())
    print("====================================================================================================================")
    print("Products that are out of stock:")
    print(df[df['stock'] == 0]['product_name'])
    print("====================================================================================================================")

def transaction_analysis():
    df = transactions_df.copy()
    df['payment_method'] = df["payment_method"].str.title()
    print("Transaction number per payment method:")
    print(df.groupby(by='payment_method').count()['transaction_id'])
    print("====================================================================================================================")
    print("Most popular product by transactions:")
    print(df.groupby(by="product_id").count()['transaction_id'].idxmax())
    print("====================================================================================================================")
    print("Customer that made the most purchases:")
    print(df.groupby(by="customer_id").count()['transaction_id'].idxmax())
    print("====================================================================================================================")


customer_analysis()
product_analysis()
transaction_analysis()

# Task 1: End
print("====================== TASK 1 END ======================")


# Task 2: Start
print("====================== TASK 2 START ======================")
# Part A: Identify Data Quality Issues

# Customers.csv
print("====================================================================================================================")
print(customers_df[customers_df['email'].isna()]['customer_id'].tolist())
print(customers_df[customers_df.duplicated()]['customer_id'].tolist())
print(customers_df[pd.to_numeric(customers_df['age'], errors='coerce').isna()]['customer_id'].tolist())
print(customers_df.query("country == 'US' or country == 'USA'")['customer_id'].tolist())
'''
    1. Missing Values
        There are 20 missing values with email column, specifically these costumers:
        ['C001', 'C003', 'C004', 'C006', 'C009', 'C024', 'C027', 'C033', 'C037', 'C071', 'C102', 'C103', 'C111', 'C134', 'C143', 'C150', 'C152', 'C163', 'C174', 'C192']
    2. Duplicated Rows
        There are 4 duplicated rows, specifically these costumers' rows:
        ['C008', 'C115', 'C048', 'C114']
    3. Inconsistent data types
        There are 15 values in age column that are given in invalid type (XX years), specifically for these customers:
        ['C010', 'C031', 'C053', 'C073', 'C083', 'C091', 'C103', 'C126', 'C129', 'C130', 'C133', 'C150', 'C198', 'C200', 'C034']
    4. Inconsistent country names
        For 'United States' case, 14 customer rows use "US" or "USA", specifically:
        ['C026', 'C084', 'C092', 'C102', 'C115', 'C125', 'C145', 'C146', 'C157', 'C166', 'C172', 'C176', 'C183', 'C115']
'''
print("====================================================================================================================")

# Products.csv
print("====================================================================================================================")
print(products_df[products_df['price'].isnull()]['product_id'].tolist())
print(products_df.query("price < 0")['product_id'].tolist())
print(products_df[(products_df['product_name'].str.startswith(' ')) | (products_df['product_name'].str.endswith(' '))]['product_id'].to_list())
print(products_df[products_df['category'].str.match(r'^[a-z]')]['product_id'].to_list())
'''
    1. Missing Values
        There are 3 missing values in price column, specifically these products:
        ['P006', 'P010', 'P037']
    2. Negative Prices
        There are 3 negative values in price column, specifically these products:
        ['P005', 'P018', 'P030']
    3. Unrealistic Stock Values
        Possible unrealistic stock numbers are 11246, 11048, 5987, respectively these products:
        ['P002', 'P045', 'P050']  
    4. Whitespace around product names:
        There are 10 values under product_name column that has whitespace around them:
        ['P016', 'P029', 'P032', 'P035', 'P036', 'P037', 'P038', 'P043', 'P048', 'P050']
    5. Inconsistent category naming:
        There are 8 values under the category column that has inconsistent naming (first letter is not capitalized):
        ['P005', 'P014', 'P020', 'P032', 'P043', 'P046', 'P048', 'P050']
'''
print("====================================================================================================================")

# Transactions.csv
print("====================================================================================================================")
print(transactions_df[transactions_df['quantity'].isnull()]['transaction_id'].tolist())
print(transactions_df[transactions_df.duplicated()]['transaction_id'].to_list())
print(transactions_df[transactions_df['customer_id'].str[1:].astype(int) > 200]['transaction_id'].tolist())
print(transactions_df[pd.to_datetime(transactions_df['transaction_date']) > pd.Timestamp.today()]['transaction_id'].tolist())
print(transactions_df[transactions_df['payment_method'].str.isupper()]['transaction_id'].tolist())
'''
    1. Missing Values
        There are 16 missing values under quantity column:
        ['T040', 'T080', 'T089', 'T146', 'T151', 'T167', 'T217', 'T302', 'T327', 'T362', 'T364', 'T423', 'T448', 'T456', 'T482', 'T217']
    2. Duplicated Rows
        There are 6 duplicated rows
        ['T045', 'T037', 'T060', 'T304', 'T021', 'T217']
    3. Invalid customer_id references
        There are 10 invalid references under customer_id column:
        ['T031', 'T184', 'T240', 'T300', 'T316', 'T406', 'T424', 'T432', 'T457', 'T403']
    4. Future Dates
        There is only 1 future date:
        ['T492']
    5. Inconsistent payment_method naming:
        There are 20 values under column payment_method where values are written all uppercase:
        ['T015', 'T023', 'T102', 'T157', 'T178', 'T204', 'T228', 'T235', 'T255', 'T260', 'T274', 'T282', 'T290', 'T322', 'T344', 'T390', 'T428', 'T470', 'T478', 'T152']
'''
print("====================================================================================================================")
# Part B 

# Copy dfs to start cleaning in different instance
customers_df_cleaned = customers_df.copy()
products_df_cleaned = products_df.copy()
transactions_df_cleaned = transactions_df.copy()

# Handle Missing Values
customers_df_cleaned = customers_df_cleaned.dropna(subset=['email'])
products_df_cleaned['price'] = products_df_cleaned.groupby('category')['price'].transform(lambda x:x.fillna(x.median()))
transactions_df_cleaned['quantity'] = transactions_df_cleaned['quantity'].fillna(transactions_df_cleaned['quantity'].mode()[0])
'''
    Explanation:
    For emails dropping is the best choice since email is often the unique identifier, so we can not even replace them and also having them left empty would also be problem
    For price, since same category products have roughly same price --> we used median
    For quantity, playing safe, fitting with most common value for discrete value column
'''

# Remove Duplicates
customers_duplicate_removed = customers_df_cleaned.duplicated().sum()
# We do not need keep="first" because it does that by default
customers_df_cleaned = customers_df_cleaned.drop_duplicates(subset='customer_id')
products_duplicate_removed = products_df_cleaned.duplicated().sum()
products_df_cleaned = products_df_cleaned.drop_duplicates(subset='product_id')
transactions_duplicate_removed = transactions_df_cleaned.duplicated().sum()
transactions_df_cleaned = transactions_df_cleaned.drop_duplicates(subset='transaction_id')
print("====================================================================================================================")
print(f'Found {customers_duplicate_removed} duplicates for customers. \nFound {products_duplicate_removed} duplicates for products. \nFound {transactions_duplicate_removed} duplicates for transactions.')
print("====================================================================================================================")

# Fix Data Types
inconsistent_age_mask = pd.to_numeric(customers_df_cleaned['age'], errors='coerce').isna()
customers_df_cleaned.loc[inconsistent_age_mask, 'age'] = pd.to_numeric(customers_df_cleaned.loc[inconsistent_age_mask, 'age'].str.split(' ').str[0])
customers_df_cleaned['age'] = pd.to_numeric(customers_df_cleaned['age'])

customers_df_cleaned['registration_date'] = pd.to_datetime(customers_df_cleaned['registration_date'])
transactions_df_cleaned['transaction_date'] = pd.to_datetime(transactions_df_cleaned['transaction_date'])
print("====================================================================================================================")
print(f"If everything is numeric in quantity this should be 0: {pd.to_numeric(transactions_df_cleaned['quantity'], errors='coerce').isna().sum()}")
print(f"If everything is numeric in price this should be 0: {pd.to_numeric(products_df_cleaned['price'], errors='coerce').isna().sum()}")
print("====================================================================================================================")
# Standardize Values
customers_df_cleaned.loc[customers_df_cleaned.query('country == "US" or country == "USA"').index, 'country'] = "United States"
products_df_cleaned['product_name'] = products_df_cleaned['product_name'].str.strip()
customers_df_cleaned['email'] = customers_df_cleaned['email'].str.lower()

# Handle Outliers & Invalid Data
# Chose this kind of decision because absolute values are not far from other positive numbers, so we assume that negative sign was just technical mistake
products_df_cleaned['price'] = products_df_cleaned['price'].abs()
products_df_cleaned['stock'] = products_df_cleaned['stock'].clip(upper=500)
transactions_df_cleaned = transactions_df_cleaned[~(transactions_df_cleaned['customer_id'].str[1:].astype(int) > 200)]
transactions_df_cleaned = transactions_df_cleaned[~(pd.to_datetime(transactions_df_cleaned['transaction_date']) > pd.Timestamp.today())]

# It was not written in tasks but we need to do it:
products_df_cleaned['category'] = products_df_cleaned['category'].str.capitalize()
transactions_df_cleaned['payment_method'] = transactions_df_cleaned['payment_method'].str.title()


# Part C

# Create Cleaning Report
cleaning_report = pd.DataFrame({
    'Dataset': ['Customers', 'Products', 'Transactions'],
    'Original_Rows': [len(customers_df), len(products_df), len(transactions_df)],
    'Cleaned_Rows': [len(customers_df_cleaned), len(products_df_cleaned), len(transactions_df_cleaned)],
    'Rows_Removed': [
        len(customers_df) - len(customers_df_cleaned),
        len(products_df) - len(products_df_cleaned),
        len(transactions_df) - len(transactions_df_cleaned)
    ],
    'Missing_Before': [
        customers_df.isnull().sum().sum(),
        products_df.isnull().sum().sum(),
        transactions_df.isnull().sum().sum()
    ],
    'Missing_After': [
        customers_df_cleaned.isnull().sum().sum(),
        products_df_cleaned.isnull().sum().sum(),
        transactions_df_cleaned.isnull().sum().sum()
    ],
    'Duplicates_Removed': [
        customers_duplicate_removed,
        products_duplicate_removed,
        transactions_duplicate_removed
    ]
})
print("====================================================================================================================")
print(cleaning_report)
print("====================================================================================================================")


# 2. Verify Data Quality

# Missing Values Check
print("====================================================================================================================")
print("Customers - Missing values per column:")
print(customers_df_cleaned.isnull().sum())
print(f"Total missing values: {customers_df_cleaned.isnull().sum().sum()}")
print("====================================================================================================================")
print("Products - Missing values per column:")
print(products_df_cleaned.isnull().sum())
print(f"Total missing values: {products_df_cleaned.isnull().sum().sum()}")
print("====================================================================================================================")
print("Transactions - Missing values per column:")
print(transactions_df_cleaned.isnull().sum())
print(f"Total missing values: {transactions_df_cleaned.isnull().sum().sum()}")
print("====================================================================================================================")
# Duplicates Check
print("====================================================================================================================")
print(f"Customers duplicates remaining: {customers_df_cleaned.duplicated().sum()}")
print("====================================================================================================================")
print(f"Products duplicates remaining: {products_df_cleaned.duplicated().sum()}")
print("====================================================================================================================")
print(f"Transactions duplicates remaining: {transactions_df_cleaned.duplicated().sum()}")
print("====================================================================================================================")
# Data Types Verification
print("====================================================================================================================")
print("Customers data types:")
print(customers_df_cleaned.dtypes)
print("Products data types:")
print(products_df_cleaned.dtypes)
print("Transactions data types:")
print(transactions_df_cleaned.dtypes)
print("====================================================================================================================")
# Values Ranges Verification
print("Customers:")
print(f"Age range: {customers_df_cleaned['age'].min()} - {customers_df_cleaned['age'].max()}")
print(f"Countries: {customers_df_cleaned['country'].nunique()} unique countries")
print(f"Registration date range: {customers_df_cleaned['registration_date'].min()} to {customers_df_cleaned['registration_date'].max()}")
print("====================================================================================================================")
print("Products:")
print(f"  Price range: ${products_df_cleaned['price'].min():.2f} - ${products_df_cleaned['price'].max():.2f}")
print(f"  Stock range: {products_df_cleaned['stock'].min()} - {products_df_cleaned['stock'].max()}")
print(f"  Categories: {products_df_cleaned['category'].unique()}")
print("====================================================================================================================")
print("Transactions:")
print(f"  Quantity range: {transactions_df_cleaned['quantity'].min()} - {transactions_df_cleaned['quantity'].max()}")
print(f"  Transaction date range: {transactions_df_cleaned['transaction_date'].min()} to {transactions_df_cleaned['transaction_date'].max()}")
print(f"  Payment methods: {transactions_df_cleaned['payment_method'].unique()}")
print("====================================================================================================================")
# Check if all customer_ids in transactions exist in customers
invalid_customers = transactions_df_cleaned[~transactions_df_cleaned['customer_id'].isin(customers_df_cleaned['customer_id'])]['customer_id'].nunique()
print(f"Invalid customer_id references in transactions: {invalid_customers}")
# There are some invalid customer_ids because we removed some customers from customers_df because of email null value
# We should keep this invalid references, it will be more interesting for the sake of Task 3
print("====================================================================================================================")
# Check if all product_ids in transactions exist in products
invalid_products = transactions_df_cleaned[~transactions_df_cleaned['product_id'].isin(products_df_cleaned['product_id'])]['product_id'].nunique()
print(f"Invalid product_id references in transactions: {invalid_products}")


# Export Clean Data

os.makedirs('data/cleaned', exist_ok=True)

customers_df_cleaned.to_csv('data/cleaned/customers_clean.csv', index=False)
products_df_cleaned.to_csv('data/cleaned/products_clean.csv', index=False)
transactions_df_cleaned.to_csv('data/cleaned/transactions_clean.csv', index=False)
# Task 2: End
print("====================== TASK 2 END ======================")

# We need to drop duplicates again, because some invalid and 

# Task 3: Start
print("====================== TASK 3 START ======================")

# Part A

# Create Complete Transaction View
transactions_customers_merged = pd.merge(transactions_df_cleaned, customers_df_cleaned, on='customer_id', how='left')
df = pd.merge(transactions_customers_merged, products_df_cleaned, on='product_id', how='left')
# Chose left joins because we need to have all transactions (At least that is what I understood from task)

# Handle Merge Issues
print("Transactions that are unmatched with product: ")
product_unmatched = df[df['product_name'].isna()]
print(product_unmatched)
print(f"Total: {len(product_unmatched)}")
print("====================================================================================================================")
print("Transactions that are unmatched with customer: ")
customer_unmatched = df[df['email'].isna()]
print(customer_unmatched)
print(f"Total: {len(customer_unmatched)}")
print("====================================================================================================================")
print("No data loss because of Left join")
print(f"Original Transaction row number: {len(transactions_df_cleaned)}")
print(f"After Merge Transaction row number: {len(df)}")
print("====================================================================================================================")


