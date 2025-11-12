# Project 2: Pandas Data Manipulation

**Course:** Introduction to Data Science with Python  
**Program:** Computer Science  
**Institution:** Kutaisi International University

## Student Information

**Name:** Nikoloz Rusishvili  
**Submission Date:** November 12, 2025  

**Honor Code:** I certify this work is my own.

---

## Project Overview

This project demonstrates proficiency in data manipulation and analysis using Pandas. The project involves working with possible real-time e-commerce data across three datasets (customers, products, and transactions), performing data cleaning, transformation, and comprehensive analysis.

---

## Repository Structure

```
KIU-DS-Project2-Nikoloz-Rusishvili/
├── Project2_Nikoloz_Rusishvili.py
├── data/
│   ├── original/                    
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   └── transactions.csv
│   └── cleaned/             
│       ├── customers_clean.csv
│       ├── products_clean.csv
│       └── transactions_clean.csv
├── README.md                          
└── requirements.txt
```

---

## Installation & Setup

### Prerequisites

- Python 3.14 or higher
- pip (Python package manager)

### Installing Dependencies

1. Clone this repository:
```bash
git clone https://github.com/NikolozR/KIU-DS-Project2-Nikoloz-Rusishvili.git
cd KIU-DS-Project2-Nikoloz-Rusishvili
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

---

## Running the Code

### Execute the complete project:

**If using the included virtual environment:**
```bash
./venv/bin/python Project2_Nikoloz_Rusishvili.py
```

**Or if you installed dependencies globally:**
```bash
python3 Project2_Nikoloz_Rusishvili.py
```

The script will:
1. Load the original CSV files from `data/original/`
2. Perform exploratory data analysis
3. Clean the data systematically
4. Export cleaned data to `data/cleaned/`
5. Perform advanced analysis and feature engineering
6. Display comprehensive results

### Expected Output

The script prints:
- Data loading validation
- Exploratory statistics for all datasets
- Data quality issues identified
- Cleaning operations performed
- Validation reports
- Advanced analysis results including:
  - Revenue analysis by category, country, payment method
  - Customer behavior patterns
  - Product performance metrics
  - Summary tables and cross-tabulations

---

## Data Cleaning Decisions

### Customers Dataset

- **Missing Emails:** Dropped rows - As explained in comments, email is key identifier and we can not have rows without that column.
- **Duplicates:** Removed duplicate rows (4 rows), kept first occurrence
- **Age Data Type:** Extracted numeric values from "XX years" format
- **Country Names:** Standardized "US"/"USA" to "United States"
- **Email Format:** Converted all emails to lowercase for consistency (but I think all emails were already lowercase)

### Products Dataset

- **Missing Prices:** Filled with median price of the same category
- **Negative Prices:** Converted to absolute values - assumed data entry errors
- **Stock Levels:** Capped unrealistic values at 500 (as suggested by task description)
- **Product Names:** Stripped leading/trailing whitespace
- **Category Names:** Capitalized for consistency

### Transactions Dataset

- **Missing Quantities:** Filled with mode value - most common quantity
- **Duplicates:** Removed duplicate transactions
- **Invalid Customer IDs:** Removed transactions with non-existent customers
- **Future Dates:** Removed transaction with future date
- **Payment Method:** Standardized to Title Case

### Rationale

- **Drop vs. Fill:** Dropped critical identifiers (email), filled numeric values with statistical measures
- **Median over Mean:** Used median for prices to avoid skew from outliers
- **Mode for Discrete:** Used mode for quantity as it's a discrete, countable value
- **Inner Join:** Used for merging to ensure complete records with valid references

