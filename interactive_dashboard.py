import pandas as pd
import plotly.express as px
import streamlit as st

# Load the cleaned CSV files
employee_csv_path = "Redacted_Employee_Data.csv"
applicant_csv_path = "Redacted_Applicant_Data.csv"

employee_df = pd.read_csv(employee_csv_path)
applicant_df = pd.read_csv(applicant_csv_path)

# Define demographic columns and job families
demographic_columns = ["Sex", "Disabled", "Disab Vet", "Race/Ethnicity", "Mil Status"]

# Fix the column name for "Job Family" (correct spelling)
job_families = employee_df["Job Family"].dropna().unique()

# Streamlit app layout
st.title("Interactive Demographic Comparison Dashboard")

# Dropdowns for job family and demographic column selection
selected_job_family = st.selectbox("Select Job Family", job_families)
selected_demographic = st.selectbox("Select Demographic", demographic_columns)

# Filter employee and applicant data for the selected job family
employee_subset = employee_df[employee_df["Job Family"] == selected_job_family]
applicant_subset = applicant_df[applicant_df["Job Family"] == selected_job_family]

# Calculate percentage distributions
employee_counts = employee_subset[selected_demographic].value_counts(normalize=True) * 100
applicant_counts = applicant_subset[selected_demographic].value_counts(normalize=True) * 100

# Combine both datasets to align categories
all_categories = set(employee_counts.index).union(set(applicant_counts.index))

# Ensure all categories are represented
employee_counts = employee_counts.reindex(all_categories, fill_value=0)
applicant_counts = applicant_counts.reindex(all_categories, fill_value=0)

# Combine data for Plotly
data = pd.DataFrame({
    "Category": list(all_categories) * 2,
    "Percentage": list(employee_counts) + list(applicant_counts),
    "Group": ["Employee"] * len(all_categories) + ["Applicant"] * len(all_categories)
})

fig = px.bar(
    data,
    x="Category",
    y="Percentage",
    color="Group",
    barmode="group",
    title=f"{selected_demographic} Distribution for {selected_job_family}",
    labels={"Percentage": "Percentage (%)", "Category": selected_demographic},
    hover_data={"Percentage": ":.2f"}  # Display percentage with two decimal points
)


st.plotly_chart(fig, use_container_width=True)
