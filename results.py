import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hyperliquid Sentiment Analysis Dashboard")

merged = pd.read_csv("merged_dataset.csv")
merged["win"] = merged["Closed PnL"] > 0

# Performance by sentiment
perf = (
    merged.groupby("classification")
    .agg(
        avg_pnl=("Closed PnL", "mean"),
        win_rate=("win", "mean"),
        trades=("Closed PnL", "count")
    )
    .reset_index()
)

st.subheader("Performance by Sentiment")
st.dataframe(perf)

# Plot
fig, ax = plt.subplots()
ax.bar(perf["classification"], perf["avg_pnl"])
ax.set_title("Average PnL by Sentiment")
ax.set_ylabel("Avg PnL")
st.pyplot(fig)

# Trader segment selector
account = st.selectbox("Select Trader", merged["Account"].unique())

trader_data = merged[merged["Account"] == account]

st.subheader("Trader Performance")
st.write("Total PnL:", trader_data["Closed PnL"].sum())
st.write("Win Rate:", (trader_data["win"].mean()))
st.write("Total Trades:", len(trader_data))