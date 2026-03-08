# =========================
# Import Libraries
# =========================
import pandas as pd
import matplotlib.pyplot as plt
import os
os.makedirs("images", exist_ok=True)
# =========================
# Load Dataset
# =========================
df = pd.read_csv(r"C:\Users\mkart\OneDrive\Desktop\movie insights project\movie_dataset.csv")
# =========================
# Data Cleaning
# =========================
df['release_date'] = pd.to_datetime(df['release_date'])
# =========================
# Feature Engineering
# =========================
df['year'] = df['release_date'].dt.year
# =========================
# Movies Released Per Year
# =========================
movies_per_year = df['year'].value_counts().sort_index()
print(movies_per_year)
movies_per_year.plot()
plt.title("number of movies released per year")
plt.xlabel("year")
plt.ylabel("number of movies")
plt.savefig("images/movies_per_year.png")
plt.show()
# =========================
# Top Movie Genres
# =========================
df['genres'] = df['genres'].str.split(',')
df = df.explode('genres')
genre_counts = df['genres'].value_counts()
top_genres = genre_counts.head(10)
top_genres.plot(kind='bar')
plt.title("top 10 movie genres")
plt.xlabel("genre")
plt.ylabel("number of movies")
plt.savefig("images/genre_counts.png")
plt.show()
# =========================
# Language Distribution
# =========================
language = df['original_language'].value_counts().head(10)

language.plot(kind='bar')

plt.title("Original Language vs Number of Movies")
plt.xlabel("Language")
plt.ylabel("Number of Movies")
plt.savefig("images/language.png")
plt.show()
# =========================
# Top Rated Movies
# =========================
top_rated = df.sort_values(by='vote_average', ascending=False).head(10)
top_rated.plot(x='title', y='vote_average', kind='bar')
plt.title("Top 10 Highest Rated Movies")
plt.xlabel("Movie Title")
plt.ylabel("Average Rating")
plt.savefig("images/top_rated.png")
plt.show()
# =========================
# Popularity vs Rating
# =========================
plt.scatter(df['popularity'], df['vote_average'])

plt.title("Popularity vs Average Rating")
plt.xlabel("Popularity")
plt.ylabel("Average Rating")
plt.savefig("images/popularity_vs_rating.png")
plt.show()
# =========================
# Most Voted Movies
# =========================
most_voted = df.sort_values(by='vote_count', ascending=False).head(10)
most_voted.plot(x='title',y='vote_count',kind='bar')
plt.title("Top 10 movies  Most voted ")
plt.xlabel("MovieTitle")
plt.ylabel("number of votes")
plt.savefig("images/most_voted.png")
plt.show()
# =========================
# Genre Trends Over Time
# =========================
genre_trend = df.groupby(['year','genres']).size().unstack().fillna(0)
genre_trend[['Drama','Comedy','Action']].plot()
plt.title("Genre Trends Over time")
plt.xlabel("Year")
plt.ylabel("Number of movies")
plt.savefig("images/genre_trend.png")
plt.show()

print(df.head(10))
df.info()
