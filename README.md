

---

# **AI trading bot : Algorithmic Crypto Trading & Strategy Research Tool** 📈🤖

**Project Title:** AI-Powered Trading Strategy Simulator


## **📌 Executive Summary**

**AI-TradeSim** is a high-performance simulation framework designed for **Quantitative Analysis** and **Trading Strategy Backtesting**. Unlike standard bots, this project serves as a scientific tool to validate AI-driven technical indicators. It allows researchers to simulate market conditions, optimize hyperparameters, and analyze risk-to-reward ratios in a risk-free, 100% simulated environment.

---

## **🚀 Core Research Modules**

### **1. Strategy Engineering (AI Logic)**

The project uses modular Python classes to define "AI Agents." These agents analyze technical patterns like:

* **Momentum Analysis:** RSI and MACD crossovers.
* **Trend Tracking:** Fast and Slow Simple Moving Averages (SMA).
* **Predictive Optimization:** Using AI to find the "Sweet Spot" for stop-loss and take-profit triggers.

### **2. The Backtesting Engine**

The "Time Travel" feature allows you to run an AI strategy against historical data (e.g., Bitcoin data from 2021).

* **Accuracy:** Simulates slippage and exchange fees for a realistic result.
* **Granularity:** Supports 1m, 5m, 1h, and 1d candle timeframes.

### **3. Risk Management Dashboard**

A built-in analytics suite that generates:

* **Sharpe Ratio:** Measuring risk-adjusted return.
* **Drawdown Percentage:** Maximum potential loss during a strategy run.
* **Win/Loss Ratio:** Statistical probability of strategy success.

---

## **🛠️ Technical Implementation**

* **Language:** Python 3.9+
* **Framework:** Jesse (Customized for Simulation)
* **Architecture:** Event-driven architecture for real-time price simulation.
* **Library Dependencies:** `Numpy`, `Pandas`, `Matplotlib`, `Cython`.

### **Custom Strategy Sample**

This code demonstrates the "Logic Layer" where the AI decides to enter a trade based on Moving Average convergence:

```python
from jesse.strategies import Strategy
import jesse.indicators as ta

class IUB_Research_Strategy(Strategy):
    def should_long(self) -> bool:
        # AI Logic: Buy when 50 SMA crosses above 200 SMA
        return ta.sma(self.candles, 50) > ta.sma(self.candles, 200)

    def should_cancel_entry(self) -> bool:
        return True

```

---

## **📂 Repository Structure**

* `/strategies`: Contains unique AI logic files.
* `/storage`: Historical CSV data for simulations.
* `/docs`: Contains the **SRS and SDD** documents.
* `routes.py`: Configures which pairs and timeframes the AI should simulate.

---

## **💡 Why this is Unique?**

1. **Academic Integrity:** Explicitly labeled as a **Simulation Tool** to prevent misuse as a financial bot.
2. **Modular Design:** Follows **Software Engineering Blueprints**, making it easy to swap AI models.
3. **Data-Driven:** Focuses on statistical proof rather than "guessing" the market.

---

## **👨‍🏫 How to Use (For Evaluators)**

1. Install the environment: `pip install jesse`
2. Import historical data: `jesse import-candles Binance BTC USDT 2023-01-01`
3. Run the simulation: `jesse backtest 2023-01-01 2023-12-31`

---
