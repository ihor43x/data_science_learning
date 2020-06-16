import pandas as pd
import re

"""Reading CSV file"""
# df_csv = pd.read_csv('KeithGalli/pokemon_data.csv')
# print(df_csv)
# print(df_csv.head(3))
# print(df_csv.tail(3))

"""Reading XLSX file"""
df_xlsx = pd.read_excel('KeithGalli/pokemon_data.xlsx')
# print(df_xlsx)
# print(df_xlsx.head(3))

"""Reading TXT file"""
# df_txt = pd.read_csv('KeithGalli/pokemon_data.txt', delimiter='\t')
# print(df_txt)

"""Reading data"""
# print(df_xlsx.columns)  # Get columns headers
# print(df_xlsx['Name'][0:5])  # Get top 5 rows
# print(df_xlsx[['Name', 'HP']])  # Get multi columns
# print(df_xlsx.iloc[1])  # Get particular row ([1:4] also works)
# print(df_xlsx.iloc[1, 2])  # Get specific location

# for index, row in df_xlsx.iterrows():  # Read each row
#     print(index, row['Name'])

# print(df_xlsx.loc[df_xlsx['Type 1'] == "Fire"])  # Get filtered data

# print(df_xlsx.describe())  # Short overview
# print(df_xlsx.sort_values('Name', ascending=False))  # Sorting
# print(df_xlsx.sort_values(['Type 1', 'HP'], ascending=[1, 0]))  # Sorting

"""Create calculated column"""
# df_xlsx['Total'] = df_xlsx['HP'] + df_xlsx['Attack'] + \
#                    df_xlsx['Defense'] + df_xlsx['Sp. Atk'] + \
#                    df_xlsx['Sp. Def'] + df_xlsx['Speed']
# print(df_xlsx.head(2))
# df_xlsx.drop(columns=['Total']) # Remove column
# print(df_xlsx.head(2))
#
# df_xlsx['Total'] = df_xlsx.iloc[:, 4:10].sum(axis=1)  # axis=0 - vertically, 1 - horizontally
# cols = list(df_xlsx.columns.values)
# df_xlsx = df_xlsx[cols[0:4] + [cols[-1]] + cols[4:12]]  # Change columns order
# print(df_xlsx.head(2))

""""Write data to file"""
# df_xlsx.to_csv('KeithGalli/modified.csv', index=False)
# df_xlsx.to_csv('KeithGalli/modified.txt', index=False, sep='\t')
# df_xlsx.to_excel('KeithGalli/modified.xlsx', index=False)

"""Filtering Data"""
# x = df_xlsx.loc[(df_xlsx['Type 1'] == 'Grass') & (df_xlsx['Type 2'] == 'Poison')]
# print(x)

# x = df_xlsx.loc[(df_xlsx['Type 1'] == 'Grass') | (df_xlsx['Type 2'] == 'Poison')]
# print(x)
# x.to_csv('KeithGalli/modified2.txt', index=False, sep='\t')

# new_df = df_xlsx.loc[(df_xlsx['Type 1'] == 'Grass') &
#                      (df_xlsx['Type 2'] == 'Poison') &
#                      (df_xlsx['HP'] > 70)]
# new_df = new_df.reset_index()  # drop=True, inplace=True
# new_df.to_excel('KeithGalli/filtered.xlsx')

# print(df_xlsx.loc[df_xlsx['Name'].str.contains('Mega')])  # Names contains "Mega"
# print(df_xlsx.loc[~df_xlsx['Name'].str.contains('Mega')])  # (~) - Excludes names contains "Mega"

"""Filter using RegEx"""
# flags=re.I - Case insensitive
# print(df_xlsx.loc[df_xlsx['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])
# print(df_xlsx.loc[df_xlsx['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])

"""Conditional Changes"""
# print(df_xlsx.loc[df_xlsx['Type 1'] == 'Fire'])
# df_xlsx.loc[df_xlsx['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# print(df_xlsx.loc[df_xlsx['Type 1'] == 'Flamer'])

# df_xlsx.loc[df_xlsx['Type 1'] == 'Fire', 'Legendary'] = True
# print(df_xlsx.loc[df_xlsx['Type 1'] == 'Fire'])

# df_xlsx['Total'] = df_xlsx['HP'] + df_xlsx['Attack'] + \
#                    df_xlsx['Defense'] + df_xlsx['Sp. Atk'] + \
#                    df_xlsx['Sp. Def'] + df_xlsx['Speed']
# df_xlsx.loc[df_xlsx['Total'] > 500, ['Generation', 'Legendary']] = ['Multiple', 'Change']
# print(df_xlsx)

"""Aggregate Statistics (Group by)"""
# new_df = df_xlsx.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)
# new_df.to_excel('KeithGalli/grouped.xlsx')

# print(df_xlsx.groupby(['Type 1']).sum())
#
# print(df_xlsx.groupby(['Type 1']).count())

# df_xlsx['count'] = 1
# print(df_xlsx.groupby(['Type 1']).count()['count'])

# df_xlsx['count'] = 1
# print(df_xlsx.groupby(['Type 1', 'Type 2']).count()['count'])

"""Working with large amounts of data"""
# new_df = pd.DataFrame(columns=df_xlsx.columns)
# for df in pd.read_csv('KeithGalli/pokemon_data.csv', chunksize=5):
#     results = df.groupby(['Type 1']).count()
#     new_df = pd.concat([new_df, results])
#     # print("CHUNK DF")
#     # print(df)
# print(new_df)
# new_df.to_excel('KeithGalli/concated.xlsx')