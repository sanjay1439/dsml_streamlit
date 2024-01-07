import streamlit as st
import pandas as pd
import yfinance as yf

st.title("Stock_market App")
#streamlit run stock_market.py
st.write("this is hope to learn and earn")
ticker_data=yf.Ticker("AAPL")
hist=ticker_data.history(start="2022-05-31",end="2022-07-31")
st.write("I'm going to show you data of Apple stock")
st.write(hist)
st.write("This plot is for volume of stock")
st.line_chart(hist.Volume)
st.write("This plot is for price of the stock")
st.line_chart(hist.Close)