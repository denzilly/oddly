import pandas as pd

import time
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from modules.helpers import *

def gen_lineplot(df,country1,country2):


    fig = make_subplots(rows=2, cols=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country1}_OFFER'],
                        mode='lines',
                        line=dict(color='#00cc96')), row=1,col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country1}_BID'],
                        mode='lines',
                        line=dict(color='#ff5454')), row=1,col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country2}_OFFER'],
                        mode='lines',
                        line=dict(color='#00cc96')), row=2,col=1)
    fig.add_trace(go.Scatter(x=df['time'], y=df[f'{country2}_BID'],
                        mode='lines',
                        line=dict(color='#ff5454')), row=2,col=1)
               
    
    fig.update_layout(
    height=750,
    showlegend=False,
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
            ]),
            bgcolor="#ffdd1c",
            font_color="#363535"
        ),
        rangeslider=dict(
            visible=False
        ),
        type="date",
        
    ),
    template='plotly_dark',
    plot_bgcolor= 'rgba(0,0,0,0)',
    paper_bgcolor= 'rgba(0, 0, 0, 0)',
    
    )
    fig.update_xaxes(showgrid=True, gridcolor='#222631', spikedash='dash', row=1,col=1)
    fig.update_yaxes(showgrid=True, gridcolor='#222631', spikedash='dash', row=1,col=1)
    fig.update_xaxes(showgrid=True, gridcolor='#222631', spikedash='dash', row=2,col=1)
    fig.update_yaxes(showgrid=True, gridcolor='#222631', spikedash='dash', row=2,col=1)

    
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
    return fig





def create_dropdown(id):
    return html.Div([
        
                dcc.Dropdown(
            id=id,
            options=[
                {'label': 'ITALY', 'value': 'ITALY'},
                {'label': 'SWITZERLAND', 'value': 'SWITZERLAND'},
                {'label': 'TURKEY', 'value': 'TURKEY'},
                {'label': 'WALES', 'value': 'WALES'},
                {'label': 'BELGIUM', 'value': 'BELGIUM'},
                {'label': 'DENMARK', 'value': 'DENMARK'},
                {'label': 'FINLAND', 'value': 'FINLAND'},
                {'label': 'RUSSIA', 'value': 'RUSSIA'},
                {'label': 'AUSTRIA', 'value': 'AUSTRIA'},
                {'label': 'NETHERLANDS', 'value': 'NETHERLANDS'},
                {'label': 'NORTH_MACEDONIA', 'value': 'NORTH_MACEDONIA'},
                {'label': 'UKRAINE', 'value': 'UKRAINE'},
                {'label': 'CROATIA', 'value': 'CROATIA'},
                {'label': 'CZECH_REPUBLIC', 'value': 'CZECH_REPUBLIC'},
                {'label': 'ENGLAND', 'value': 'ENGLAND'},
                {'label': 'SCOTLAND', 'value': 'SCOTLAND'},
                {'label': 'POLAND', 'value': 'POLAND'},
                {'label': 'SLOVAKIA', 'value': 'SLOVAKIA'},
                {'label': 'SPAIN', 'value': 'SPAIN'},
                {'label': 'SWEDEN', 'value': 'SWEDEN'},
                {'label': 'FRANCE', 'value': 'FRANCE'},
                {'label': 'GERMANY', 'value': 'GERMANY'},
                {'label': 'HUNGARY', 'value': 'HUNGARY'},
                {'label': 'PORTUGAL', 'value': 'PORTUGAL'}
            ],
            value='ITALY'
            )

            
    ],style={'width': '100%', 'display': 'inline-block'})


def draw_main_plots():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(id="main_plots", animate=True)
            ])
        )
    ], style={'margin':'1px'})


def drawText(id):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2(id=id),
                ], style={'textAlign': 'center'}) 
            ])
        ),
    ])