import pandas as pd

# Load marketing data
df = pd.read_csv("marketing_data.csv")

print("Marketing Funnel & Conversion Performance Analysis")
print("--------------------------------------------------")

print(df)

# Calculate conversion rates
lead_to_qualified = (df["Qualified Leads"].sum() / df["Leads"].sum()) * 100
qualified_to_customer = (df["Customers"].sum() / df["Qualified Leads"].sum()) * 100

print("\nLead to Qualified Lead Conversion Rate: {:.2f}%".format(lead_to_qualified))
print("Qualified Lead to Customer Conversion Rate: {:.2f}%".format(qualified_to_customer))
