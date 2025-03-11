import pandas as pd

# 1. Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# 2. Reading a CSV file
df_csv = pd.read_csv('example.csv')  # Make sure 'example.csv' exists
print("\nFirst 5 rows of CSV:")
print(df_csv.head())

# 3. Writing a DataFrame to a CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to output.csv")

# 4. Displaying basic information about the DataFrame
print("\nDataFrame Info:")
df.info()

# 5. Selecting a column
print("\nSelecting the 'Name' column:")
print(df['Name'])

# 6. Selecting multiple columns
print("\nSelecting 'Name' and 'Age' columns:")
print(df[['Name', 'Age']])

# 7. Selecting rows using iloc (by index)
print("\nSelecting the first row using iloc:")
print(df.iloc[0])

# 8. Selecting rows using loc (by label)
print("\nSelecting rows where Age > 28:")
print(df[df['Age'] > 28])

# 9. Adding a new column
df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame after adding 'Salary' column:")
print(df)

# 10. Dropping a column
df = df.drop(columns=['City'])
print("\nDataFrame after dropping 'City' column:")
print(df)

# 11. Sorting values by Age
df_sorted = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age:")
print(df_sorted)

# 12. Grouping data by a column
print("\nAverage Salary by Age:")
print(df.groupby('Age')['Salary'].mean())