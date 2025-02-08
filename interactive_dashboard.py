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
job_families = employee_df["Job Fmaily"].dropna().unique()

# Streamlit app layout
st.title("Interactive Demographic Comparison Dashboard")

# Dropdowns for job family and demographic column selection
selected_job_family = st.selectbox("Select Job Family", job_families)
selected_demographic = st.selectbox("Select Demographic", demographic_columns)

# Filter employee data for the selected job family
employee_subset = employee_df[employee_df["Job Fmaily"] == selected_job_family]

# Calculate percentage distributions
employee_counts = employee_subset[selected_demographic].value_counts(normalize=True) * 100
applicant_counts = applicant_df[selected_demographic].value_counts(normalize=True) * 100

# Combine data for Plotly
data = pd.DataFrame({
    "Category": employee_counts.index.tolist() + applicant_counts.index.tolist(),
    "Percentage": employee_counts.tolist() + applicant_counts.tolist(),
    "Group": ["Employee"] * len(employee_counts) + ["Applicant"] * len(applicant_counts)
})

# Create an interactive bar chart with Plotly
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

# Show the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
