import pandas as pd

# Task 1: Start

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

# Task 2: Start

# Part A: Identify Data Quality Issues

# Customers.csv
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

# Products.csv
print(products_df[products_df['price'].isnull()]['product_id'].tolist())
print(products_df.query("price < 0")['product_id'].tolist())
print(products_df[products_df['product_name'].str.startswith(' ')]['product_id'].to_list())
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