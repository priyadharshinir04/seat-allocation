import pandas as pd

# Read the Excel file
print("📖 Reading Excel file...")
df = pd.read_excel(r'c:\Users\Priyadharshini\Downloads\students_320_updated_depts.xlsx')

# Save as CSV (replacing sample_students.csv)
df.to_csv('sample_students.csv', index=False)

print("✓ Successfully converted and saved dataset")
print(f"✓ Total records: {len(df)}")
print(f"✓ File saved to: sample_students.csv")
print(f"\nDataset Summary:")
print(f"  Departments: {', '.join(df['Department'].unique())}")
print(f"  Register Numbers: {df['Register Number'].min()} - {df['Register Number'].max()}")
print(f"\nDepartment Distribution:")
print(df['Department'].value_counts().to_string())
print(f"\n✓ Dataset is ready to use!")
