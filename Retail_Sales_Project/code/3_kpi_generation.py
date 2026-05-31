
import pandas as pd


retail = pd.read_csv(
    "../output/cleaned_retail_data.csv"
)

print("Dataset Loaded Successfully")
print("Rows:", len(retail))



total_revenue = retail["net_revenue"].sum()

total_transactions = retail["transaction_id"].nunique()

total_customers = retail["customer_id"].nunique()

average_order_value = (
    total_revenue / total_transactions
)

print("\n===== KPI SUMMARY =====")

print("Total Revenue:", round(total_revenue, 2))

print("Total Transactions:", total_transactions)

print("Total Customers:", total_customers)

print(
    "Average Order Value:",
    round(average_order_value, 2)
)


#revenue by category

revenue_by_category = (
    retail.groupby("category")
    ["net_revenue"]
    .sum()
    .reset_index()
)

print("\nRevenue By Category")

print(revenue_by_category)

#revenue by city

revenue_by_city = (
    retail.groupby("city")
    ["net_revenue"]
    .sum()
    .reset_index()
)

print("\nRevenue By City")

print(revenue_by_city)


#top product

top_product = (
    retail.groupby("product_name")
    ["net_revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(1)
)

print("\nTop Product")

print(top_product)
revenue_by_category.to_csv(
    "../output/revenue_by_category.csv",
    index=False
)

revenue_by_city.to_csv(
    "../output/revenue_by_city.csv",
    index=False
)
payment_revenue = (
    retail.groupby("payment_method")
    ["net_revenue"]
    .sum()
    .reset_index()
)

print("\nRevenue By Payment Method")

print(payment_revenue)

payment_revenue.to_csv(
    "../output/revenue_by_payment_method.csv",
    index=False
)

#monthly revenue trend
monthly_revenue = (
    retail.groupby(["year", "month"])
    ["net_revenue"]
    .sum()
    .reset_index()
)

print("\nMonthly Revenue")

print(monthly_revenue.head())

monthly_revenue.to_csv(
    "../output/monthly_revenue.csv",
    index=False
)

print("\nKPI Files Exported Successfully")