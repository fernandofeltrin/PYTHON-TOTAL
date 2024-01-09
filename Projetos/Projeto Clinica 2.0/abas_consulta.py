from dash import html
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_abas_consulta = dbc.Container([
                html.Hr(),
                    dbc.Card([
                        dbc.CardBody(dbc.Tabs(id='abas_consulta', active_tab='consulta_setting_analitico', children=[
                            dbc.Tab(label='Setting Analítico', tab_id='consulta_setting_analitico'),
                            dbc.Tab(label='Técnicas de Análise', tab_id='consulta_tecnicas_analise'),
                            dbc.Tab(label='Evolução', tab_id='consulta_evolucao'),
                            dbc.Tab(label='Histórico de Consultas', tab_id='consulta_historico_consultas'),
                            dbc.Tab(label='Laudos / Pareceres', tab_id='consulta_laudos_pareceres'),
                            dbc.Tab(label='Hipótese Diagnóstica', tab_id='consulta_hipotese_diagnostica')])),dbc.CardBody(html.Div(id='conteudo_abas_consulta'))])]), ''

