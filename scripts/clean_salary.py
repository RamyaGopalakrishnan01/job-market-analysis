import pandas as pd

def clean_salary(df, column='salary_estimate'):
    # Remove $ and K, and text in parentheses
    salary_clean = df[column].str.replace(r'[\$,K]', '', regex=True)
    salary_clean = salary_clean.str.split(' ').str[0]  # take only the first part

    # Split into min and max salary
    df['min_salary'] = salary_clean.str.split('-').str[0].astype(float)
    df['max_salary'] = salary_clean.str.split('-').str[1]
    df['max_salary'] = df['max_salary'].fillna(df['min_salary']).astype(float)

    # Average salary
    df['avg_salary'] = (df['min_salary'] + df['max_salary']) / 2
    return df
