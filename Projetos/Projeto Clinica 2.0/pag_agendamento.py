from dash import html, dcc
import dash_bootstrap_components as dbc
from datetime import datetime as dt

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho',
         7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
horas = list(range(8, 12)) + list(range(14, 18))

layout_agendamento = dbc.Container([
        html.Hr(),
        html.H5('Agendamento'),
        html.P('Selecione um paciente:'),
        html.P(),
        dcc.Dropdown(id='menu_selecao_paciente',
            options=[{'label': label, 'value': value} for value, label in nomes.items()],
            value=list(nomes.keys())[0]),
        html.P(),
        html.Hr(),
        html.P(),
        dbc.Row([
            dbc.Col([dcc.Dropdown(id='ano-dropdown',
            options=[{'label': str(ano), 'value': ano} for ano in range(2022, 2030)], value='2023')]),
            dbc.Col([dcc.Dropdown(id='mes-dropdown',
            options=[{'label': value, 'value': value} for label, value in meses.items()], value='Janeiro')]),
            dbc.Col([dcc.Dropdown(id='dia-dropdown',
            options=[{'label': str(dia), 'value': dia} for dia in range(1, 32)], value=1)]),
            dbc.Col([dcc.Dropdown(id='hora-dropdown',
            options=[{'label': str(hora), 'value': hora} for hora in horas], value=8)])]),
        html.P(),
        html.P(),
        dcc.Dropdown(id='menu_selecao_colaborador',
            options=[{'label': label, 'value': value} for value, label in colaboradores.items()],
            value=list(colaboradores.keys())[0]),
        html.P(),
        dbc.Row([
                dbc.Label('Modalidade: ', width=1, style={'fontSize': '14px'}),
                dbc.Col(dbc.RadioItems(options=[
                    {"label": "Convênio", "value": 'Convênio'},
                    {"label": "Particular", "value": 'Particular'},],
                    id="menu_selecao_convenio", value='Particular', inline=True, style={'fontSize': '14px'}),
                width=10),
                html.Div(id='saida_selecao_convenio', style={'display':'none'})]),
        html.P(),
        dbc.FormFloating([dbc.Input(id = 'obs_agendamento', type="text", value = ''),
                          dbc.Label("Observações")]),
        html.P(),
        dbc.Button("Confirmar", id="botao_confirmar_agendamento", n_clicks=0, color="primary"),
        html.P(),
        html.Div(id='saida_selecao_agendamento'),
        html.P(),
])

