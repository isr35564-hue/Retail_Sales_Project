import pandas as pd
file_path = r"../data/USECASE - Data Engineering.xlsx"

product = pd.read_excel(
    file_path,
    sheet_name="product_details"
)

retail1 = pd.read_excel(
    file_path,
    sheet_name="retail_data1"
)

retail2 = pd.read_excel(
    file_path,
    sheet_name="retail_data2"
)


retail = pd.concat(
    [retail1, retail2],
    ignore_index=True
)



print("Rows Before Cleaning:", len(retail))

# fixing the missing prices
retail = retail.merge(
    product[["product_id", "price"]],
    on="product_id",
    how="left",
    suffixes=("", "_master")
)

retail["price"] = retail["price"].fillna(
    retail["price_master"]
)

print("\nMissing Prices After Fix:")
print(retail["price"].isnull().sum())

#removing invalid quantities

before_rows = len(retail)

retail = retail[
    retail["quantity"] > 0
]

after_rows = len(retail)

rows_removed = before_rows - after_rows
print("\nRows Before Quantity Cleaning:", before_rows)
print("Rows After Quantity Cleaning:", after_rows)
print("Rows Removed:", rows_removed)

print("\nRemaining Invalid Quantities:")
print((retail["quantity"] <= 0).sum())



#date standardization
retail["transaction_date"] = pd.to_datetime(
    retail["transaction_date"],
    errors="coerce"
)

print("\nNull Dates After Conversion:")
print(retail["transaction_date"].isnull().sum())



retail["month"] = retail["transaction_date"].dt.month_name()

retail["year"] = retail["transaction_date"].dt.year

print("\nDate Conversion Successful")
print(retail[["transaction_date", "month", "year"]].head())


# product,category analysis
print("\nUnique Product Names:")
print(sorted(retail["product_name"].dropna().unique()))

print("\nUnique Categories:")
print(sorted(retail["category"].dropna().unique()))


retail["product_name"] = (
    retail["product_name"]
    .str.strip()
    .str.title()
)

print("\nProduct Names Standardized")
print(sorted(retail["product_name"].unique()))


category_map = {
    "ELEC": "Electronics",
    "electronics": "Electronics",

    "FURN": "Furniture",
    "furniture": "Furniture",

    "CLOTH": "Clothing",
    "clothing": "Clothing",

    "HOME": "Home Appliances",
    "home appliances": "Home Appliances"
}

retail["category"] = retail["category"].replace(category_map)

print("\nCategories Standardized")
print(sorted(retail["category"].unique()))


#masking

def mask_email(email):

    if pd.isna(email):
        return email

    email = str(email)

    if "@" not in email:
        return email

    username, domain = email.split("@")

    return username[:2] + "***@" + domain


def mask_phone(phone):

    if pd.isna(phone):
        return phone

    phone = str(phone)

    if len(phone) < 6:
        return phone

    return phone[:3] + "****" + phone[-3:]


retail["email"] = retail["email"].apply(mask_email)

retail["phone"] = retail["phone"].apply(mask_phone)

print("\nPII Masking Successful")

print(
    retail[
        ["customer_name", "email", "phone"]
    ].head()
)


#calculation

retail["gross_revenue"] = (
    retail["price"] *
    retail["quantity"]
)

retail["net_revenue"] = (
    retail["gross_revenue"] *
    (1 - retail["discount"])
)

print("\nRevenue Calculation Successful")

print(
    retail[
        [
            "product_name",
            "price",
            "quantity",
            "discount",
            "gross_revenue",
            "net_revenue"
        ]
    ].head()
)


retail.to_csv(
    "../output/cleaned_retail_data.csv",
    index=False
)

print("\nCleaned Dataset Exported Successfully")
print("Location: output/cleaned_retail_data.csv")