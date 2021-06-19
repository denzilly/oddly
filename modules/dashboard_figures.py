import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import random
import pandas as pd
import dash_daq as daq
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go





def gen_lineplot(conn):

    #get all data since last 
