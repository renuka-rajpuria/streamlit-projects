#https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#https://youtu.be/ZZ4B0QUHuNc
#https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and **volume** of Google!
""")
#define the ticker symbol where symobol is the name of the company stock as listed
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period = '1d', start = '2020-2-3', end = '2023-2-3')
#Open High Low Close Volume Dividends Stock Splits -> are the columns of this dataframe
st.write("""
## Stock Close Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Stock Volume
""")
st.line_chart(tickerDf.Volume)
