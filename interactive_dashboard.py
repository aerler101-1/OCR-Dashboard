import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset
file_path = "OCR Interview Employee and Applicant Dataset.xlsx"
xls = pd.ExcelFile(file_path)

employee_df = pd.read_excel(xls, sheet_name="Employee Data")
applicant_df = pd.read_excel(xls, sheet_name="Applicant Data")

# Identifying the correct demographic columns
demographic_columns = ["Sex", "Disabled", "Disab Vet", "Race/Ethnicity", "Mil Status"]

# Get unique job families
job_families = employee_df["Job Fmaily"].dropna().unique()

# Streamlit UI
st.title("Demographic Breakdown: Employee vs. Applicant Comparison")

# Dropdowns for job family and demographic selection
selected_job_family = st.selectbox("Select Job Family", job_families)
selected_demographic = st.selectbox("Select Demographic", demographic_columns)

# Filter employee data for the selected job family
employee_subset = employee_df[employee_df["Job Fmaily"] == selected_job_family]

# Compute percentage distributions
employee_counts = employee_subset[selected_demographic].value_counts(normalize=True) * 100
applicant_counts = applicant_df[selected_demographic].value_counts(normalize=True) * 100

# Combine for plotting
demographic_data = pd.DataFrame({
    "Employee %": employee_counts,
    "Applicant %": applicant_counts
}).fillna(0)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))
demographic_data.plot(kind="bar", ax=ax)
plt.title(f"Comparison of {selected_demographic} Distribution - {selected_job_family}")
plt.ylabel("Percentage")
plt.xlabel(selected_demographic)
plt.xticks(rotation=45)
plt.legend(["Employee %", "Applicant %"])
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the chart in Streamlit
st.pyplot(fig)
