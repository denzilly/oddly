import dash
from dash_bootstrap_components._components.CardBody import CardBody
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output
from xpaths import *
from modules.db_logic import *
import pandas as pd
from modules.dashboard_figures import *
from modules.helpers import * 
import time
from dash.exceptions import PreventUpdate
from datetime import datetime
import redis
import pyarrow as pa







#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


connection = db_connect("market_DB",local=False)
r = redis.Redis('localhost', charset="utf-8")
#brain = Brain()


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
app.layout = html.Div([

    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(html.H1("Footie_trader", id="titletext"),
                    width={"size": 3, "order":"first"}),

                # dbc.Col(html.H2("ARMED",id="armed"),
                #     width={"size": 3, "order":"12", "offset" : 2}),

                # dbc.Col(html.Div([
                #     daq.ToggleSwitch(
                #         id='my-toggle-switch',
                #         value=False
                # )]),
                #     width={"size":3,"order":"last", "offset" : 1})
            ])
        ])
    ),

    
    dbc.Card(
        dbc.CardBody([
            #graph panel
            dbc.Row([
                dbc.Col([draw_main_plots()], width=6),

                dbc.Col([
                        html.Div([
                            dbc.Card(
                                dbc.CardBody([
                                    dbc.Row([
                                    
                                        dbc.Col([
                                            html.H3("Country 1:"),
                                            create_dropdown("dropdown1")
                                        ]),
                                        dbc.Col([
                                            html.H3("Country 2:"),
                                            create_dropdown("dropdown2")
                                        ])
                                    ]),
                                    ])),
                            dbc.Card(
                                dbc.CardBody([
                                    dbc.Row([
                                        dbc.Col([
                                            html.Div(id="countrylabel1", className="vert-country"),
                                    
                                        ]),
                                        dbc.Col([
                                            html.Div("3", id="c1-bids",className="orders left"),
                                        ],className="tradecol left"),
                                        dbc.Col([
                                            dbc.Button([html.Div(id="c1-bid-px", className="button bid")], color="danger", className="mr-1"),
                                    
                                        ]),
                                        dbc.Col([
                                            dbc.Button([html.Div(id="c1-offer-px", className="button offer")], color="success", className="mr-1"),
                                        ]),
                                        dbc.Col([
                                            html.Div("6", id="c1-offers",className="orders right"),
                                        ],className="tradecol right"),
                                        dbc.Col([
                                            html.Div("", className="spacer"),
                                        ]),


                                    ], className="traderow", align="center")
                                ], className="tradecardbody"), className="tradecard"),
                                dbc.Card(
                                dbc.CardBody([
                                    html.Div([
                                        dbc.Row([
                                            dbc.Col([
                                                html.Div(id="countrylabel2", className="vert-country"),
                                        
                                            ]),
                                            dbc.Col([
                                                html.Div("5", id="c2-bids",className="orders left"),
                                            ],className="tradecol left"),
                                            dbc.Col([
                                                dbc.Button([html.Div(id="c2-bid-px", className="button bid")], color="danger", className="mr-1"),
                                        
                                            ]),
                                            dbc.Col([
                                                dbc.Button([html.Div(id="c2-offer-px", className="button offer")],  color="success", className="mr-1"),
                                            ]),
                                            dbc.Col([
                                                html.Div("2", id="c2-offers",className="orders right"),
                                            ],className="tradecol right"),
                                            dbc.Col([
                                                html.Div("",className="spacer"),
                                            ]),

                                        ], className="traderow", align="center")
                                    ],className="innertradebox")
                                ], className="tradecardbody"), className="tradecard"),

                                


                        
          
                            ],className="tradebox")


                        ]),
            ]),
            
            dbc.Row([
                dbc.Col([drawText('recent-update')])
                    ]), 
                    ]), color ='dark'
        ),


    
    
    html.Div(id='test'),
    
    
    dcc.Interval(
            id='interval-short',
            interval=2000, # in milliseconds
            n_intervals=0
        ),
       
   
    
    
])

#UPDATE THE MAIN DATAFRAME WITH A FULL SELECT 
@app.callback(
    Output('test','children'),
    Input('interval-short','n_intervals')
    )
def update_df(n_intervals):
    #load the data the first time, and store it in dcc store
    text = 'foo'
    if n_intervals == 0 or n_intervals % 20 ==0:
        connection.reconnect()
        df = pd.read_sql("""SELECT * FROM MARKET_DATA WHERE id > 30000 ORDER BY id ASC""", con=connection)
        print("main DF updated")
        storeInRedis(r,'main_df',df)
    return text

    

@app.callback(
    Output('main_plots','figure'),
    Output('recent-update','children'),
    Output('c1-bid-px','children'),
    Output('c1-offer-px','children'),
    Output('c2-bid-px','children'),
    Output('c2-offer-px','children'),
    Output('countrylabel1','children'),
    Output('countrylabel2','children'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('interval-short', 'n_intervals'),
)
def update_df(country1, country2, n_intervals):
    #print(n_intervals)
    #dont run until main is loaded
    while loadFromRedis(r,'main_df').shape == "(0,1)":
        time.sleep(1)
        print("no data yet")

    else:
        connection.reconnect()
        df_main = loadFromRedis(r,'main_df')
        max_id = df_main['id'].iloc[-1]
        #df_new = pd.read_sql(f"""SELECT * FROM MARKET_DATA WHERE id > {max_id} ORDER BY id""", con=connection)
        #df_main = df_main.append(df_new, ignore_index=True)
        fig = gen_lineplot(df_main, country1, country2)

        c1_bid_px = price_string(df_main, country1, "bid")
        c1_offer_px = price_string(df_main, country1, "offer")
        c2_bid_px = price_string(df_main, country2, "bid")
        c2_offer_px = price_string(df_main, country2, "offer")
        countrylabel1 = country_code(country1)
        countrylabel2 = country_code(country2)
        print("updating small")


        recent_update = f"""Last update: {datetime.strptime(df_main['time'].iloc[-1], '%Y-%m-%d %H:%M:%S.%f').strftime("%b %d %Y %H:%M:%S")}"""
        return fig, recent_update, c1_bid_px, c1_offer_px, c2_bid_px, c2_offer_px, countrylabel1, countrylabel2
    



if __name__ == '__main__':
    app.run_server(debug=True)