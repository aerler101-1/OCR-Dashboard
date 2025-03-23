# OCR-Dashboard

This project is an interactive dashboard designed to analyze demographic data. The dashboard helps visualize differences in demographics between applicants and employees across various job families, enabling organizations to identify disparities and inform equitable decision-making. A online version is available at https://ocr-dashboard.streamlit.app/

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)

## Features

- 📊 **Interactive Visualizations**: Built with Plotly and Dash for dynamic, browser-based charts and graphs.  
- 📁 **Data Exploration**: Easily switch between applicant and employee data views.  
- 📈 **Statistical Insights**: Highlights significant demographic differences across job families, supporting diversity and equity initiatives.  

## Installation

To run the project locally:

1. **Clone the repository**

```bash
git clone https://github.com/aerler101-1/OCR-Dashboard.git
cd OCR-Dashboard
```

2. **(Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Usage

After setup, launch the dashboard with:

```bash
python interactive_dashboard.py
```

Open your browser and go to `http://127.0.0.1:8050/` to interact with the dashboard.

## Project Structure

- `interactive_dashboard.py` – Main script that runs the Dash app  
- `OCR_Data_Analyst.ipynb` – Jupyter notebook for preprocessing and analysis  
- `Redacted_Applicant_Data.csv` – Applicant demographic dataset  
- `Redacted_Employee_Data.csv` – Employee demographic dataset  
- `Significant Differences in Demographics by Job Family.csv` – Output file with calculated statistical differences  
- `requirements.txt` – Python dependencies

## Contributing

Contributions are welcome! If you’d like to suggest improvements or add features, please fork the repo, make your changes, and submit a pull request. Make sure your work aligns with the project's goals and maintains code quality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Project Challenges

- **Data Integration**: One of the core challenges was connecting the applicant and employee datasets. Since there was no shared identifier beyond a redacted ID, the analysis had to be carefully scoped to only include individuals present in both datasets.
- **Filtered Analysis**: To ensure data integrity and meaningful comparisons, the dashboard restricts visualizations and statistical testing to only those IDs that overlapped between the two sources. This required meticulous data cleaning, filtering, and validation to maintain consistency and relevance across job family demographics.
