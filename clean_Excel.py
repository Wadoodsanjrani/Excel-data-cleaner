import pandas as pd

def clean_excel(input_file, output_file):
    df = pd.read_excel(input_file)
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    df = df.loc[:, df.notna().any(axis=0)]
    df.to_excel(output_file, index=False)
    print(f"Cleaned file saved as {output_file}")

clean_excel("messy_data.xlsx", "clean_data.xlsx")
