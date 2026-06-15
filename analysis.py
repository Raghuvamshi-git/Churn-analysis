import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Dataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nChurn Distribution:")
print(df["Churn"].value_counts())


# Churn Distribution Chart
df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")

plt.show()

contract_churn = pd.crosstab(df["Contract"], df["Churn"])

print("\nContract vs Churn")
print(contract_churn)

contract_churn.plot(kind="bar")

plt.title("Contract Type vs Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.show()

# Average Monthly Charges by Churn

avg_charges = df.groupby("Churn")["MonthlyCharges"].mean()

print("\nAverage Monthly Charges:")
print(avg_charges)

avg_charges.plot(kind="bar")

plt.title("Average Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")

plt.show()