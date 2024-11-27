import pandas as pd

# Load the CSV file
file_path = '/home/ryusuke/Downloads/AnkiDojo__.csv'  # Replace with your file path
anki_data = pd.read_csv(file_path)

# Function to bold only the current row's Expression in its Sentence
def bold_current_expression(row):
    if pd.notnull(row['Sentence']) and pd.notnull(row['Expression']):
        # Bold only the current row's Expression
        return row['Sentence'].replace(row['Expression'], f"<b>{row['Expression']}</b>")
    return row['Sentence']

# Apply the bolding function row by row
anki_data['Sentence'] = anki_data.apply(bold_current_expression, axis=1)

# Save the updated data to a new CSV file
output_path = '/home/ryusuke/Documents/ankiconverted3.csv'  # Replace with your desired output path
anki_data.to_csv(output_path, index=False)

print(f"Processed file saved as: {output_path}")
