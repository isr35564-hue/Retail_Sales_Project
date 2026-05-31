import pandas as pd

file_path = r"../data/USECASE - Data Engineering.xlsx"

product = pd.read_excel(file_path, sheet_name="product_details")
retail1 = pd.read_excel(file_path, sheet_name="retail_data1")
retail2 = pd.read_excel(file_path, sheet_name="retail_data2")


retail = pd.concat([retail1, retail2], ignore_index=True)

print("\nTOTAL ROWS")
print(len(retail))

print("\nMISSING VALUES")
print(retail.isnull().sum())

print("\nDUPLICATES")
print(retail.duplicated().sum())

print("\nINVALID QUANTITIES")
print((retail["quantity"] <= 0).sum())