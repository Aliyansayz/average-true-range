
def  atr_bands( bar , multiplier ):

  close = np.array( bars["Close"] ,dtype=np.float16  )
  # multiplier = 2.0 
  high_low, high_close, low_close  = np.array(bars["High"]-bars["Low"],dtype=np.float16 ) , 
  np.array(abs(bars["High"]-bars["Close"].shift()),dtype=np.float16 ) , 
    np.array(abs(bars["Low"]-bars["Close"].shift() ),dtype=np.float16 )
    
  true_range = np.amax (np.hstack( (high_low, high_close, low_close) ).reshape(-1,3),axis=1 )
  avg_true_range = sma(true_range , window_size=14)  # takes average for 14 period  

  upper_band =   close + (multiplier * avg_true_range)
  lower_band =   close - (multiplier * avg_true_range)  

  return  upper_band , lower_band