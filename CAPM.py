# import pandas_datareader as pdr
# from pandas_datareader import data, wb 
import yfinance as yf
from datetime import date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

risk_free_rate = 0.05

def capm(start_date, end_date, ticker1, ticker2):

    # Get the stock data for the two tickers
    stock1 = yf.download(ticker1, start=start_date, end=end_date, auto_adjust=False, progress=False)
    stock2 = yf.download(ticker2, start=start_date, end=end_date, auto_adjust=False, progress=False)

    # If yfinance returns MultiIndex columns, flatten them so 'Adj Close' works
    if isinstance(stock1.columns, pd.MultiIndex):
        stock1.columns = stock1.columns.get_level_values(0)

    if isinstance(stock2.columns, pd.MultiIndex):
        stock2.columns = stock2.columns.get_level_values(0)

    #we prefer monthly returns instead of daily returns
    return_stock1 = stock1.resample('M').last()
    return_stock2 = stock2.resample('M').last()

    #creating a dataframe from the data - Adjusted closing price is used as usual
    data = pd.DataFrame({
        's_adjclose': return_stock1['Adj Close'],
        'm_adjclose': return_stock2['Adj Close']},
        index=return_stock1.index
    )
    #natural logarithm of the returns
    data[['s_return', 'm_return']] = np.log(data[['s_adjclose', 'm_adjclose']]/data[['s_adjclose', 'm_adjclose']].shift(1))
    #no need for NaN/missing values so let's drop them
    data = data.dropna()

    #covariance matrix: the diagonal items are the variances - off diagonals are the covariances
    #the matrix is symmetric: cov[0,1] = cov[1,0] !!!
    cov_matrix = np.cov(data['s_return'], data['m_return'])
    print(cov_matrix)

    #calculating beta according to the formula 
    beta = cov_matrix[0,1] / cov_matrix[1,1]
    print("Beta from formula: ", beta)

    #using linear regression to fit a line to the data [stock_return, market_return] - slope of the line is the beta
    beta,alpha = np.polyfit(data['m_return'], data['s_return'], deg=1)
    print("Beta from linear regression: ", beta)

    #plot 
    fig,axis = plt.subplots(1,figsize=(20,10))
    axis.scatter(data['m_return'], data['s_return'], color='blue', label='Data Points')
    axis.plot(data['m_return'], alpha + beta * data['m_return'], color='red', label='CAPM Line')
    plt.title("Capital Asset Pricing Model, finding alpha and beta")
    plt.xlabel("Market Return $R_m$", fontsize=18)
    plt.ylabel("Stock Return $R_a$", fontsize=18)
    plt.text(0.08, 0.05, r'$R_a = \beta * R_m + \alpha$', fontsize=18)
    plt.legend()
    plt.grid(True)
    plt.show()

    #calculate the expected return according to the CAPM formula: E[R] = Rf + beta * (E[Rm] - Rf)
    expected_return = risk_free_rate + beta * (data['m_return'].mean()*12 - risk_free_rate)
    print("Expected return according to CAPM: ", expected_return)

if __name__ == "__main__":
    #using historical data 2010-2025: the market is the S&P 500 index and the stock is Apple Inc.
    capm(start_date='2010-01-01', end_date='2025-01-01', ticker1='AAPL', ticker2='^GSPC')

