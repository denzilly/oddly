import dash
import dash_daq as daq
import dash_html_components as html
from modules.dashboard_figures import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#connect to the database
connection_m = db_connect("market_DB")
cursor_m = connection.cursor()
connection_b = db_connect("odds_DB")
cursor_b = connection.cursor()



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div(children=[
    html.Div(
    
    dbc.Row(
        dbc.Col(html.H3(children="betmkt2")),
    ),
    
    dbc.Row(
    dcc.Graph(id="group_plots"),
    
    ),
    
    
    

    dcc.Interval(
            id='interval-short',
            interval=5000, # in milliseconds
            n_intervals=0
        ),
    dcc.Store(id="main_df")
    )
])


@app.callback(Output('main_df', 'data'), Input('interval-short', 'n_intervals'))
def refresh_data(value):
     # some expensive clean data step
     cleaned_df = your_expensive_clean_or_compute_step(value)

     # more generally, this line would be
     # json.dumps(cleaned_df)
     return df


@app.callback(
    Output("group_plots", "figure"), 
    [Input("main_df", "data")])
def update_bar_chart(day):
    fig = gen_lineplot()
    return fig









if __name__ == '__main__':
    app.run_server(debug=True)