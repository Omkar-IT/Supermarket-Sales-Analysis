import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('SuperMarket Analysis.csv')

# Clean up any trailing spaces in column names
df.columns = df.columns.str.strip()

# Standardize the date formats
df['Date'] = pd.to_datetime(df['Date'])

# Remove any empty or corrupt data rows
df.dropna(inplace=True)

print("Data loaded and cleaned successfully!")

# Calculate total revenue by product category using the correct 'Sales' column
category_sales = df.groupby('Product line')['Sales'].sum()

# Create a bar chart
plt.figure(figsize=(10, 6))
category_sales.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart to your folder
plt.savefig('revenue_by_category.png')
print("Chart saved as revenue_by_category.png successfully!")