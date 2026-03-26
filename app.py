import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Trader Sentiment Dashboard", layout="wide")

# Title
st.title("📊 Trader Behavior vs Market Sentiment")

# Load data
df = pd.read_csv("final.csv")

# Sidebar filter
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.selectbox(
    "Select Market Sentiment",
    options=df['classification'].dropna().unique()
)

filtered_df = df[df['classification'] == sentiment_filter]

# --- Metrics ---
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Avg PnL", round(filtered_df['Closed PnL'].mean(), 2))
col2.metric("Avg Trade Size", round(filtered_df['Size USD'].mean(), 2))
col3.metric("Win Rate", round((filtered_df['Closed PnL'] > 0).mean(), 2))

# --- Charts ---
st.subheader("📈 Analysis")

# PnL by sentiment
st.write("Average PnL by Sentiment")
st.bar_chart(df.groupby('classification')['Closed PnL'].mean())

# Trade size
st.write("Average Trade Size by Sentiment")
st.bar_chart(df.groupby('classification')['Size USD'].mean())

# Win rate
df['win'] = df['Closed PnL'] > 0
st.write("Win Rate by Sentiment")
st.bar_chart(df.groupby('classification')['win'].mean())

# --- Raw Data ---
st.subheader("🔍 Sample Data")
st.dataframe(filtered_df.head(100))

