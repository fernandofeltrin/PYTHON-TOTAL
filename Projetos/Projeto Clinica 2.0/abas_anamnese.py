from dash import html
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_abas_anamnese = dbc.Container([
                html.Hr(),
                    dbc.Card([
                        dbc.CardBody(dbc.Tabs(id='abas_anamnese', active_tab='anamnese_conv_inicial', children=[
                            dbc.Tab(label='Conversa Inicial', tab_id='anamnese_conv_inicial'),
                            dbc.Tab(label='Histórico Clínico', tab_id='anamnese_hist_clinico'),
                            dbc.Tab(label='Exame Psíquico', tab_id='anamnese_exam_psiquico'),
                            dbc.Tab(label='Anotações', tab_id='anamnese_anotacoes'),
                            dbc.Tab(label='Hipótese Diagnóstica', tab_id='anamnese_hipotese_diagnostica')])),dbc.CardBody(html.Div(id='conteudo_abas_anamnese'))])]), ''

