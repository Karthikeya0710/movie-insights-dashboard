import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# Load Dataset
# =========================

df = pd.read_csv("movie_dataset.csv")

# =========================
# Data Preparation
# =========================

df['release_date'] = pd.to_datetime(df['release_date'])
df['year'] = df['release_date'].dt.year

df['genres'] = df['genres'].str.split(',')
df_genres = df.explode('genres')

# =========================
# Dashboard Title
# =========================

st.title("🎬 Movie Insights Dashboard")

# =========================
# Sidebar Navigation
# =========================

section = st.sidebar.selectbox(
    "Select Analysis",
    [
        "Dataset Preview",
        "Movies Per Year",
        "Top Genres",
        "Language Distribution",
        "Top Rated Movies",
        "Popularity vs Rating",
        "Most Voted Movies",
        "Genre Trend Over Time"
    ]
)

# =========================
# Dataset Preview
# =========================

if section == "Dataset Preview":
    st.write("### Dataset Preview")
    st.dataframe(df.head())

# =========================
# Movies Released Per Year
# =========================

elif section == "Movies Per Year":

    movies_per_year = df['year'].value_counts().sort_index()

    st.write("## Movies Released Per Year")

    fig, ax = plt.subplots()
    movies_per_year.plot(ax=ax)

    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Movies")
    ax.set_title("Movies Released Per Year")

    st.pyplot(fig)

    st.write("Insight: Movie production increased significantly after the year 2000.")

# =========================
# Top Genres
# =========================

elif section == "Top Genres":

    genre_counts = df_genres['genres'].value_counts().head(10)

    st.write("## Top 10 Movie Genres")

    fig, ax = plt.subplots()
    genre_counts.plot(kind='bar', ax=ax)

    ax.set_xlabel("Genre")
    ax.set_ylabel("Number of Movies")
    ax.set_title("Top Genres")

    st.pyplot(fig)

    st.write("Insight: Drama and Comedy appear most frequently in the dataset.")

# =========================
# Language Distribution
# =========================

elif section == "Language Distribution":

    language_counts = df['original_language'].value_counts().head(10)

    st.write("## Top Languages")

    fig, ax = plt.subplots()
    language_counts.plot(kind='bar', ax=ax)

    ax.set_xlabel("Language")
    ax.set_ylabel("Number of Movies")
    ax.set_title("Language Distribution")

    st.pyplot(fig)

# =========================
# Top Rated Movies
# =========================

elif section == "Top Rated Movies":

    top_rated = df.sort_values(by='vote_average', ascending=False).head(10)

    st.write("## Top Rated Movies")

    fig, ax = plt.subplots()
    top_rated.plot(x='title', y='vote_average', kind='bar', ax=ax)

    ax.set_xlabel("Movie Title")
    ax.set_ylabel("Rating")
    ax.set_title("Top Rated Movies")

    st.pyplot(fig)

# =========================
# Popularity vs Rating
# =========================

elif section == "Popularity vs Rating":

    st.write("## Popularity vs Rating")

    fig, ax = plt.subplots()
    ax.scatter(df['popularity'], df['vote_average'])

    ax.set_xlabel("Popularity")
    ax.set_ylabel("Average Rating")
    ax.set_title("Popularity vs Rating")

    st.pyplot(fig)

    st.write("Insight: Most highly popular movies tend to have ratings between 6 and 8.")

# =========================
# Most Voted Movies
# =========================

elif section == "Most Voted Movies":

    most_voted = df.sort_values(by='vote_count', ascending=False).head(10)

    st.write("## Most Voted Movies")

    fig, ax = plt.subplots()
    most_voted.plot(x='title', y='vote_count', kind='bar', ax=ax)

    ax.set_xlabel("Movie Title")
    ax.set_ylabel("Number of Votes")
    ax.set_title("Most Voted Movies")

    st.pyplot(fig)

# =========================
# Genre Trend Over Time
# =========================

elif section == "Genre Trend Over Time":

    genre_trend = df_genres.groupby(['year','genres']).size().unstack().fillna(0)

    st.write("## Genre Trend Over Time")

    fig, ax = plt.subplots()
    genre_trend[['Drama','Comedy','Action']].plot(ax=ax)

    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Movies")
    ax.set_title("Genre Trends")

    st.pyplot(fig)