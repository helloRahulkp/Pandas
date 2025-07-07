import pandas as pd

df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/weather_data.csv')
print("Dataframe:\n", df)
print("Dataframe shape:", df.shape)
print("Dataframe columns:", df.columns)
print("Dataframe info:\n", df.info())
print("Dataframe head:\n", df.head(3))
print("Dataframe tail:\n", df.tail(3))
print("Dataframe is null:\n", df.isnull())
print("Dataframe is null sum:\n", df.isnull().sum())

print("Type of day column:\n", type(df['day']))
print("Type of day column values:\n", type(df.day[0]))

# change date colum as the data type of date
df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/weather_data.csv', parse_dates=['day'])
print("Dataframe with day as date type:\n", df)
print("Dataframe info after parsing dates:\n", df.info())
print("Type of day column:\n", type(df['day']))
print("Type of day column values:\n", type(df.day[0]))

# set index to day column

df.set_index('day',inplace=True)
print("Dataframe with day as index:\n", df)




# filling all the NaN values with zero
df_with_zero=df.fillna(0)
print("Dataframe after filling NaN with 0:\n", df_with_zero)



# fill NaN values with ffill method forward fill

ffill_method=df.fillna(method='ffill')
print("Dataframe after filling NaN values with ffill method:\n", ffill_method)

# setting limit on ffill method to fill only 1 NaN value
ffill_method_limit=df.fillna(method='ffill', limit=1)
print("Dataframe after filling NaN values with ffill method with limit 1:\n", ffill_method_limit)

# fill NaN values with bfill method backward fill

bfill_method=df.fillna(method='bfill')
print("Dataframe after filling NaN values with bfill method:\n", bfill_method)

# fill NaN values with median of the column
df_median=df.fillna({
    'temperature': df['temperature'].median(),
    'windspeed': df['windspeed'].median(),
    'event': 'No Event'
})
print("Dataframe after filling NaN values with median:\n", df_median)

# linear grapgh interpolation
df_interpolate=df.interpolate()
print("Dataframe after filling NaN values with linear interpolation:\n", df_interpolate)

# drop rows with NaN values
df_dropna=df.dropna(how='all')  # 'all' drops rows where all elements are NaN
# df_dropna=df.dropna(how='any')  # 'any' drops rows
print("Dataframe after dropping rows with NaN values:\n", df_dropna)

