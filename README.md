# trader-sentiment-analysis
# 📊 Trader Behavior vs Market Sentiment Analysis

## 📌 Overview

This project analyzes how market sentiment (Fear/Greed) influences trader behavior and performance using real trading data. The goal is to uncover patterns that can inform smarter trading strategies.

---

## 🎯 Objectives

* Analyze relationship between market sentiment and trader performance
* Identify behavioral patterns (risk-taking, activity, win rate)
* Segment traders into distinct archetypes
* Build a predictive model for next-day profitability
* Develop an interactive dashboard for exploration

---

## 📂 Dataset

Two datasets were used:

1. **Bitcoin Market Sentiment**

   * Features: Date, Classification (Fear/Greed)

2. **Trader Data (Hyperliquid)**

   * Features: Account, Size USD, Closed PnL, Side, Timestamp, etc.

---

## ⚙️ Methodology

### 1. Data Preparation

* Converted timestamps to datetime format
* Aligned datasets using day-month mapping
* Handled missing values and inconsistencies

### 2. Feature Engineering

* Daily PnL per trader
* Win rate (profitability indicator)
* Trade size (risk proxy)
* Rolling win rate (momentum)
* Trade hour (behavioral pattern)

### 3. Exploratory Data Analysis (EDA)

* PnL vs Sentiment
* Win rate vs Sentiment
* Trade size & activity patterns
* PnL distribution analysis

### 4. Segmentation

Traders were grouped into:

* High vs Low risk (based on trade size)
* Frequent vs Infrequent traders
* Consistent winners vs losers

### 5. Predictive Modeling

* Model: Random Forest Classifier
* Task: Predict next-day profitability
* Features: behavior + sentiment

### 6. Clustering

Used KMeans to identify trader archetypes:

* Balanced traders
* Conservative traders
* High-risk, high-reward traders

---

## 📊 Key Insights

* Traders take larger positions during **Greed phases**, indicating higher risk appetite
* Profitability improves in bullish sentiment but not proportionally to risk
* Trading activity increases during extreme sentiment (Fear & Greed)
* Momentum (recent performance) is a strong predictor of future outcomes
* High-risk traders achieve higher returns but with significantly higher volatility

---

## 🤖 Model Performance

* Accuracy: ~69%
* Improved recall for profitable trades using feature engineering
* Model effectively identifies both profitable and unprofitable trades

> The model demonstrates that downside risk is easier to predict than upside opportunity.

---

## 💡 Strategy Recommendations

* Reduce position size during Fear phases
* Use momentum-based strategies (follow recent winners)
* Avoid aggressive trading during Extreme Greed
* Use predictive models as a risk filter
* Focus on risk management over trade frequency

---

## 📈 Dashboard

A lightweight Streamlit dashboard was built to:

* Visualize PnL, win rate, and trade size
* Filter by market sentiment
* Explore trading patterns interactively

### Run dashboard:

```bash
python -m streamlit run app.py
```

---

## 🚀 How to Run

### 1. Clone repository

```bash
git clone https://github.com/your-username/trader-sentiment-analysis.git
cd trader-sentiment-analysis
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

### 3. Run notebook

Open Jupyter Notebook and run all cells.

### 4. Run dashboard

```bash
python -m streamlit run app.py
```

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Streamlit

---

## 📌 Conclusion

This project demonstrates how combining market sentiment with trader behavior can uncover meaningful insights and improve decision-making in trading systems.

---

## 👤 Author

Aayush Kumar Dubey
