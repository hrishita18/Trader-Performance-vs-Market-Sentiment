<h1>Hyperliquid Sentiment Analysis</h1>

<b> (The methodology and insights for this assignment are included at the end of the ipynb file in a markdown cell.) </b>

This project analyzes how market sentiment (Fear vs Greed) relates to trader behavior and performance on Hyperliquid.
The goal is to identify patterns in trading outcomes and derive actionable strategy recommendations.

The analysis combines:

- Fear & Greed Index data (daily sentiment)

- Historical trade data (per-trade records)

The datasets are aligned by date and used to compute performance and behavioral metrics such as:

- Daily PnL

- Win rate

- Trade frequency

- Average trade size

- Long/short ratio

The analysis then compares these metrics across sentiment conditions and trader segments.

<h2>Key Objectives</h2>

- Compare performance during Fear vs Greed periods

- Identify behavioral changes across sentiment

- Segment traders by activity, consistency, and leverage proxy

- Derive actionable trading strategies

<h2>Requirements</h2>
Python 3.9+ is recommended.

```python
pip install pandas matplotlib scikit-learn
```
For streamlit:
```python
pip install streamlit
```
Setup instructions:
Clone or download the repository.
Keep the datasets (not included in the repository due to large size) and the .ipynb file in the same directory. 
Run all the cells in the order given.
The notebook produces three .csv files (not included in the repository due to large file size):

- merged_dataset.csv
- daily_metrics.csv
- trader_clusters.csv

In order to run streamlit script:
Make sure you are running the script in the directory where the dataset and the script is present. 
results.py requires merged_dataset.csv which is not included in the repository but it is produced when you run the actual internship_assignment.ipynb file

```python
streamlit run results.py
```
