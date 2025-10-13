# Import necessary libraries
import pandas as pd  # For data manipulation and analysis
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For enhanced data visualization

# Set a clean visual style for plots
sns.set(style="whitegrid")

# Load the dataset from a CSV file
df = pd.read_csv("student_habits_performance.csv")

# Display the first five rows of the dataset to get a quick overview
print(df.head())

# Check for missing values in each column
print("Missing values:\n", df.isna().sum())

# Check how many duplicate rows exist in the dataset
print("Duplicated rows:", df.duplicated().sum())

# Generate descriptive statistics for numerical columns
print("\nNumerical Description:\n", df.describe())

# Show the names of the columns that are of type 'object' (i.e., categorical)
print("\nCategorical Columns:\n", df.describe(include="object").columns)

# Define a list of categorical columns manually
# These are usually non-numeric and represent categories or labels
categorical_cols = [
    'student_id',  # Likely a unique identifier
    'gender',  # Male/Female/Other
    'part_time_job',  # Yes/No
    'diet_quality',  # Good/Average/Poor
    'parental_education_level',  # High School/College/etc.
    'internet_quality',  # Good/Poor/None
    'extracurricular_participation'  # Yes/No
]

# Loop through each categorical column and display the frequency of each category
for col in categorical_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())
