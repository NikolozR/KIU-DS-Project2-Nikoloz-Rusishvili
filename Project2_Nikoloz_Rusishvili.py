import pandas as pd

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
    print("====================================================================================================================")



data_quality_check(customers_df, "Customers")
data_quality_check(products_df, "Products")
data_quality_check(transactions_df, "Transactions")