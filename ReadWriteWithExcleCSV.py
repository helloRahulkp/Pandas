import pandas as pd

df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/stock_data.csv')
print("Dataframe :\n", df)
new_df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/stock_data.csv', skiprows=1)
print("New Dataframe :\n", new_df)
new_df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/stock_data.csv', header=1)
print("New Dataframe with header :\n", new_df)
new_df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/stock_data.csv', header=1, names=['stock symbol', 'eps', 'revenue', 'price', 'people'])
print("New Dataframe with no header :\n", new_df)
new_df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/stock_data.csv', nrows=2)
print("New Dataframe with only 2 rows :\n", new_df)
new_df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/stock_data.csv',header=1, na_values={
    'eps': ['N/A', 'NaN', 'null','not available'],
    'revenue': ['N/A', 'NaN', 'null', -1],
    'price': ['N/A', 'NaN', 'null','n.a.', -1],
    'people': ['N/A', 'NaN', 'null', -1]
})
print("New Dataframe without na values :\n", new_df)

new_df['ratio'] = new_df['price'] / new_df['eps']
print("Dataframe with ratio column:\n", new_df)
new_df.to_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/stock_data_new_ratio.csv',index=False)

df_movies = pd.read_excel('/home/rahulkp/Desktop/AI/Libraries/Pandas/movies_db.xlsx','movies')
print("Movies Dataframe from Excel:\n", df_movies)

def standard_curency(currency):
    if currency == 'usd' or currency == 'UsD' or currency == '$$' or currency == 'Dollars':
        return 'USD'
    return currency

df_finance = pd.read_excel('/home/rahulkp/Desktop/AI/Libraries/Pandas/movies_db.xlsx','financials', converters={
    'currency': standard_curency
})
print("Finance Dataframe from Excel:\n", df_finance)

df_merged = pd.merge(df_movies, df_finance, on='movie_id')
print("Merged Dataframe:\n", df_merged)
df_merged.to_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/movies_financials_merged.csv', index=False)