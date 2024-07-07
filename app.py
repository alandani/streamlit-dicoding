import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

all_df = pd.read_csv("content/hour.csv")

all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)

all_df["dteday"] = pd.to_datetime(all_df["dteday"])
# st.dataframe(all_df.head())

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

# ---------------------------------------------------

st.header('Dicoding Bike Sharing Dashboard :sparkles:')

st.subheader('Bike Orders by Weather')

data_weather = main_df.groupby('weathersit')['cnt'].mean().reset_index().sort_values("cnt")

fig, ax = plt.subplots(figsize=(16, 8))
sns.barplot(x='weathersit', y='cnt', data=data_weather, ax=ax, palette='viridis')
ax.set_title('Total Number of Bike Sharing in Different Weather')

st.pyplot(fig)

# ---------------------------------------------------

st.subheader('Bike Orders by Hour')

fig, ax = plt.subplots(figsize=(16, 8))
sns.pointplot(data=main_df, x='hr', y='cnt', hue='weekday', ax=ax, palette='muted')
ax.set_title('Count of Bikes by Hour')
ax.set_xlabel('Hour')
ax.set_ylabel('Count')
 
st.pyplot(fig)



