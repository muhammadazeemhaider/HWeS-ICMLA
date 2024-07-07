import pandas as pd

df = pd.read_csv("oldData.csv")
df_pivoted = df.pivot(index='Account No', columns='Month', values='Electrical_Units')
df_pivoted.reset_index(inplace=True)

new_columns = {
    '2022-08-01': 'August 2022',
    '2022-09-01': 'September 2022',
    '2022-10-01': 'October 2022',
    '2022-11-01': 'November 2022',
    '2022-12-01': 'December 2022',
    '2023-01-01': 'January 2023',
    '2023-02-01': 'February 2023',
    '2023-03-01': 'March 2023',
    '2023-04-01': 'April 2023',
    '2023-05-01': 'May 2023',
    '2023-06-01': 'June 2023',
    '2023-07-01': 'July 2023',
    '2023-08-01': 'August 2023',
    '2023-09-01': 'September 2023',
    '2023-10-01': 'October 2023',
    '2023-11-01': 'November 2023',
    '2023-12-01': 'December 2023',
    '2024-01-01': 'January 2024'
}

df_pivoted.rename(columns=new_columns, inplace=True)

df_pivoted.to_csv("Data.csv", index=False)
