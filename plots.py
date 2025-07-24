import plotly.express as px
from IPython.display import display, Markdown, Latex
import pandas as pd
from analysis import calculate_adx
import plotext as plt
# The idea is to display these  plots in the terminal

df = pd.read_csv('eurusd_rates.csv')

def plot_close_prices(data):
    fig = px.line(data,x='time',y='close',title='EURO USD - CLOSE PRICES')
    display(fig)

# Simple Moving Average
def sma(period:int,data):
    df = data
    sma_period = period
    df['sma_10'] = df['close'].rolling(sma_period).mean()
    display(Markdown("Notice as we have NaN values in the beginning as our least 20 values to calculate the SMA"))
    display(df[['time','close','sma_10']])
    fig_sma = px.line(df,x='time',y=['close','sma_10'],title='SMA Indicator')
    display(fig_sma)

# Plotting the ADX
period = 10
adx = calculate_adx(df,period)
def plot_Onto(data,adx):
    df = data
    #avg = adx
    df['ADX'] = adx
    #display(df[['time','ADX']])
    #fig = px.line(df,x='time',y='ADX',title = f"ADX - {avg}")
    #return display(fig)
    y = adx
    plt.plot(y)
    plt.title("Plot")
    return plt.show()

plot_Onto(df,adx)


import plotext as plt 
y = plt.sin()
plt.scatter(y)
plt.title("scatter plot")
plt.show()
