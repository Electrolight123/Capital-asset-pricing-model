# 📉 Capital Asset Pricing Model (CAPM) in Python

A simple, practical implementation of the **Capital Asset Pricing Model (CAPM)** to estimate:

- **Beta** (systematic risk) using:
  - covariance / variance formula
  - linear regression (Security Characteristic Line)
- **Alpha** (regression intercept)
- **CAPM expected return**
- A **scatter + regression line** plot of stock vs market returns

This project uses **Yahoo Finance data via `yfinance`**, resamples prices to **month-end**, and computes **log returns**.

---

## 🧠 CAPM Formula

\[
E[R_i] = R_f + \beta_i\,(E[R_m] - R_f)
\]

Where:
- \(R_f\) = risk-free rate  
- \(\beta_i\) = asset beta  
- \(E[R_m]\) = expected market return  

---

## ✅ Features

- Downloads historical prices for a stock and a market index
- Resamples to **month-end** (`'ME'`)
- Computes **logarithmic returns**
- Computes beta in two ways:
  - **Covariance matrix** method
  - **Linear regression** method (`np.polyfit`)
- Plots the **Security Characteristic Line** (SCL)
- Calculates **annualized expected return** (market mean × 12)

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt` should include:

- yfinance
- pandas
- numpy
- matplotlib

---

## 🚀 Usage

Run the script directly:

```bash
python capm.py
```

Or call the function in your own code:

```python
capm(
    start_date="2010-01-01",
    end_date="2025-01-01",
    ticker1="AAPL",
    ticker2="^GSPC"
)
```

### Parameters
- `start_date` / `end_date`: date strings like `"YYYY-MM-DD"`
- `ticker1`: stock ticker (e.g., `"AAPL"`)
- `ticker2`: market ticker (e.g., `"^GSPC"` for S&P 500)

---

## 📌 What the script prints

- Covariance matrix
- Beta from covariance formula
- Beta from regression
- CAPM expected return

Example outputs you’ll see:

- `Beta from formula: ...`
- `Beta from linear regression: ...`
- `Expected return according to CAPM: ...`

---

## 📊 Plot

The plot shows:
- X-axis: market log returns \(R_m\)
- Y-axis: stock log returns \(R_a\)
- Red line: fitted CAPM line  
  \[
  R_a = \alpha + \beta R_m
  \]

---

## 🗂 Project Structure

```
capital-asset-pricing-model/
├── capm.py
├── README.md
└── requirements.txt
```

---

## ⚠️ Notes

- This implementation uses **month-end resampling** via:
  - `data.resample('ME').last()`
- Market expected return is annualized as:
  - `data['m_return'].mean() * 12`
- Yahoo Finance data quality can vary (missing values, ticker symbol differences, etc.).

---

## 📝 License

MIT (or choose any license you prefer).

