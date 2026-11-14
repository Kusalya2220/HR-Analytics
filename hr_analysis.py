from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path("data/hr_employee_data.csv")
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE)
print("HR DATA OVERVIEW")
print(df.head())
print("\nEmployees:", len(df))
print("\nAttrition count:")
print(df["Attrition"].value_counts())

attrition_rate = (df["Attrition"].eq("Yes").mean()) * 100
print(f"\nOverall attrition rate: {attrition_rate:.2f}%")

dept_rate = (df.groupby("Department")["Attrition"]
             .apply(lambda s: s.eq("Yes").mean() * 100)
             .sort_values(ascending=False))
print("\nAttrition rate by department (%):")
print(dept_rate.round(2))

dept_rate.plot(kind="bar", title="Attrition Rate by Department",
               xlabel="Department", ylabel="Attrition Rate (%)")
plt.tight_layout()
plt.savefig(OUT / "attrition_by_department.png")
plt.close()

df.groupby("JobRole")["MonthlyIncome"].mean().sort_values().plot(
    kind="bar", title="Average Monthly Income by Job Role",
    xlabel="Job Role", ylabel="Average Monthly Income")
plt.tight_layout()
plt.savefig(OUT / "average_income_by_role.png")
plt.close()

print("\nCharts saved in outputs/.")
