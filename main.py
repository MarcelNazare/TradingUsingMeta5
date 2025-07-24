import os
from dotenv import load_dotenv
import MetaTrader5 as mt
from datetime import datetime
import pandas as pd
from analysis import calculate_adx

# Paths
CSV_PATH = '/csv/'

# Custom Print function 
def printer(msg:str) -> str:
    print(f"[+] {str(msg)}")

# Loading the enviroment keys and we will store our login details in the dotenv file
load_dotenv()
login_keys = {
    "LOGIN_KEY" : os.getenv("LOGIN_KEY"),
    "PASS_KEY": os.getenv("PASS_KEY"),
    "SERVER_KEY": os.getenv("SERVER_KEY"),
}

# Symbol Selector Function
symbols = ('EURUSD','GBPUSD','JPYUSD','CADUSD','XAUUSD')
def select_symbol(symbols):
    for symbol in range(len(symbols)):
        printer(f"Type {symbol} for {symbols[symbol]}")
    selector = int(input("Select Trading Pair -> "))
    selected_symbol  = symbols[selector]
    return selected_symbol

# Setting Timeframes
timeframes ={
    "TM-I-MINUTE" : mt.TIMEFRAME_M1,
    "TM-5-MINUTE" : mt.TIMEFRAME_M5,
    "TM-15-MINuTE": mt.TIMEFRAME_M15,
    "TM-30-MINUTE": mt.TIMEFRAME_M30,
    "TM-1-HOUR": mt.TIMEFRAME_H1,
    "TM-4-HOUR": mt.TIMEFRAME_H4,
    "TM-1-DAY": mt.TIMEFRAME_D1,
    "TM-1-WEEK": mt.TIMEFRAME_W1,
}

# Timeframe selector funtion
def select_timeframe(timeframes):
    time_frame_list = list(timeframes.keys())
    new_list = time_frame_list
    for marker in range(len(new_list)):
        printer(f"Type {marker} for {new_list[marker]}")
    marker_selector = int(input("Choose Time Frame -> "))
    selected_timeframe = timeframes[new_list[marker_selector]]
    timeframe_marker = new_list[marker_selector]
    return selected_timeframe, timeframe_marker

# Here we initialize the MetaTrader5 package
# And we provide our login details so we can login into out Meta account
# This account will be a gateway to our broker account
def login(login,password,server) -> bool:
    mt.initialize()
    mt.login(login,password,server)
    account_info = mt.account_info()
    account_info = account_info._asdict()
    acc_loggedIn = account_info["login"]
    print(f"ACCOUNT INITIALIZED FOR -> {str(acc_loggedIn)}")
    return True

# Copy rates function - We copy the rates from MetaTrader5
def copyrates(symbol,timeframe,from_date,no_rows) -> any:
    rates = mt.copy_rates_from(symbol,timeframe,from_date,no_rows)
    return rates

# Convert to Dataframe
def convert_to_dataframe(data) -> any:
    data = pd.DataFrame(data)
    return data
 
# The idea is to perform some data analysis on the current data within the Terminal
def data_analysis(data) -> None:
    #Perform some basic analysis on the data.
    period = int(input("Please choos the period you want to run your analysis on"))
    printer("Performing data analysis...")
    printer("Calculating the ADX (Average Directional Index)")
    printer(calculate_adx(data,period).mean())
    printer("Data analysis completed.") 


def save_to_csv(data, filename="rates.csv") -> None:
    #Save the DataFrame to a CSV file.
    name = filename
    date = datetime.now()
    file =f"{CSV_PATH}/{name}-{date}"
    file = filename
    data.to_csv(filename, index=True)
    printer(f"Data saved to {file}")
## Indicators

if __name__ == "__main__":
    def main():
        try:
            # Login Function,
            login = login(login_keys["LOGIN_KEY"],login_keys["PASS_KEY"],login_keys["SERVER_KEY"])
            # Checking if the login was successful
            if not login:
                raise Exception("Login failed, please check your credentials.") 
            else:    
                printer("Login successful, proceeding to copy rates...")
                # Copying the rates from MetaTrader5
                # This function allows you to select a trading pair    
                symbol = select_symbol(symbols)
                time_frame_selected = select_timeframe(timeframes)
                time_frame_marker = time_frame_selected[0]
                chosen_time_frame = time_frame_selected[1]
                printer(f"You chose the {chosen_time_frame} timeframe")
                data_range = 2000
                from_date = datetime.now()
                rates = copyrates(symbol,time_frame_marker,from_date,data_range)
                printer(f"Rates copied successfully -> {str(rates)}")   
                #Converting the data into a Pandas DataFrame
                data = convert_to_dataframe(rates)
                printer(f"Data converted to DataFrame successfully -> {str(data)}")
                data['time'] =pd.to_datetime(data['time'],unit='s')
                data.set_index('time', inplace=True)
                printer("Data is ready for analysis.")
                data_analysis(data)
                # Saving the data to a CSV file
                printer("Saving data to CSV file...")
                save_to_csv(data, "eurusd_rates.csv")   
                # Do some anlysis with the data
                printer("Analysis completed, data saved to CSV file.") 
        # Catching errors 
        except Exception as e:
            printer(f"Oops there is a problem, Check if you connected to the Internet -> {e}")

    ##########################################################################################
    #main()
    symbol = select_symbol(symbols)
    time_frame_selected = select_timeframe(timeframes)
    time_frame_marker = time_frame_selected[0]
    chosen_time_frame = time_frame_selected[1]
    printer(f"You selected {symbol}")
    printer(f"You chose the {chosen_time_frame} timeframe")
    data = pd.read_csv('eurusd_rates.csv')
    data_analysis(data)
 

  


    