import csv
import pandas as pd


#calculate average, maximum, and minimum ratings using nomal python
with open('/home/rahulkp/Desktop/AI/Libraries/Pandas/movies.csv') as file:
    data = list(csv.reader(file))
def calculate_rating(data, industry=None):
    rating = []
    for row in data:
        if row[3] != None and (not industry or row [1]==industry):
            try:
                rating.append(float(row[3]))

            except ValueError:
                continue
    max_rating = max(rating)
    min_rating = min(rating)
    avg_rating = sum(rating) / len(rating)
    return avg_rating, max_rating, min_rating
# header = data[0]
# data = data[1:]
# print("header:", header)
# print("Data:", data)
print("All Movies:")
min_rating, max_rating, avg_rating = calculate_rating(data)
print("Minimum Rating:", min_rating)
print("Maximum Rating:", max_rating)
print("Average Rating:", avg_rating)
# industry = input("Enter industry (or press Enter to skip): ")
industry = "Hollywood"
if industry:
    min_rating, max_rating, avg_rating = calculate_rating(data, industry)
    print(f"Minimum Rating for {industry}:", min_rating)
    print(f"Maximum Rating for {industry}:", max_rating)
    print(f"Average Rating for {industry}:", avg_rating)



# Using Pandas to calculate average, maximum, and minimum ratings
df = pd.read_csv('/home/rahulkp/Desktop/AI/Libraries/Pandas/movies.csv')
print(df.head())
print(df.head(3))
print(df.tail())
print(df.tail(7))
print("from random:\n",df.sample(3))
print("from 2 to 5:\n",df[2:6])
print("Rows and colums:", df.shape)
print("printing a colum:\n",df['imdb_rating'])
print("printing a colum as a property:\n",df.imdb_rating)
print("Statistics  of imdb_rating:\n",df.imdb_rating.describe())
print("type of df.imdb_rating: ",type(df.imdb_rating))
print("type of df", type(df))

# filtering df.imdb_rating

print("Hollywood Movies:\n",df[df.industry == 'Hollywood'])
print("Hollywood Movies avg rating\n",df[df.industry == 'Hollywood'].imdb_rating.mean())
print("Bollywood Movies min rating\n",df[df.industry == 'Bollywood'].imdb_rating.min(),)
df_hr = df[df.industry == "Hollywood"]
print("Hollywood Movies with rating > 8.5:\n", df_hr[df_hr.imdb_rating > 8.5])
print("Bollywood Movies with rating > 5.5:\n",df[(df.industry == "Bollywood") & (df.imdb_rating > 5.5)])
