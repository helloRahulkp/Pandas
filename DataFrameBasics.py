import pandas as pd

df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/movies.csv')
print(df.head(3))
print(df.tail(3))

print("Rows and columns:", df.shape)
print("Printing a column:\n", df['title'])
print("All columns:\n", df.columns)
print("Unique industries:\n", df.industry.unique())
print("Unique release years:\n", df.release_year.unique())
print("Count of unique release years:\n", df.release_year.nunique())
print("Unique languages: \n", df.language.unique())
print("Count of unique languages:\n", df.language.nunique())

print("Count of Industries:\n", df.industry.value_counts())
print("Count of Languages:\n", df.language.value_counts())
print("Count of Release Years:\n", df.release_year.value_counts())
print("Count of Industries and Languages:\n", df.groupby(['industry', 'language']).size())
print("Count of Industries and Release Years:\n", df.groupby(['industry', 'release_year']).size())
print("Count of Languages and Release Years:\n", df.groupby(['language', 'release_year']).size())
print("Count of Industries, Languages, and Release Years:\n", df.groupby(['industry', 'language', 'release_year']).size())


print("Language Movies count: \n", df.language.value_counts())
df_new = df[['title', 'imdb_rating', 'release_year']]
print("Sub dataframe\n", df_new)
print("Sub dataframe head :\n", df_new.head(3), "\nand tail: \n", df_new.tail(3))

print("Release year 2015 movies: \n", df[df.release_year == 2015])
print("Release year 2010 to 2020 movies: \n", df[df.release_year.between(2010, 2020)])
print("Rlease year greter than 2000 and less than 2010 movies: \n", df[(df.release_year > 2000) & (df.release_year < 2020)])
print("Release year 2010 to 2020 movies with rating greater than 7.5: \n", df[df.release_year.between(2010, 2020) & (df.imdb_rating > 7.5)])

df_marvel = df[df.studio == 'Marvel Studios']
print("Movies from marvel studios:\n", df_marvel)
print("Number of marvel movies:\n", df.studio.value_counts()['Marvel Studios'])
print("Number of marvel movies:\n", df_marvel.shape, "\nfrom this there are 8 rows and 10 columns, so the number of movies becom rows:\n", df_marvel.shape[0])
print("Statistics of marvel movies:\n", df_marvel.describe())

print("To identify null values in the dataframe:\n", df.isnull().sum())
print("To identify null values in the dataframe",df.info())

print("Max imbd  rating and minimum rating movies:\n", df[(df.imdb_rating == df.imdb_rating.max()) | (df.imdb_rating == df.imdb_rating.min())])
print(df.head(3))
df['age'] = 2025 - df.release_year
print("Dataframe with age column:\n", df)
print(df.columns)
df_finance = df[[ 'studio','currency', 'budget', 'revenue']]
print("Sub dataframe for finance:\n", df_finance)
df_finance.loc[df_finance.currency == 'USD', 'budget'] *= 80
df_finance.loc[df_finance.currency == 'USD', 'revenue'] *= 80
df_finance.loc[df_finance.currency == 'USD', 'currency'] = 'INR'
df_finance['profit'] = df_finance.revenue - df_finance.budget
print("Dataframe with profit column:\n", df_finance)

print("Index of the dataframe:\n", df.index)
df.set_index('title', inplace=True)
print("Dataframe with title as index:\n", df)
print("Dataframe with title as index :\n", df.index)

print("Data for Avatar:\n", df.loc['Avatar'])
print("Data for Avatar and Avengers:\n", df.loc[['Avatar', 'Avengers: Infinity War']])