import pandas as pd
import plotly.express as px
import streamlit as st

# Load the cleaned CSV files
employee_full_csv_path = "Redacted_Employee_Data.csv"
employee_subset_csv_path = "Redacted_Employee_Data_Subset.csv"
applicant_csv_path = "Redacted_Applicant_Data.csv"

# Load datasets
employee_full_df = pd.read_csv(employee_full_csv_path)
employee_subset_df = pd.read_csv(employee_subset_csv_path)
applicant_df = pd.read_csv(applicant_csv_path)

# User selection for dataset
st.sidebar.title("Dataset Selection")
selected_dataset = st.sidebar.radio("Choose Employee Data:", ["Full Dataset", "Subset Dataset"])

# Assign the selected dataset
if selected_dataset == "Full Dataset":
    employee_df = employee_full_df
else:
    employee_df = employee_subset_df

# Define demographic columns
demographic_columns = ["Sex", "Disabled", "Disab Vet", "Race/Ethnicity", "Mil Status"]

# Fix the column name for "Job Family" (correct spelling)
job_families = sorted(employee_df["Job Family"].dropna().unique())  # Sort alphabetically
job_families = ["Overall"] + job_families  # Add "Overall" as the first option

# Streamlit app layout
st.title("Interactive Demographic Comparison Dashboard")

# Dropdowns for job family and demographic column selection
selected_job_family = st.selectbox("Select Job Family", job_families)
selected_demographic = st.selectbox("Select Demographic", demographic_columns)

# Filter data based on selection
if selected_job_family == "Overall":
    # Use the entire dataset for overall comparisons
    employee_subset = employee_df
    applicant_subset = applicant_df
else:
    # Filter based on the selected job family
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

# Create an interactive bar chart with Plotly
fig = px.bar(
    data,
    x="Category",
    y="Percentage",
    color="Group",
    barmode="group",
    title=f"{selected_demographic} Distribution for {selected_job_family} ({selected_dataset})",
    labels={"Percentage": "Percentage (%)", "Category": selected_demographic},
    hover_data={"Percentage": ":.2f"}  # Display percentage with two decimal points
)

# Show the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
