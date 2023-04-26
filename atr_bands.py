import pandas as pd
import numpy as np
""" 
## Example 
bar = yfinance or inclusive bar["High"]  bar["Low"] bar["Close"] 
upper_band , lower_band   =   atr_bands( bar , multiplier =1.7 , period = 3   ) 
"""

def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 
     
def  atr_bands( bar , multiplier  , period ):

  close = np.array( bars["Close"] ,dtype=np.float16  )
  # multiplier = 2.0 
  high_low, high_close, low_close  = np.array(bars["High"]-bars["Low"],dtype=np.float16 ) , 
  np.array(abs(bars["High"]-bars["Close"].shift()),dtype=np.float16 ) , 
    np.array(abs(bars["Low"]-bars["Close"].shift() ),dtype=np.float16 )
    
  true_range = np.amax (np.hstack( (high_low, high_close, low_close) ).reshape(-1,3),axis=1 )
  true_range = np.nan_to_num(true_range , nan=0) 
    
  avg_true_range = sma(true_range , period )  # takes average for 14 period  

  upper_band =   close + (multiplier * avg_true_range)
  lower_band =   close - (multiplier * avg_true_range)  

  return  upper_band , lower_band
