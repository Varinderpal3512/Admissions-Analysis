import pandas as pd
import numpy as np

# File paths
INPUT_FILE = "../data/raw/admission_data.csv"
OUTPUT_FILE = "../data/processed/admission_data_cleaned.csv"

def load_data(file_path):
    return pd.read_csv(file_path)

def handle_missing_values(df):
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['GPA'].fillna(df['GPA'].mean(), inplace=True)
    df['SAT_Score'].fillna(df['SAT_Score'].median(), inplace=True)
    df['Scholarship_Status'].fillna(df['Scholarship_Status'].mode()[0], inplace=True)
    return df

def fix_inconsistent_data(df):
    df['Gender'] = df['Gender'].replace({'Fmale': 'Female', 'Mal': 'Male', 'Femal': 'Female', 'Mle': 'Male'})
    df['Program_Applied'] = df['Program_Applied'].replace({
        'Comp Sci': 'Computer Science',
        'Cmptr Sci': 'Computer Science',
        'CompSci': 'Computer Science',
        'Engg': 'Engineering',
        'Bussiness': 'Business',
        'Hlthcare': 'Healthcare',
        'Healthcar': 'Healthcare'
    })
    return df

def remove_duplicates(df):
    print(f"🔍 Duplicate Rows Before: {df.duplicated().sum()}")
    df = df.drop_duplicates()
    print(f"✅ Duplicate Rows After: {df.duplicated().sum()}")
    return df

def normalize_numeric_values(df):
    df.loc[:, 'GPA_Normalized'] = (df['GPA'] - df['GPA'].min()) / (df['GPA'].max() - df['GPA'].min())
    df.loc[:, 'SAT_Score_Normalized'] = (df['SAT_Score'] - df['SAT_Score'].min()) / (df['SAT_Score'].max() - df['SAT_Score'].min())
    return df

def save_cleaned_data(df, file_path):
    df.to_csv(file_path, index=False)
    print(f"✅ Cleaned dataset saved to: {file_path}")

def main():
    print("📥 Loading data...")
    df = load_data(INPUT_FILE)
    
    print("🔍 Handling missing values...")
    df = handle_missing_values(df)
    
    print("📝 Fixing inconsistent data...")
    df = fix_inconsistent_data(df)
    
    print("🗑️ Removing duplicates...")
    df = remove_duplicates(df)
    
    print("📊 Normalizing numeric values...")
    df = normalize_numeric_values(df)
    
    print("💾 Saving cleaned dataset...")
    save_cleaned_data(df, OUTPUT_FILE)

    print("🎉 Data cleaning completed successfully!")

if __name__ == "__main__":
    main()
