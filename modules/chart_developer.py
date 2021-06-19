import pandas as pd
from db_logic import *
import time
from plotly.subplots import make_subplots
import plotly.graph_objects as go

def gen_lineplot(df,country1,country2):


    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country1}_OFFER'],
                        mode='lines',
                        name='lines'), row=1,col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country1}_BID'],
                        mode='lines',
                        name='lines'), row=1,col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country2}_OFFER'],
                        mode='lines',
                        name='lines'), row=2,col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country2}_BID'],
                        mode='lines',
                        name="lines"), row=2,col=1)
                        
    
    print(df[f'{country1}_OFFER'].iloc[-1])

    fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="minute",
                     stepmode="backward"),
                dict(count=15,
                     label="15m",
                     step="minute",
                     stepmode="backward"),
                dict(count=1,
                     label="1hr",
                     step="hour",
                     stepmode="backward"),
                dict(count=24,
                     label="24h",
                     step="hour",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=False
        ),
        type="date"
    )
)
    
    fig.add_annotation(x=1, y=df[f'{country1}_OFFER'].iloc[-1]*1.2,
                xref='x domain',
                yref='y1',
                text=f"Offer: {df[f'{country1}_OFFER'].iloc[-1]}",
                showarrow=False,
                arrowhead=1,
                bgcolor="#808080",
                bordercolor="#00FF00",
                borderwidth=3,)

    fig.add_annotation(x=1, y=df[f'{country1}_BID'].iloc[-1]*0.7,
                xref='x domain',
                yref='y1',
                text=f"Bid: {df[f'{country1}_BID'].iloc[-1]}",
                showarrow=False,
                arrowhead=1,
                bgcolor="#808080",
                bordercolor="#00FF00",
                borderwidth=3,)


    fig.add_annotation(x=1, y=df[f'{country2}_OFFER'].iloc[-1]*1.2,
                xref='x domain',
                yref='y2',
                text=f"Offer: {df[f'{country2}_OFFER'].iloc[-1]}",
                showarrow=False,
                arrowhead=1,
                bgcolor="#808080",
                bordercolor="#00FF00",
                borderwidth=3,)

    fig.add_annotation(x=1, y=df[f'{country2}_BID'].iloc[-1]*0.7,
                xref='x domain',
                yref='y2',
                text=f"Bid: {df[f'{country2}_BID'].iloc[-1]}",
                showarrow=False,
                arrowhead=1,
                bgcolor="#808080",
                bordercolor="#00FF00",
                borderwidth=3,)




    fig.update_xaxes(matches='x')
    fig.show()
