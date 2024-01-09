from dash import html
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_abas_materiais = dbc.Container([
                html.Hr(),
                    dbc.Card([
                        dbc.CardBody(dbc.Tabs(id='abas_materiais', active_tab='aba_dsm', children=[
                            dbc.Tab(label='DSM-5', tab_id='materiais_dsm'),
                            dbc.Tab(label='Técnicas de Análise', tab_id='materiais_tec_analise')])),dbc.CardBody(html.Div(id='conteudo_abas_materiais'))])]), ''