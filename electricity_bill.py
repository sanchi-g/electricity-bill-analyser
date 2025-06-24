import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sample_data.csv")

total_units = df["Units"].sum()
peak_usage = df["Units"].max()
peak_day = df[df["Units"] == peak_usage]["Date"].values[0]
monthly_cost = df["Cost"].sum()

print("Total Units Used:", total_units)
print("Peak Usage:", peak_usage,"units on", peak_day)
print("Monthly Cost: ₹",monthly_cost)

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Units"], marker='o')
plt.title("Daily Electricity Usage")
plt.xlabel("Date")
plt.ylabel("Units")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("usage_plot.png")
plt.show()
