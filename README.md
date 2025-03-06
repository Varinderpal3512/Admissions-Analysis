# Admission Analysis

## Project Overview
This project analyzes admission trends, exploring factors such as GPA, SAT scores, scholarships, and gender distribution. The analysis includes data cleaning, visualization, and insights using Python.

## Repository Structure
```
Admission-Analysis/
│── data/
│   ├── raw/                        # Raw dataset before cleaning
│   │   ├── admission_data.csv
│   ├── processed/                   # Cleaned dataset
│   │   ├── admission_data_cleaned.csv
│
│── notebooks/                        # Jupyter notebooks for analysis
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_cleaned_data_exploration.ipynb
│
│── scripts/                          # Python scripts for automation
│   ├── data_cleaning.py
│   ├── analysis.py
│
│── reports/                          # Reports and visualizations
│   ├── figures/                      # Figures generated from analysis
│   │   ├── 1_acceptance_rate_by_gpa.png
│   │   ├── 2_sat_vs_gpa.png
│   │   ├── 3_scholarship_vs_acceptance.png
│   │   ├── 4_enrollment_trends_by_age.png
│   │   ├── 5_popular_programs.png
│   │   ├── 6_gender_distribution_across_programs.png
│
│── README.md                         # Project overview and instructions
│── requirements.txt                   # Dependencies
│── .gitignore                         # Ignore unnecessary files
```

## Installation
To run this project, install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage
### Data Cleaning
Run the data cleaning script:
```sh
python scripts/data_cleaning.py
```

### Data Analysis & Visualization
Run the analysis script:
```sh
python scripts/analysis.py
```
Alternatively, explore the Jupyter notebooks:
```sh
jupyter notebook notebooks/
```

## Dependencies
- pandas
- numpy
- matplotlib
- seaborn

## Results
Visualizations and insights are available in the `reports/figures/` folder.

## License
This project is open-source and available under the MIT License.
