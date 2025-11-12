import pandas as pd

sales1 = pd.DataFrame({
    'city': ['Tbilisi', 'Tbilisi', 'Kutaisi', 'Batumi'],
    'year': [2023, 2024, 2023, 2023],
    'revenue': [100, 120, 90, 80]
})

sales2 = pd.DataFrame({
    'city': ['Tbilisi', 'Kutaisi', 'Batumi', 'Batumi'],
    'year': [2023, 2023, 2023, 2024],
    'profit': [20, 15, 10, 12]
})

merged = pd.merge(sales1, sales2, on=['city', 'year'], how='left')
print(merged)