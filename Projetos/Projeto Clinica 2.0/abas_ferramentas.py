from dash import html
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_abas_ferramentas = dbc.Container([
                html.Hr(),
                    dbc.Card([
                        dbc.CardBody(dbc.Tabs(id='abas_ferramentas', active_tab='ferr_anamneses', children=[
                            dbc.Tab(label='Anamneses', tab_id='ferr_anamneses'),
                            dbc.Tab(label='Exercícios', tab_id='ferr_exercicios'),
                            dbc.Tab(label='Fichas de Avaliação', tab_id='ferr_fichas_avaliacao'),
                            dbc.Tab(label='Testes Psicométricos', tab_id='ferr_testes_psicometricos'),
                            dbc.Tab(label='Outros', tab_id='ferr_outros')])),dbc.CardBody(html.Div(id='conteudo_abas_ferramentas'))])]), ''