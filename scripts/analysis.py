import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")

# Load the dataset
file_path = "../data/processed/admission_data_cleaned.csv"  # Using cleaned data
df = pd.read_csv(file_path)

# Function to save plots
def save_plot(fig, filename):
    fig.savefig(f"../reports/figures/{filename}", bbox_inches='tight')
    print(f"📊 {filename} saved!")

# Acceptance Rate by GPA (Line Chart)
df["GPA_Binned"] = pd.cut(df["GPA"], bins=5)
acceptance_rates = df.groupby("GPA_Binned", observed=False)["Acceptance_Status"].apply(lambda x: (x == "Accepted").mean())

plt.figure(figsize=(8, 5))
acceptance_rates.plot(kind='line', marker='o', color='b')
plt.title("Acceptance Rate by GPA")
plt.xlabel("GPA Range")
plt.ylabel("Acceptance Rate")
save_plot(plt, "1_acceptance_rate_by_gpa.png")

# SAT Score vs. GPA (Regression Plot)
plt.figure(figsize=(8, 5))
sns.regplot(x=df["SAT_Score"], y=df["GPA"], scatter_kws={"alpha": 0.5}, line_kws={"color": "red"})
plt.title("SAT Score vs. GPA")
plt.xlabel("SAT Score")
plt.ylabel("GPA")
save_plot(plt, "2_sat_vs_gpa.png")

# Scholarship vs. Acceptance Rate (Stacked Bar Chart)
scholarship_acceptance = df.groupby("Scholarship_Status")["Acceptance_Status"].value_counts(normalize=True).unstack()

plt.figure(figsize=(8, 5))
scholarship_acceptance.plot(kind="bar", stacked=True, colormap="coolwarm")
plt.title("Scholarship vs. Acceptance Rate")
plt.xlabel("Scholarship Status")
plt.ylabel("Proportion")
plt.legend(title="Acceptance Status")
save_plot(plt, "3_scholarship_vs_acceptance.png")

# Enrollment Trends by Age Group (Histogram)
age_bins = [17, 19, 21, 23, 25, 30]
plt.figure(figsize=(8, 5))
sns.histplot(df, x="Age", bins=age_bins, hue="Enrollment_Status", multiple="stack", palette="muted")
plt.title("Enrollment Trends by Age Group")
plt.xlabel("Age")
plt.ylabel("Count")
save_plot(plt, "4_enrollment_trends_by_age.png")

# Most Popular Programs Applied (Pie Chart)
plt.figure(figsize=(8, 5))
df["Program_Applied"].value_counts().plot(kind="pie", autopct="%1.1f%%", cmap="viridis", startangle=90)
plt.title("Most Popular Programs Applied")
plt.ylabel("")
save_plot(plt, "5_popular_programs.png")

# Male & Female Distribution Across Programs (Bar Chart)
plt.figure(figsize=(8, 5))
sns.countplot(data=df, y="Program_Applied", hue="Gender", palette=["#3498db", "#f987c5", "#95a5a6"])
plt.title("Gender Distribution Across Programs")
plt.xlabel("Count")
plt.ylabel("Program Applied")
plt.legend(title="Gender")
save_plot(plt, "6_gender_distribution_across_programs.png")

print("\n✅ Analysis completed. Charts saved in 'reports/figures/'.")
