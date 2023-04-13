import plotly.graph_objects as go
import plotly.express as px 
from plotly.subplots import make_subplots
""" 
## Example 
bar = yfinance or inclusive bar["High"]  bar["Low"] bar["Close"] 
plot_candles_atr(bar , index=None   )

"""



def plot_candles_atr(bar , index=None):
  fig = make_subplots(rows=2, cols=1)
  fig= go.Figure(data= [go.Candlestick(x=bar.index.values if not index else bar.index.values[index:], open=bar["Open"] if not index else bar["Open"][index:]
      ,high=bar["High"] if not index else bar["High"][index:] , low=bar["Low"] if not index else bar["Low"][index:]  ,close=bar["Close"] if not index else bar["Close"][index:])])

  
  fig.add_scatter( name="upper_band" ,x=bar.index.values  , y=bar['upper_band'], mode='lines' , line=dict(color='yellow', width=1.5))

  fig.add_scatter( name="lower_band" ,x=bars.index.values  , y=bar['lower_band'], mode='lines' , line=dict(color='yellow', width=1.5))


  # fig.add_scatter( name="Average_True_Range" , x=bars.index.values  , y=bars['Average_True_Range'], mode='lines' , line=dict(color='yellow', width=1.5) )
  fig.update_layout(yaxis_tickformat = ".5f") 
  # yaxis="tickformat': 5.f" )                                
                    # {'tickformat': '5.f'})

  
  fig.update_layout(plot_bgcolor='rgb(8, 14, 44)')
  fig.update_xaxes(showline=True, linewidth=2, linecolor='white' , gridcolor='rgb(8, 14, 44)')
  fig.update_yaxes(showline=True, linewidth=2, linecolor='white' , gridcolor='grey')
  # fig.update_layout(title=f'{title}') 
  fig.show()
