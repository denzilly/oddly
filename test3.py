import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from xpaths import *
from modules.db_logic import *
import pandas as pd
from modules.dashboard_figures import *
import time
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from flask_caching import Cache




external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


connection_m_1 = db_connect("market_DB",local=True)
connection_m_2 = db_connect("market_DB",local=True)

CACHE_CONFIG = {
    # try 'filesystem' if you don't want to setup redis
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': 'localhost'
}
cache = Cache()
cache.init_app(app.server, config=CACHE_CONFIG)




app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown1',
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
    ),

    dcc.Dropdown(
        id='dropdown2',
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
    ),
    html.Div(id='dd-output-container'),
    html.Div(id='dd-output-container2'),
    html.Div(id='recent-update'),
    html.Div(id='update-main'),
    html.Div(id='test'),
    dcc.Graph(id="main_plots"),

    dcc.Store(id="main_df"),
    dcc.Interval(
            id='interval-short',
            interval=2000, # in milliseconds
            n_intervals=0
        ),
       
    dcc.Interval(
            id='interval-long',
            interval=30000, # in milliseconds
            n_intervals=0
        ),
    
    
])



@app.callback(
    Output('main_plots','figure'),
    Output('recent-update','children'),
    Output('update-main','children'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    Input('interval-short', 'n_intervals'),
    Input('update-main','children'),
    Input('main_df', 'data')
)
def update_df(country1, country2, n_intervals,update_status, data):
    #dont run until main is loaded, or while main is updating
    print(n_intervals)

    if n_intervals == 0:
        update_status = "update main"
        return "none","none",update_status

    if n_intervals == 1 or n_intervals %20 == 0:
        
        connection_m_1.reconnect()
        df_main = pd.read_sql("""SELECT * FROM MARKET_DATA WHERE id > 30000 ORDER BY id ASC""", con=connection_m_1)
        js = df_main.to_json()    
        print("updating main")
        update_status = "update_complete"
        fig = gen_lineplot(df_main, country1, country2)
        return fig,df_main['time'].iloc[-1], update_status

    elif update_status != "updating main" and n_intervals != 0:
        connection_m_2.reconnect()
        df_main = pd.read_json(data)
        max_id = df_main['id'].iloc[-1]
        df_new = pd.read_sql(f"""SELECT * FROM MARKET_DATA WHERE id > {max_id} ORDER BY id""", con=connection_m_2)
        df_main = df_main.append(df_new, ignore_index=True)
        update_status = "update complete"
        print("updating small")
        print (df_main.shape)
        fig = gen_lineplot(df_main, country1, country2)
        return fig,df_main['time'].iloc[-1], update_status

    # else:
    #     df_main = pd.read_json(data)
    #     fig = gen_lineplot(df_main, country1, country2)
    #     update_status = "Update complete"
    #     return fig,df_main['time'].iloc[-1], update_status
    


@app.callback(
    Output('dd-output-container', 'children'),
    Output('dd-output-container2', 'children'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value'),
    )
def update_output(country1,country2):
    return 'You have selected "{}"'.format(country1), 'You have selected "{}"'.format(country2)


if __name__ == '__main__':
    app.run_server(debug=True)