import pandas as pd
import numpy as np
# Calculating the ADX (Average Directional Index)

def calculate_adx(data,period:int):
    df = data
    #Calculate Directional Movement (DM)
    df['upMove'] = df['high'] -df['high'].shift(1)
    df['downMove'] = df['low'].shift(1) - df['low']
    df['+DM'] = np.where((df['upMove']>df['downMove']) & (df['upMove']>0),df['upMove'],0)
    df['-DM'] = np.where((df['downMove']>df['upMove']) & (df['downMove']>0),df['downMove'],0)
    # Calculating True Range (TR)
    df['TR1'] = df['high'] - df['low']
    df['TR2'] = abs(df['high']-df['close'].shift(1))
    df['TR3'] = abs(df['low']-df['close'].shift(1))
    df['TR'] = df[['TR1','TR2','TR3']].max(axis=1)
    # Calculating Avarege True Range (ATR)
    df['ATR'] = df['TR'].ewm(span=period,adjust=False).mean()
    # Calculating Directional Indicators (DI)
    df['+DI'] = 100 * (df['+DM'].ewm(span=period,adjust=False).mean()/df['ATR'])
    df['-DI'] = 100 * (df['-DM'].ewm(span=period,adjust=False).mean()/df['ATR'])
    # Calculating Directional Incex (DX)
    df['DX'] =  100 * (abs(df['+DI'] - df['-DI'])/(df['-DI'] + df['-DI']))
    # Calculate Average Directional Index (ADX)
    df['ADX'] = df['DX'].ewm(span=period,adjust=False).mean()

    return df['ADX']
