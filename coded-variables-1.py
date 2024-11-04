
import pandas as pd

# Sample data simulating survey responses
data = {
    'ID': [1, 2, 3, 4, 5],
    'coded_variable_A': [1, 2, 1, 3, 2],
    'coded_variable_B': [0, 1, 0, 1, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

print("Initial DataFrame:")
print(df)

# Mapping dictionaries for coded variables
code_map_A = {1: 'Yes', 2: 'No', 3: 'Maybe'}
code_map_B = {1: 'Yes', 0: 'No'}

# Decode coded_variable_A
df['coded_variable_A'] = df['coded_variable_A'].map(code_map_A)

# Decode coded_variable_B
df['coded_variable_B'] = df['coded_variable_B'].map(code_map_B)

print("\nDataFrame with Decoded Values:")
print(df)

