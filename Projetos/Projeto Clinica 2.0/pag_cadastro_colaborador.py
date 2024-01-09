from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_cadastro_colab = html.Div([dbc.Row([
        dbc.Row(html.Div([html.Hr(),
                         html.H5('Cadastro de Colaborador')])),
        dbc.Row(html.Div([
        dbc.Row([
            dbc.Label('Nome Completo: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='nome_colab', type='text'), width = 10)]),
        html.P(),
        dbc.Row([
            dbc.Label('Nº Telefone: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='telefone_colab', type='text', value=''), width = 2),
            dbc.Label('Especialidade: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='especialidade_colab', type='text', value=''), width = 2),
            dbc.Label('Nº Registro Profissional: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='credencial_colab', type='text', value=''), width = 2)]),
        html.P(),
        html.Hr(),
        dbc.Row([
                dbc.Label('Observações: ', width=2, style={'fontSize': '14px'}),
                dbc.Textarea(id='observacoes_colab', value='')]),
        html.P(),
        dbc.Row([dbc.Col(dbc.Button('Cadastrar', id='botao_cadastrar_colaborador', n_clicks=0), className="d-grid gap-2 col-2 mx-auto")]),
        html.Hr(),
        html.P(),
        html.Div(id = 'saida_formulario_cadastro_colab')])),
        html.P(),
        html.Hr(),
        dbc.Row()])])
