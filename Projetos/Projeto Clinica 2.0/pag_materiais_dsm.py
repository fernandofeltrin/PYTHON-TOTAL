from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_materiais_dsm5 = html.Div([

    html.Div(id='pdf-content')
])
