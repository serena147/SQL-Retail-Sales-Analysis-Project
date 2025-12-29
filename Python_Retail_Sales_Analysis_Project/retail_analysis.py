import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv("retail_sales_dataset.csv")

# 2. Process Time Data (Do this BEFORE plotting)
df['Date'] = pd.to_datetime(df['Date'])
# Sorting by month can be tricky, but let's see what this prints first:
monthly_sales = df.groupby(df['Date'].dt.strftime('%m - %B'))['Total Amount'].sum()

# 3. Print the text results (This will show up in the terminal immediately)
print("\n--- 💰 Total Revenue by Category ---")
category_sales = df.groupby('Product Category')['Total Amount'].sum()
print(category_sales)

print("\n--- 📅 Monthly Sales Performance ---")
print(monthly_sales)

# 4. Create and Show the Chart
category_sales.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Total Revenue by Product Category')
plt.xlabel('Category')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('sales_chart.png')
print("\n--- 📊 CHART SAVED! Opening window now... ---")

# Create a second chart for Monthly Trends
plt.figure(figsize=(10, 5)) # Make it wider
monthly_sales.plot(kind='line', marker='o', color='purple', linestyle='--')

plt.title('Monthly Sales Trend')
plt.ylabel('Revenue ($)')
plt.xlabel('Month')
plt.grid(True, linestyle=':', alpha=0.6) # Add a faint grid
plt.tight_layout()

# Save this one too!
plt.savefig('monthly_trend.png')

# Calculate Average Spend
average_spend = df['Total Amount'].mean()

print("\n--- 💡 KEY RETAIL METRIC ---")
print(f"Average Customer Spend per Transaction: ${average_spend:.2f}")

# --- GENDER ANALYSIS ---
gender_counts = df['Gender'].value_counts()
gender_revenue = df.groupby('Gender')['Total Amount'].sum()

print("\n--- 👥 Gender Demographics ---")
print(gender_revenue)

# Create a Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(gender_revenue, labels=gender_revenue.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'], startangle=140)
plt.title('Revenue Contribution by Gender')

# Save the new chart
plt.savefig('gender_distribution.png')

# --- AGE GROUP ANALYSIS ---
# 1. Define the buckets (bins) and the names for them
bins = [0, 18, 30, 45, 60, 100]
labels = ['Under 18', '18-30', '31-45', '46-60', '60+']

# 2. Create the 'Age Group' column
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 3. Calculate Revenue by Age Group
age_revenue = df.groupby('Age Group', observed=True)['Total Amount'].sum()

print("\n--- 🎂 Revenue by Age Group ---")
print(age_revenue)

# 4. Create a Bar Chart for Age
plt.figure(figsize=(10, 6))
age_revenue.plot(kind='bar', color='orange')
plt.title('Total Revenue by Age Group')
plt.ylabel('Revenue ($)')
plt.xlabel('Age Group')
plt.xticks(rotation=0)
plt.tight_layout()

# Save it
plt.savefig('age_distribution.png')

plt.show() # <--- Everything AFTER this line waits until you close the window!