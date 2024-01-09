from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px

from app import df

layout_dashboard = dbc.Container([
                html.Hr(),
                html.H5('Dashboard'),
                html.P(),
                dbc.Row([]),
                html.P(),
                dbc.Row([dcc.Graph(id='distribuicao-semana')]),
                html.P(),
                dbc.Row([
                    dbc.Col([dcc.Graph(id='total-consultas')]),
                    dbc.Col([dcc.Graph(id='consultas-por-convenio')]),]),
                html.P()
                ])

