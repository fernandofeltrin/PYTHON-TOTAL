from dash import html, dcc
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_prontuarios = dbc.Container([dbc.Row([
    dbc.Row(html.Div([html.Hr(),
                     html.H5('Prontuários')])),
    html.H6('Selecione um paciente:'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else None),
    html.P(id='valor_selecionado'),
    html.P(),
    html.Div(id='saida_prontuario_selecionado'),
    html.P(),
    html.Hr(),
])])

