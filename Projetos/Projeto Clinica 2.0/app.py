# -*- coding: utf-8 -*-

import os
import dash
import pandas as pd
import base64
import sqlite3
import plotly.express as px
import dash_bootstrap_components as dbc
from datetime import datetime
from dash import html, dcc
from dash.dependencies import Input, Output, State

from gera_base import gera_base, carrega_bases
from nav_bar import layout_nav_bar
from dados_aux import modal_ids
from funcoes_aux import converte_imagem, gera_modal_dinamicamente

global df
global df_agenda

gera_base()
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

app = dash.Dash(__name__,
                title = 'Sistema Clínica 2.0',
                external_stylesheets = [dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions = True)

def serve_layout():
    layout = dbc.Container(
    [dcc.Location(id='url', pathname='/dashboard'),
     dcc.Store(id='store_df', data=df.to_dict()),
     html.Div(id='retorno_store', style={"display": "none"}),
     dcc.Interval(id='interval-component', interval=60 * 1000, n_intervals=0),
     dbc.Row([dbc.Col([layout_nav_bar], width=2),
              dbc.Col(html.Div(id="page-content"), width=10)]),
     ] + [gera_modal_dinamicamente(modal_id) for modal_id in modal_ids], fluid=True)
    return layout

app.layout = serve_layout

# RENDERIZA PÁGINA
@app.callback(
     [Output('page-content', 'children'),
      Output('palavra_chave_input', 'value')],
     [Input('url', 'pathname'),
      Input('palavra_chave_input', 'n_submit')],
     [State('palavra_chave_input', 'value')])
def renderiza_conteudo(pathname, n_submit, palavra_chave):
    if n_submit is not None:
        from dados_aux import palavras_chave_mec_busca
        for chave, valor in palavras_chave_mec_busca.items():
            if palavra_chave.lower() in valor:
                if chave == 'agenda':
                    return layout_agendamento, ''
                elif chave == 'cadastro':
                    return layout_cadastro, ''
                elif chave == 'anamnese':
                    from abas_anamnese import layout_abas_anamnese
                    return layout_abas_anamnese, ''
                elif chave == 'ferramentas':
                    from abas_ferramentas import layout_abas_ferramentas
                    return layout_abas_ferramentas, ''
                elif chave == 'materiais':
                    from abas_materiais import layout_abas_materiais
                    return layout_abas_materiais, ''
    if pathname:
        if pathname == '/dashboard':
            from dashboards import layout_dashboard
            return layout_dashboard, ''
        elif pathname == '/agenda':
            from pag_agendamento import layout_agendamento
            return layout_agendamento, ''
        elif pathname == '/cadastro':
            from pag_cadastro import layout_cadastro
            return layout_cadastro, ''
        elif pathname == '/anamnese':
            from abas_anamnese import layout_abas_anamnese
            return layout_abas_anamnese, ''
        elif pathname == '/consulta':
            from abas_consulta import layout_abas_consulta
            return layout_abas_consulta, ''
        elif pathname == '/documentos':
            from abas_documentos import layout_abas_documentos
            return layout_abas_documentos, ''
        elif pathname == '/ferramentas':
            from abas_ferramentas import layout_abas_ferramentas
            return layout_abas_ferramentas, ''
        elif pathname == '/materiais':
            from abas_materiais import layout_abas_materiais
            return layout_abas_materiais, ''
        elif pathname == '/prontuarios':
            from pag_prontuarios import layout_prontuarios
            return layout_prontuarios, ''
        elif pathname == '/admin':
            from pag_cadastro_colaborador import layout_cadastro_colab
            return layout_cadastro_colab, ''

# Callback para atualizar o conteúdo do dcc.Store
@app.callback(
    Output('store_df', 'data'),
    Output('retorno_store', 'children'),
    Input('interval-component', 'n_intervals'))
def update_store(n_intervals):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    df_dict = df.to_dict('records')
    df_agenda_dict = df_agenda.to_dict('records')
    return {'df': df_dict, 'df_agenda': df_agenda_dict}, None

# Callbacks para atualizar dinamicamente os gráficos
@app.callback(
    Output('total-consultas', 'figure'),
    Output('consultas-por-convenio', 'figure'),
    Output('distribuicao-semana', 'figure'),
    Input('total-consultas', 'value'))
def atualiza_graficos(_):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    contagem_consultas = df_agenda.groupby(['Nome',
                                            'Dia da Semana']).size().reset_index(name='Número de Consultas')
    fig_total = px.bar(contagem_consultas,
                       x='Nome',
                       y='Número de Consultas',
                       color='Dia da Semana',
                       title='Número de Consultas por Paciente e Dia da Semana',
                       labels={'Número de Consultas': 'Número de Consultas por Dia'})
    consultas_por_convenio = df_agenda['Convênio'].value_counts()
    fig_convenio = px.pie(consultas_por_convenio,
                          names=consultas_por_convenio.index,
                          title='Consultas por Convênio')
    fig_semana = px.bar(contagem_consultas,
                        x='Dia da Semana',
                        y='Número de Consultas',
                        color='Nome',
                        title='Distribuição de Consultas por Paciente e Dia da Semana',
                        labels={'Número de Consultas': 'Número de Consultas por Dia'},
                        category_orders={'Dia da Semana': ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                                                           'Quinta-feira', 'Sexta-feira', 'Sábado']})
    return fig_total, fig_convenio, fig_semana

# MODAIS ANAMNESE
@app.callback(
    [Output("modal1", "is_open"),
     Output("modal1-content", "children"),
     Output("modal_anamnese_geral", "n_clicks"),
     Output('modal_anamnese_infantil', 'n_clicks'),
     Output('modal_anamnese_autismo', 'n_clicks'),
     Output('modal_anamnese_cirurgia_bariatrica', 'n_clicks'),
     Output('modal_anamnese_compulsao_alimentar', 'n_clicks'),
     Output('modal_anamnese_psicomotricidade', 'n_clicks')],
    [Input("modal_anamnese_geral", "n_clicks"),
     Input('modal_anamnese_infantil', 'n_clicks'),
     Input('modal_anamnese_autismo', 'n_clicks'),
     Input('modal_anamnese_cirurgia_bariatrica', 'n_clicks'),
     Input('modal_anamnese_compulsao_alimentar', 'n_clicks'),
     Input('modal_anamnese_psicomotricidade', 'n_clicks')],
    [State("modal1", "is_open")],
    prevent_initial_call=True)
def renderiza_modal(btn_m_anamnese, btn_m_anamnese_inf, btn_m_anamnese_aut, btn_m_anamnese_c_bar,
                    btn_m_anamnese_comp_a, btn_m_anamnese_psicomot, is_open):
    if btn_m_anamnese > 0:
        from pag_documentos import layout_documentos_anamnese_geral
        return not is_open, layout_documentos_anamnese_geral, 0, 0, 0, 0, 0, 0
    elif btn_m_anamnese_inf > 0:
        from pag_documentos import layout_documentos_anamnese_infantil
        return not is_open, layout_documentos_anamnese_infantil, 0, 0, 0, 0, 0, 0
    elif btn_m_anamnese_aut > 0:
        from pag_documentos import layout_documentos_anamnese_autismo
        return not is_open, layout_documentos_anamnese_autismo, 0, 0, 0, 0, 0, 0
    elif btn_m_anamnese_c_bar > 0:
        from pag_documentos import layout_documentos_anamnese_c_bariatrica
        return not is_open, layout_documentos_anamnese_c_bariatrica, 0, 0, 0, 0, 0, 0
    elif btn_m_anamnese_comp_a > 0:
        from pag_documentos import layout_documentos_anamnese_comp_a
        return not is_open, layout_documentos_anamnese_comp_a, 0, 0, 0, 0, 0, 0
    elif btn_m_anamnese_psicomot > 0:
        from pag_documentos import layout_documentos_anamnese_psicomotricidade
        return not is_open, layout_documentos_anamnese_psicomotricidade, 0, 0, 0, 0, 0, 0
    return is_open, None, 0, 0, 0, 0, 0, 0


# MODAIS ATESTADOS
@app.callback(
    [Output("modal2", "is_open"),
     Output("modal2-content", "children"),
     Output("modal_at_psicologico", "n_clicks"),
     Output("modal_at_sanidade_mental", "n_clicks"),
     Output("modal_at_boa_conduta", "n_clicks"),
     Output("modal_at_aptidao", "n_clicks")],
    [Input("modal_at_psicologico", "n_clicks"),
     Input("modal_at_sanidade_mental", "n_clicks"),
     Input("modal_at_boa_conduta", "n_clicks"),
     Input("modal_at_aptidao", "n_clicks")],
    [State("modal2", "is_open")], prevent_initial_call=True)
def renderiza_modal(btn_m_at_psico, btn_m_at_san, btn_m_at_b_cond, btn_m_at_apti, is_open):
    if btn_m_at_psico > 0:
        from pag_documentos import layout_documentos_anamnese_geral
        return not is_open, layout_documentos_anamnese_geral, 0, 0, 0, 0
    elif btn_m_at_san > 0:
        return not is_open, 'Atestado Psicológico de Sanidade Mental', 0, 0, 0, 0
    elif btn_m_at_b_cond > 0:
        return not is_open, 'Atestado de Boa Conduta', 0, 0, 0, 0
    elif btn_m_at_apti > 0:
        return not is_open, 'Atestado de Aptidão Específica', 0, 0, 0, 0
    return is_open, None, 0, 0, 0, 0

# MODAIS CARTAS / TERMOS
@app.callback(
    [Output("modal3", "is_open"),
     Output("modal3-content", "children"),
     Output("modal_carta_pedido_emprego", "n_clicks"),
     Output("modal_carta_recomendacao_geral", "n_clicks"),
     Output("modal_carta_solicitacao_curadoria", "n_clicks")],
    [Input("modal_carta_pedido_emprego", "n_clicks"),
     Input("modal_carta_recomendacao_geral", "n_clicks"),
     Input("modal_carta_solicitacao_curadoria", "n_clicks")],
    [State("modal3", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_c_p_emprego, m_c_rec_geral, m_c_sol_curadoria, is_open):
    if m_c_p_emprego > 0:
        return not is_open, 'Carta de Pedido de Emprego', 0, 0, 0
    elif m_c_rec_geral > 0:
        return not is_open, 'Carta de Recomendação Geral', 0, 0, 0
    elif m_c_sol_curadoria > 0:
        return not is_open, 'Carta de Solicitação de Curadoria', 0, 0, 0
    return is_open, None, 0, 0, 0

# MODAIS CONTRATOS
@app.callback(
    [Output("modal4", "is_open"),
     Output("modal4-content", "children"),
     Output("modal_contrato_psicoterapia_individual", "n_clicks"),
     Output("modal_contrato_psicoterapia_grupo", "n_clicks"),
     Output("modal_contrato_psicoterapia_online", "n_clicks"),
     Output("modal_contrato_psicoterapia_esporadica", "n_clicks"),
     Output("modal_contrato_prestacao_servico_consultoria", "n_clicks")],
    [Input("modal_contrato_psicoterapia_individual", "n_clicks"),
     Input("modal_contrato_psicoterapia_grupo", "n_clicks"),
     Input("modal_contrato_psicoterapia_online", "n_clicks"),
     Input("modal_contrato_psicoterapia_esporadica", "n_clicks"),
     Input("modal_contrato_prestacao_servico_consultoria", "n_clicks")],
    [State("modal4", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_c_psico_in, m_c_psico_gr, m_c_psico_on, m_c_psico_esp, m_c_consultoria, is_open):
    if m_c_psico_in > 0:
        return not is_open, 'Contrato de Psicoterapia Individual', 0, 0, 0, 0, 0 
    elif m_c_psico_gr > 0:
        return not is_open, 'Contrato de Psicoterapia Familiar / em Grupo', 0, 0, 0, 0, 0
    elif m_c_psico_on > 0:
        from pag_documentos import layout_documentos_contrato_psicoterapia_online
        return not is_open, layout_documentos_contrato_psicoterapia_online, 0, 0, 0, 0, 0
    elif m_c_psico_esp > 0:
        return not is_open, 'Contrato de Consulta Terapêutica Esporádica / Geral', 0, 0, 0, 0, 0
    elif m_c_consultoria > 0:
        return not is_open, 'Contrato de Prestação de Serviços de Consultoria', 0, 0, 0, 0, 0
    return is_open, None, 0, 0, 0, 0, 0

# MODAIS DECLARACOES
@app.callback(
    [Output("modal5", "is_open"),
     Output("modal5-content", "children"),
     Output("modal_declaracao_acompanhamento", "n_clicks"),
     Output("modal_declaracao_tratamento", "n_clicks")],
    [Input("modal_declaracao_acompanhamento", "n_clicks"),
     Input("modal_declaracao_tratamento", "n_clicks")],
    [State("modal5", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_dec_acomp, m_dec_trat, is_open):
    if m_dec_acomp > 0:
        return not is_open, 'Declaração de Acompanhamento Psicológico', 0, 0
    elif m_dec_trat > 0:
        return not is_open, 'Declaração de Tratamento Psicoterápico', 0, 0
    return is_open, None, 0, 0

# MODAIS ENCAMINHAMENTOS
@app.callback(
    [Output("modal6", "is_open"),
     Output("modal6-content", "children"),
     Output("modal_encaminhamento_outro_profissional", "n_clicks"),],
    [Input("modal_encaminhamento_outro_profissional", "n_clicks"),],
    [State("modal6", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_enc_outro, is_open):
    if m_enc_outro > 0:
        return not is_open, 'Encaminhamento Para Outro Profissional da Saúde', 0
    return is_open, None, 0

# MODAIS FICHAS DE AVALIACAO
@app.callback(
    [Output("modal7", "is_open"),
     Output("modal7-content", "children"),
     Output("modal_ficha_avaliacao_psicologica_geral", "n_clicks"),
     Output("modal_ficha_avaliacao_risco_suicidio", "n_clicks")],
    [Input("modal_ficha_avaliacao_psicologica_geral", "n_clicks"),
     Input("modal_ficha_avaliacao_risco_suicidio", "n_clicks")],
    [State("modal7", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_f_av_psico, m_f_av_suicidio, is_open):
    if m_f_av_psico > 0:
        return not is_open, 'Ficha de Avaliação Psicológica Geral', 0, 0
    elif m_f_av_suicidio > 0:
        from pag_documentos import layout_ficha_av_risco_suicidio
        return not is_open, layout_ficha_av_risco_suicidio, 0, 0
    return is_open, None, 0, 0

# MODAIS FICHAS DE EVOLUCAO
@app.callback(
    [Output("modal8", "is_open"),
     Output("modal8-content", "children"),
     Output("modal_ficha_evolucao_geral", "n_clicks"),],
    [Input("modal_ficha_evolucao_geral", "n_clicks"),],
    [State("modal8", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_f_evolucao, is_open):
    if m_f_evolucao > 0:
        return not is_open, 'Ficha de Acompanhamento / Evolução Geral', 0
    return is_open, None, 0

# MODAIS LAUDOS / PARECERES
@app.callback(
    [Output("modal9", "is_open"),
     Output("modal9-content", "children"),
     Output("modal_laudo_psicologico_geral", "n_clicks"),
     Output("modal_parecer_saude_mental", "n_clicks")],
    [Input("modal_laudo_psicologico_geral", "n_clicks"),
     Input("modal_parecer_saude_mental", "n_clicks")],
    [State("modal9", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_l_psico, m_p_saude_mental, is_open):
    if m_l_psico > 0:
        return not is_open, 'Laudo Psicológico Geral', 0, 0
    elif m_p_saude_mental > 0:
        return not is_open, 'Parecer de Saúde Mental Parcial', 0, 0
    return is_open, None, 0, 0

# MODAIS PRESCRICOES
@app.callback(
    [Output("modal10", "is_open"),
     Output("modal10-content", "children"),
     Output("modal_receituario_geral_medicacao", "n_clicks"),],
    [Input("modal_receituario_geral_medicacao", "n_clicks"),],
    [State("modal10", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_receituario, is_open):
    if m_receituario > 0:
        return not is_open, 'Receituário Geral Para Medicação', 0
    return is_open, None, 0

# MODAIS RECIBOS
@app.callback(
    [Output("modal11", "is_open"),
     Output("modal11-content", "children"),
     Output("modal_recibo_consulta_unitaria", "n_clicks"),
     Output("modal_recibo_pacote_tratamento", "n_clicks"),
     Output("modal_recibo_aquisicao_servico_adicional", "n_clicks")],
    [Input("modal_recibo_consulta_unitaria", "n_clicks"),
     Input("modal_recibo_pacote_tratamento", "n_clicks"),
     Input("modal_recibo_aquisicao_servico_adicional", "n_clicks")],
    [State("modal11", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_rec_cons, m_rec_pac_cons, m_rec_serv_adicional, is_open):
    if m_rec_cons > 0:
        return not is_open, 'Recibo de Pagamento de Consulta / Sessão Unitária', 0, 0, 0
    elif m_rec_pac_cons > 0:
        return not is_open, 'Recibo de Pagamento de Pacote de Tratamento', 0, 0, 0
    elif m_rec_serv_adicional > 0:
        return not is_open, 'Recibo de Pagamento de Aquisição de Serviço Adicional', 0, 0, 0
    return is_open, None, 0, 0, 0

# MODAIS ROTEIROS
@app.callback(
    [Output("modal12", "is_open"),
     Output("modal12-content", "children"),
     Output("modal_roteiro_hipnoterapia_ansiedade", "n_clicks"),
     Output("modal_roteiro_hipnoterapia_luto", "n_clicks")],
    [Input("modal_roteiro_hipnoterapia_ansiedade", "n_clicks"),
     Input("modal_roteiro_hipnoterapia_luto", "n_clicks")],
    [State("modal12", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_rot_hip_ans, m_rot_hip_luto, is_open):
    if m_rot_hip_ans > 0:
        return not is_open, 'Laudo Psicológico Geral', 0, 0
    elif m_rot_hip_luto > 0:
        return not is_open, 'Parecer de Saúde Mental Parcial', 0, 0
    return is_open, None, 0, 0

# MODAIS TESTES PSICOMETRICOS
@app.callback(
    [Output("modal13", "is_open"),
     Output("modal13-content", "children"),
     Output("modal_teste_psicometrico_", "n_clicks"),],
    [Input("modal_teste_psicometrico_", "n_clicks"),],
    [State("modal13", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_teste_psi_1, is_open):
    if m_teste_psi_1 > 0:
        return not is_open, 'Teste', 0
    return is_open, None, 0

# MODAIS OUTROS
@app.callback(
    [Output("modal14", "is_open"),
     Output("modal14-content", "children"),
     Output("modal_outro_01", "n_clicks"),],
    [Input("modal_outro_01", "n_clicks"),],
    [State("modal14", "is_open")], prevent_initial_call=True)
def renderiza_modal(m_outro_01, is_open):
    if m_outro_01 > 0:
        return not is_open, 'Teste', 0
    return is_open, None, 0


# ABAS PAGINA ANAMNESE
@app.callback(
    Output('conteudo_abas_anamnese', 'children'),
    [Input('abas_anamnese', 'active_tab')])
def render_content(active_tab):
    if active_tab == 'anamnese_conv_inicial':
        from pag_anamnese import layout_anamnese_conv_inicial
        return layout_anamnese_conv_inicial
    elif active_tab == 'anamnese_hist_clinico':
        from pag_anamnese import layout_historico_clinico
        return layout_historico_clinico
    elif active_tab == 'anamnese_exam_psiquico':
        from pag_anamnese import layout_exame_psiquico
        return layout_exame_psiquico
    elif active_tab == 'anamnese_anotacoes':
        from pag_anamnese import layout_anotacoes_anamnese
        return layout_anotacoes_anamnese
    elif active_tab == 'anamnese_hipotese_diagnostica':
        from pag_anamnese import layout_hipotese_diagnostica
        return layout_hipotese_diagnostica


# ABAS PAGINA CONSULTA
@app.callback(
    Output('conteudo_abas_consulta', 'children'),
    [Input('abas_consulta', 'active_tab')])
def render_content(active_tab):
    if active_tab == 'consulta_setting_analitico':
        from pag_consulta import layout_consulta_setting_analitico
        return layout_consulta_setting_analitico
    elif active_tab == 'consulta_tecnicas_analise':
        from pag_consulta import layout_tec_analise_respostas
        return layout_tec_analise_respostas
    elif active_tab == 'consulta_evolucao':
        from pag_consulta import layout_consulta_evolucao
        return layout_consulta_evolucao
    elif active_tab == 'consulta_historico_consultas':
        from pag_consulta import layout_consulta_historico_consultas
        return layout_consulta_historico_consultas
    elif active_tab == 'consulta_laudos_pareceres':
        from pag_consulta import layout_consulta_laudos_pareceres
        return layout_consulta_laudos_pareceres
    elif active_tab == 'consulta_hipotese_diagnostica':
        from pag_consulta import layout_consulta_hipotese_diagnostica
        return layout_consulta_hipotese_diagnostica


# ABAS PAGINA DOCUMENTOS
@app.callback(
    Output('conteudo_abas_documentos', 'children'),
    [Input('abas_documentos', 'active_tab')])
def render_content(active_tab):
    if active_tab == 'modelos_anamneses':
        from pag_documentos import layout_documentos_anamnese_geral 
        from abas_documentos import aba_anamneses
        return aba_anamneses
    elif active_tab == 'modelos_atestados':
        from abas_documentos import aba_atestados
        return aba_atestados
    elif active_tab == 'modelos_cartas_termos':
        from abas_documentos import aba_cartas_termos
        return aba_cartas_termos
    elif active_tab == 'modelos_contratos':
        from abas_documentos import aba_contratos
        return aba_contratos
    elif active_tab == 'modelos_declaracoes':
        from abas_documentos import aba_declaracoes
        return aba_declaracoes
    elif active_tab == 'modelos_encaminhamentos':
        from abas_documentos import aba_encaminhamentos
        return aba_encaminhamentos
    elif active_tab == 'modelos_fichas_avaliacao':
        from abas_documentos import aba_fichas_avaliacao
        return aba_fichas_avaliacao
    elif active_tab == 'modelos_fichas_evolucao':
        from abas_documentos import aba_fichas_evolucao
        return aba_fichas_evolucao
    elif active_tab == 'modelos_laudos_pareceres':
        from abas_documentos import aba_laudos_pareceres
        return aba_laudos_pareceres
    elif active_tab == 'modelos_prescricoes':
        from abas_documentos import aba_prescricoes
        return aba_prescricoes
    elif active_tab == 'modelos_recibos':
        from abas_documentos import aba_recibos
        return aba_recibos
    elif active_tab == 'modelos_roteiros':
        from abas_documentos import aba_roteiros
        return aba_roteiros
    elif active_tab == 'modelos_testes_psicometricos':
        from abas_documentos import aba_testes_psicometricos
        return aba_testes_psicometricos
    elif active_tab == 'modelos_outros':
        from abas_documentos import aba_outros
        return aba_outros


# ABAS PAGINA MATERIAIS
@app.callback(
    Output('conteudo_abas_materiais', 'children'),
    [Input('abas_materiais', 'active_tab')])
def render_content(active_tab):
    if active_tab == 'materiais_dsm':
        pass


# AGENDAMENTO
@app.callback(
    [Output('dia-dropdown', 'options'),
     Output('saida_selecao_agendamento', 'children')],
    [Input('menu_selecao_paciente', 'value'),
     Input('menu_selecao_colaborador', 'value'),
     Input('mes-dropdown', 'value'),
     Input('ano-dropdown', 'value'),
     Input('dia-dropdown', 'value'),
     Input('hora-dropdown', 'value'),
     Input('menu_selecao_convenio', 'value'),
     Input('obs_agendamento', 'value'),
     Input('botao_confirmar_agendamento', 'n_clicks')],
    [State('menu_selecao_paciente', 'options'),
     State('menu_selecao_colaborador', 'options')])
def agendamento(paciente_selecionado, colaborador_selecionado, mes, ano, dia, hora, convenio, obs, n_clicks, lista_pacientes, lista_colaboradores):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    from funcoes_aux import valida_mes_dia, obter_dia_da_semana
    convenio_ = 'Particular' if convenio == 'Particular' else 'Convênio'
    mes_dia_validados = valida_mes_dia(mes, dia)
    dia_semana = obter_dia_da_semana(int(ano), mes, int(dia))
    if paciente_selecionado and colaborador_selecionado:
        nome_pac_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado), 'Nenhum paciente selecionado')
        nome_colab_selecionado = next((i['label'] for i in lista_colaboradores if i['value'] == colaborador_selecionado), 'Nenhum colaborador selecionado')
        if nome_pac_selecionado and n_clicks:
            agendamento_final = f'{nome_pac_selecionado}, {dia_semana} dia {dia} de {mes} de {ano} às {hora}h com {nome_colab_selecionado}. \nConvênio: {convenio_}, \nObs: {obs}.'
            try:
                conexao = sqlite3.connect('base.db')
                cursor = conexao.cursor()
                cursor.execute("SELECT [Histórico de Consultas] FROM Agenda WHERE Nome=?", (nome_pac_selecionado,))
                hist = cursor.fetchone()
                registros_anteriores = hist[0] if hist else ''
                novo_registro = f'{agendamento_final},'
                registros_atualizados = f'{registros_anteriores} {novo_registro}'
                cursor.execute("SELECT [Número de Consultas] FROM Agenda WHERE Nome=?", (nome_pac_selecionado,))
                num = cursor.fetchone()
                num_consultas_atualizado = num[0] + 1 if num and num[0] is not None else 1
                cursor.execute("INSERT INTO Agenda (Nome, Ano, Mês, 'Dia do Mês', 'Dia da Semana', 'Horário', 'Agendamento Observações', Convênio, Profissional, 'Histórico de Consultas', 'Número de Consultas') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nome_pac_selecionado, ano, mes, dia, dia_semana, hora, obs, convenio_, nome_colab_selecionado, registros_atualizados, num_consultas_atualizado))
                conexao.commit()
                conexao.close()
                df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
                return mes_dia_validados, [dbc.Alert(html.Small(f'Consulta agendada para {agendamento_final}'))]
            except Exception as e:
                print(f'Erro ao atualizar a base de dados: {str(e)}')
            return mes_dia_validados, ''
    return mes_dia_validados, '' 


# MENU DE SELEÇÃO DE PACIENTE
@app.callback(
    [Output('paciente_selecionado', 'children')],
    Input('menu_selecao_paciente', 'value'),
    Input('interval-component', 'n_intervals'))
def seleciona_paciente_agendamento(valor_selecionado, n_intervals):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Nome FROM Pacientes')
    nomes = [row[0] for row in cursor.fetchall()]
    conn.close()
    options = [{'label': nome, 'value': nome} for nome in nomes]
    if valor_selecionado:
        return html.Small(f'Realizando agendamento para: {valor_selecionado}')
    return html.Small('Nenhum paciente selecionado')

# MENU DE SELEÇÃO DE COLABORADOR
@app.callback(
    [Output('colaborador_selecionado', 'children')],
    Input('menu_selecao_colaborador', 'value'),
    Input('interval-component', 'n_intervals'))
def seleciona_paciente_agendamento(valor_selecionado, n_intervals):
    conn = sqlite3.connect('colaboradores.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Nome FROM Colaboradores')
    colaboradores = [row[0] for row in cursor.fetchall()]
    conn.close()
    options = [{'label': nome, 'value': nome} for nome in colaboradores]
    if valor_selecionado:
        return html.Small(f'Colaborador: {valor_selecionado}')
    return html.Small('Nenhum colaborador selecionado')


# ANAMNESE CONVERSA INICIAL
@app.callback(
    [Output('saida_formulario_atendimento', 'children')],
    [Input('menu_selecao_paciente', 'value'),
     Input('queixa_principal', 'value'),
     Input('queixa_secundaria', 'value'),
     Input('sintomas', 'value'),
     Input('comorbidades', 'value'),
     Input('obj_terapeuticos', 'value'),
     Input('botao_salvar_atendimento', 'n_clicks'),
     Input('botao_apagar_atendimento', 'n_clicks')],
    State('menu_selecao_paciente', 'options'))
def anamnese_pt1(paciente_selecionado, q_principal, q_secundaria, sintomas, comorbidades,
                obj_terapeuticos, s_n_clicks, a_n_clicks, lista_pacientes):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    if paciente_selecionado:
        nome_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado), 'Nenhum paciente selecionado')
        if nome_selecionado and s_n_clicks:
            try:
                _ = ""
                conexao1 = sqlite3.connect('base.db')
                cursor = conexao1.cursor()
                cursor.execute("SELECT [Queixa Principal] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                queixa_prin_ant = result[0] if result else _
                queixa_prin_nova = f'{q_principal}'
                queixa_prin_att = f'{queixa_prin_ant}, {queixa_prin_nova}'
                cursor.execute("SELECT [Queixa Secundária] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                queixa_sec_ant = result[0] if result else _
                queixa_sec_nova = f'{q_secundaria}'
                queixa_sec_att = f'{queixa_sec_ant}, {queixa_sec_nova}'
                cursor.execute("SELECT [Sintomas] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                sintomas_ant = result[0] if result else _
                sintomas_nova = f'{sintomas}'
                sintomas_att = f'{sintomas_ant}, {sintomas_nova}'
                cursor.execute("SELECT [Comorbidades] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                comorbidades_ant = result[0] if result else _
                comorbidades_nova = f'{comorbidades}'
                comorbidades_att = f'{comorbidades_ant}, {comorbidades_nova}'
                cursor.execute("SELECT [Objetivos Terapêuticos] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                obj_terap_ant = result[0] if result else _
                obj_terap_nova = f'{obj_terapeuticos}'
                obj_terap_att = f'{obj_terap_ant}, {obj_terap_nova}'
                cursor.execute("UPDATE Consulta SET 'Queixa Principal'=?, 'Queixa Secundária'=?, 'Sintomas'=?, 'Comorbidades'=?, 'Objetivos Terapêuticos'=? WHERE Nome=?",
                                (queixa_prin_att, queixa_sec_att, sintomas_att, comorbidades_att, obj_terap_att, nome_selecionado))
                conexao1.commit()
                conexao1.close()
                return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'))]
            except Exception as e:
                print(f'Erro ao atualizar a base de dados: {str(e)}')
        if nome_selecionado and a_n_clicks:
            _ = ""
            conexao2 = sqlite3.connect('base.db')
            cursor = conexao2.cursor()
            cursor.execute("UPDATE Consulta SET 'Queixa Principal' = ?, 'Queixa Secundária' = ?, 'Sintomas' = ? WHERE Nome=?",
                           (_, _, _, nome_selecionado))
            conexao2.commit()
            conexao2.close()
            return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'), color="danger")]
        return ['']

# ANAMNESE HISTORICO CLÍNICO
@app.callback(
    [Output('saida_formulario_historico', 'children')],
    [Input('menu_selecao_paciente', 'value'),
     Input('inicio_patologia', 'value'),
     Input('frequencia_patologia', 'value'),
     Input('intensidade_patologia', 'value'),
     Input('tratamentos_anteriores', 'value'),
     Input('uso_medicamentos', 'value'),
     Input('historico_infancia', 'value'),
     Input('historico_rotina', 'value'),
     Input('historico_alimentar', 'value'),
     Input('historico_sono', 'value'),
     Input('historico_vicios', 'value'),
     Input('historico_cirurgias', 'value'),
     Input('historico_hobbies', 'value'),
     Input('historico_trabalho', 'value'),
     Input('historico_pais', 'value'),
     Input('historico_irmaos', 'value'),
     Input('historico_conjuge', 'value'),
     Input('historico_filhos', 'value'),
     Input('historico_lar', 'value'),
     Input('historico_transtornos_familia', 'value'),
     Input('botao_salvar_historico', 'n_clicks'),
     Input('botao_apagar_historico', 'n_clicks')],
    State('menu_selecao_paciente', 'options'))
def agendamento(paciente_selecionado, ini_patologia, freq_patologia, int_patologia, trata_ant, uso_medic, h_infancia, h_rotina, h_alimentar,
                h_sono, h_vicios, h_cirurgias, h_hobbies, h_trabalho, h_pais, h_irmaos, h_conjuge, h_filhos, h_lar, h_transt_familia, s_n_clicks, a_n_clicks, lista_pacientes):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    if paciente_selecionado:
        nome_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado), 'Nenhum paciente selecionado')
        if nome_selecionado and s_n_clicks:
            try:
                conexao = sqlite3.connect('base.db')
                cursor = conexao.cursor()
                cursor.execute("SELECT [Início da Patologia] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                ini_pat_ant = result[0] if result else ''
                ini_pat_nova = f'{ini_patologia}'
                ini_pat_att = f'{ini_pat_ant}, {ini_pat_nova}'
                cursor.execute("SELECT [Frequência da Patologia] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                freq_pat_ant = result[0] if result else ''
                freq_pat_nova = f'{freq_patologia}'
                freq_pat_att = f'{freq_pat_ant}, {freq_pat_nova}'
                cursor.execute("SELECT [Intensidade da Patologia] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                int_pat_ant = result[0] if result else ''
                int_pat_nova = f'{int_patologia}'
                int_pat_att = f'{int_pat_ant}, {int_pat_nova}'
                cursor.execute("SELECT [Tratamentos Anteriores] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                trat_ant = result[0] if result else ''
                trat_nova = f'{trata_ant}'
                trat_att = f'{trat_ant}, {trat_nova}'
                cursor.execute("SELECT [Uso de Medicamentos] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                uso_med_ant = result[0] if result else ''
                uso_med_nova = f'{uso_medic}'
                uso_med_att = f'{uso_med_ant}, {uso_med_nova}'
                cursor.execute("SELECT [Histórico Infância] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_inf_ant = result[0] if result else ''
                h_inf_nova = f'{h_infancia}'
                h_inf_att = f'{h_inf_ant}, {h_inf_nova}'
                cursor.execute("SELECT [Histórico Rotina] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_rot_ant = result[0] if result else ''
                h_rot_nova = f'{h_rotina}'
                h_rot_att = f'{h_rot_ant}, {h_rot_nova}'
                cursor.execute("SELECT [Histórico Alimentar] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_al_ant = result[0] if result else ''
                h_al_nova = f'{h_alimentar}'
                h_al_att = f'{h_al_ant}, {h_al_nova}'
                cursor.execute("SELECT [Histórico Sono] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_sono_ant = result[0] if result else ''
                h_sono_nova = f'{h_sono}'
                h_sono_att = f'{h_sono_ant}, {h_sono_nova}'
                cursor.execute("SELECT [Histórico Vícios] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_vic_ant = result[0] if result else ''
                h_vic_nova = f'{h_vicios}'
                h_vic_att = f'{h_vic_ant}, {h_vic_nova}'
                cursor.execute("SELECT [Histórico Cirurgias] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_cir_ant = result[0] if result else ''
                h_cir_nova = f'{h_cirurgias}'
                h_cir_att = f'{h_cir_ant}, {h_cir_nova}'
                cursor.execute("SELECT [Histórico Hobbies] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_hob_ant = result[0] if result else ''
                h_hob_nova = f'{h_hobbies}'
                h_hob_att = f'{h_hob_ant}, {h_hob_nova}'
                cursor.execute("SELECT [Histórico Trabalho] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_trab_ant = result[0] if result else ''
                h_trab_nova = f'{h_trabalho}'
                h_trab_att = f'{h_trab_ant}, {h_trab_nova}'
                cursor.execute("SELECT [Histórico Pais] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_pais_ant = result[0] if result else ''
                h_pais_nova = f'{h_pais}'
                h_pais_att = f'{h_pais_ant}, {h_pais_nova}'
                cursor.execute("SELECT [Histórico Irmãos] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_irm_ant = result[0] if result else ''
                h_irm_nova = f'{h_irmaos}'
                h_irm_att = f'{h_irm_ant}, {h_irm_nova}'
                cursor.execute("SELECT [Histórico Cônjuge] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_conj_ant = result[0] if result else ''
                h_conj_nova = f'{h_conjuge}'
                h_conj_att = f'{h_conj_ant}, {h_conj_nova}'
                cursor.execute("SELECT [Histórico Filhos] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_fil_ant = result[0] if result else ''
                h_fil_nova = f'{h_filhos}'
                h_fil_att = f'{h_fil_ant}, {h_fil_nova}'
                cursor.execute("SELECT [Histórico Lar] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_lar_ant = result[0] if result else ''
                h_lar_nova = f'{h_lar}'
                h_lar_att = f'{h_lar_ant}, {h_lar_nova}'
                cursor.execute("SELECT [Transtornos Mentais na Família] FROM Consulta WHERE Nome=?", (nome_selecionado,))
                result = cursor.fetchone()
                h_tfam_ant = result[0] if result else ''
                h_tfam_nova = f'{h_transt_familia}'
                h_tfam_att = f'{h_tfam_ant}, {h_tfam_nova}'
                cursor.execute("UPDATE Consulta SET 'Início da Patologia'=?, 'Frequência da Patologia'=?, 'Intensidade da Patologia'=?, 'Tratamentos Anteriores'=?, 'Uso de Medicamentos'=?, 'Histórico Infância'=?, 'Histórico Rotina'=?, 'Histórico Alimentar'=?, 'Histórico Sono'=?, 'Histórico Vícios'=?, 'Histórico Cirurgias'=?, 'Histórico Hobbies'=?, 'Histórico Trabalho'=?, 'Histórico Pais'=?, 'Histórico Irmãoes'=?, 'Histórico Cônjuge'=?, 'Histórico Filhos'=?, 'Histórico Lar'=?, 'Transtornos Mentais da Família'=? WHERE Nome=?",
                                (ini_pat_att, freq_pat_att, int_pat_att, trat_att, uso_med_att, h_inf_att, h_rot_att, h_al_att, h_sono_att, h_vic_att, h_cir_att, h_hob_att, h_trab_att, h_pais_att, h_irm_att, h_conj_att, h_fil_att, h_lar_att, h_tfam_att, nome_selecionado))
                conexao.commit()
                conexao.close()
                return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'))]
            except Exception as e:
                print(f'Erro ao atualizar a base de dados: {str(e)}')
        if nome_selecionado and a_n_clicks:
            _ = ""
            conexao1 = sqlite3.connect('base.db')
            cursor = conexao1.cursor()
            cursor.execute("UPDATE Consulta SET 'Queixa Principal' = ?, 'Queixa Secundária' = ?, 'Sintomas' = ? WHERE Nome=?", (_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, nome_selecionado))
            conexao1.commit()
            conexao1.close()
            return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'), color="danger")]
        return ['']

# ANAMNESE EXAME PSÍQUICO
@app.callback(
    [Output('saida_formulario_exame', 'children')],
    [Input('menu_selecao_paciente', 'value'),
     Input('exame_aparencia', 'value'),
     Input('exame_comportamento', 'value'),
     Input('exame_postura', 'value'),
     Input('exame_orientacao', 'value'),
     Input('exame_atencao', 'value'),
     Input('exame_memoria', 'value'),
     Input('exame_inteligencia', 'value'),
     Input('exame_senso', 'value'),
     Input('exame_distorcoes_cognitivas', 'value'),
     Input('exame_humor', 'value'),
     Input('exame_pensamento', 'value'),
     Input('exame_conteudo', 'value'),
     Input('exame_expansao_eu', 'value'),
     Input('exame_retracao_eu', 'value'),
     Input('exame_negacao_eu', 'value'),
     Input('exame_linguagem', 'value'),
     Input('exame_consciencia', 'value'),
     Input('exame_comentarios', 'value'),
     Input('botao_salvar_exame_psiquico', 'n_clicks')],
    State('menu_selecao_paciente', 'options'))
def agendamento(paciente_selecionado, aparencia, comportamento, postura, orientacao, atencao, memoria, inteligencia, senso, distorcoes, humor, pensamento, conteudo, expansao, retracao, negacao, linguagem, consciencia, comentarios, n_clicks, lista_pacientes):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    if paciente_selecionado:
        nome_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado), 'Nenhum paciente selecionado')
        if nome_selecionado and n_clicks:
            try:
                distorcoes_ = ', '.join(distorcoes) if distorcoes else ''
                conteudo_ = ', '.join(conteudo) if conteudo else ''
                expansao_ = ', '.join(expansao) if expansao else ''
                retracao_ = ', '.join(retracao) if retracao else ''
                negacao_ = ', '.join(negacao) if negacao else ''
                linguagem_ = ', '.join(linguagem) if linguagem else ''
                conexao = sqlite3.connect('base.db')
                cursor = conexao.cursor()
                cursor.execute("SELECT Nome FROM Pacientes WHERE Nome = ?", (nome_selecionado,))
                paciente_existente = cursor.fetchone()
                if paciente_existente[0] == str(nome_selecionado):
                    cursor.execute(
                        "UPDATE Pacientes SET 'Exame Aparência'=?, 'Exame Comportamento'=?, 'Exame Postura'=?, 'Exame Orientação'=?, 'Exame Atenção'=?, 'Exame Memória'=?, 'Exame Inteligência'=?, 'Exame Senso'=?, 'Exame Distorções Cognitivas'=?, 'Exame Humor'=?, 'Exame Pensamentos'=?, 'Exame Conteúdo'=?, 'Exame Expansão'=?, 'Exame Retração'=?, 'Exame Negação'=?, 'Exame Linguagem'=?, 'Exame Consciência'=?, 'Comentários Exame'=? WHERE Nome=?",
                        (aparencia, comportamento, postura, orientacao, atencao, memoria, inteligencia, senso, distorcoes_, humor, pensamento, conteudo_, expansao_, retracao_, negacao_, linguagem_, consciencia, comentarios, nome_selecionado))
                    conexao.commit()
                else:
                    cursor.execute(
                        "INSERT INTO Pacientes ('Nome', 'Exame Aparência', 'Exame Comportamento', 'Exame Postura', 'Exame Orientação', 'Exame Atenção', 'Exame Memória', 'Exame Inteligência', 'Exame Senso', 'Exame Distorções Cognitivas', 'Exame Humor', 'Exame Pensamentos', 'Exame Conteúdo', 'Exame Expansão', 'Exame Retração', 'Exame Negação', 'Exame Linguagem', 'Exame Consciência', 'Comentários Exame') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (paciente_selecionado, aparencia, comportamento, postura, orientacao, atencao, memoria, inteligencia, senso, distorcoes_, humor, pensamento, conteudo_, expansao_, retracao_, negacao_, linguagem_, comentarios, consciencia))
                    conexao.commit()
                conexao.close()
                return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'))]
            except Exception as e:
                print(f'Erro ao atualizar a base de dados: {str(e)}')
        return ['']

# ANAMNESE ANOTACOES
@app.callback(
    [Output('saida_anotacoes_anamnese', 'children')],
    [Input('menu_selecao_paciente', 'value'),
     Input('texto_anotacoes_anamnese', 'value'),
     Input('botao_salvar_anot_anamnese', 'n_clicks'),
     Input('botao_apagar_anot_anamnese', 'n_clicks')],
    State('menu_selecao_paciente', 'options'))
def agendamento(paciente_selecionado, anot_anamnese, s_n_clicks, a_n_clicks, lista_pacientes):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    if paciente_selecionado:
        nome_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado), 'Nenhum paciente selecionado')
        if nome_selecionado and s_n_clicks:
            _ = ""
            conexao = sqlite3.connect('base.db')
            cursor = conexao.cursor()
            cursor.execute("SELECT [Anotações Anamnese] FROM Pacientes WHERE Nome=?", (nome_selecionado,))
            result = cursor.fetchone()
            anot_anamnese_ant = result[0] if result else _
            anot_anamnese_nova = f'{anot_anamnese}'
            anot_anamnese_att = f'{anot_anamnese_ant}, {anot_anamnese_nova}'
            cursor.execute("UPDATE Pacientes SET 'Anotações Anamnese'=? WHERE Nome=?", (anot_anamnese_att, nome_selecionado))
            conexao.commit()
            conexao.close()
            return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'))]
        if nome_selecionado and a_n_clicks:
            _ = ""
            conexao = sqlite3.connect('base.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE Pacientes SET 'Anotações Anamnese'=? WHERE Nome=?", (_, nome_selecionado))
            conexao.commit()
            conexao.close()
            return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'), color="danger")]
        return ['']

# ANAMNESE HIPOTESE DIAGNÓSTICA
@app.callback(
    [Output('saida_saida_formulario_hipotese_diagnostica', 'children')],
    [Input('menu_selecao_paciente', 'value'),
     Input('texto_hipotese_diagnostica', 'value'),
     Input('cid_dsm', 'value'),
     Input('botao_salvar_anot_anamnese', 'n_clicks'),
     Input('botao_apagar_anot_anamnese', 'n_clicks')],
    State('menu_selecao_paciente', 'options'))
def agendamento(paciente_selecionado, hip_diagnistica, cid_dsm, s_n_clicks, a_n_clicks, lista_pacientes):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    if paciente_selecionado:
        nome_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado), 'Nenhum paciente selecionado')
        if nome_selecionado and s_n_clicks:
            conexao = sqlite3.connect('base.db')
            cursor = conexao.cursor()
            cursor.execute("SELECT [Hipótese Diagnóstica] FROM Pacientes WHERE Nome=?", (nome_selecionado,))
            result = cursor.fetchone()
            hip_diag_ant = result[0] if result else ''
            hip_diag_nova = f'{hip_diagnistica}'
            hip_diag_att = f'{hip_diag_ant}, {hip_diag_nova}'
            cursor.execute("SELECT [CID DSM] FROM Pacientes WHERE Nome=?", (nome_selecionado,))
            result = cursor.fetchone()
            cid_dsm_ant = result[0] if result else ''
            cid_dsm_nova = f'{hip_diagnistica}'
            cid_dsm_att = f'{cid_dsm_ant}, {cid_dsm_nova}'
            cursor.execute("UPDATE Pacientes SET 'Hipótese Diagnóstica'=?, 'CID DSM'=? WHERE Nome=?", (hip_diag_att, cid_dsm_att, nome_selecionado))
            conexao.commit()
            conexao.close()
            return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'))]
        if nome_selecionado and a_n_clicks:
            _ = ""
            conexao = sqlite3.connect('base.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE Pacientes SET 'Hipótese Diagnóstica'=?, 'CID DSM'=? WHERE Nome=?", (_, _, nome_selecionado))
            conexao.commit()
            conexao.close()
            return [dbc.Alert(html.Small(f'Prontuário de {nome_selecionado} atualizado com sucesso'), color="danger")]
        return ['']

# CADASTRO DE PACIENTE
@app.callback(
    [Output('saida_formulario_cadastro', 'children')],
    [Input('botao_cadastrar_paciente', 'n_clicks')],
    [State('nome', 'value'),
     State('data_nascimento', 'value'),
     State('sexo', 'value'),
     State('identidade', 'value'),
     State('cpf', 'value'),
     State('nacionalidade', 'value'),
     State('estado_civil', 'value'),
     State('grau_instrucao', 'value'),
     State('profissao', 'value'),
     State('religiao', 'value'),
     State('logradouro', 'value'),
     State('telefone', 'value'),
     State('email', 'value'),
     State('foto', 'contents'),
     State('observacoes_cadastro', 'value')])
def cadastro(n_clicks, nome, data_nascimento, sexo, identidade, cpf, nacionalidade,estado_civil,
             grau_instrucao, profissao, religiao, logradouro, telefone, email, foto, observacoes_cadastro):
    df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    if n_clicks:
        try:
            conexao = sqlite3.connect('base.db')
            cursor = conexao.cursor()
            foto_convertida = converte_imagem(foto, nome)
            cursor.execute(
                    "INSERT INTO Pacientes (Nome, 'Data de Nascimento', Sexo, Identidade, CPF, Nacionalidade, 'Estado Civil', 'Grau de Instrução', Profissão, Religião, Logradouro, Telefone, Email, Foto, 'Cadastro Observações') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (nome, data_nascimento, sexo, identidade, cpf, nacionalidade, estado_civil, grau_instrucao, profissao, religiao, logradouro, telefone, email, foto_convertida, observacoes_cadastro))
            conexao.commit()
            conexao.close()
            df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
            return [dbc.Alert(f'{nome} cadastrado(a) com sucesso!', color='info')]
        except Exception as e:
            print(f'Erro ao atualizar a base de dados: {str(e)}')
    return ['']

# CADASTRO DE COLABORADOR
@app.callback(
    [Output('saida_formulario_cadastro_colab', 'children')],
    [Input('botao_cadastrar_colaborador', 'n_clicks')],
    [State('nome_colab', 'value'),
     State('telefone_colab', 'value'),
     State('especialidade_colab', 'value'),
     State('credencial_colab', 'value'),
     State('observacoes_colab', 'value')])
def cadastro(n_clicks, nome_colab, telefone_colab, especialidade_colab, credencial_colab, observacoes_colab):
    if n_clicks:
        try:
            conexao = sqlite3.connect('base.db')
            cursor = conexao.cursor()
            cursor.execute(
                    "INSERT INTO Colaboradores (Nome, Telefone, Especialidade, 'Registro Profissional', 'Observações Colaborador') VALUES (?, ?, ?, ?, ?)",
                    (nome_colab, telefone_colab, especialidade_colab, credencial_colab, observacoes_colab))
            conexao.commit()
            conexao.close()
            df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
            return [dbc.Alert(f'{nome_colab} cadastrado(a) com sucesso!', color='info')]
        except Exception as e:
            print(f'Erro ao atualizar a base de dados: {str(e)}')
    return ['']

# ATUALIZA PRONTUARIO SELECIONADO
@app.callback(
    Output('saida_prontuario_selecionado', 'children'),
    [Input('menu_selecao_paciente', 'value')],
    State('menu_selecao_paciente', 'options'))
def carrega_prontuario(paciente_selecionado, lista_pacientes):
    if paciente_selecionado:
        df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()
        nome_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado),
                                'Nenhum paciente selecionado')
        img_path = os.path.join('imagens', f'{nome_selecionado}.jpg')
        if os.path.exists(img_path):
            with open(img_path, "rb") as img_file:
                encoded_image = base64.b64encode(img_file.read()).decode()
            img_component = html.Img(src=f"data:image/jpeg;base64,{encoded_image}",
                                     style={"max-width": "20%", "display": "block", "margin": "0 auto"})
        else:
            img_component = html.Div("Imagem não encontrada")
        def formatar(key, value):
            return f'{key} {value}' if value is not None else f'{key} '
        df_ = df.loc[df['Nome'] == nome_selecionado]
        return html.Div([
            dbc.Row([html.Div(img_component)]),
            html.P(),
            html.H6('Dados Pessoais'),
            dbc.Row([dbc.Col([html.Div(f'Nome: {nome_selecionado}')], width = 6),
                     dbc.Col([html.Div(formatar('Data de Nascimento:', df_.iloc[0]["Data de Nascimento"]))], width = 6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Sexo:', df_.iloc[0]["Sexo"]))], width=6),
                     dbc.Col([html.Div(formatar('Identidade:', df_.iloc[0]["Identidade"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('CPF:', df_.iloc[0]["CPF"]))], width=6),
                     dbc.Col([html.Div(formatar('Nacionalidade:', df_.iloc[0]["Nacionalidade"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Estado Civil:', df_.iloc[0]["Estado Civil"]))], width=6),
                     dbc.Col([html.Div(formatar('Grau de Instrução:', df_.iloc[0]["Grau de Instrução"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Religião:', df_.iloc[0]["Religião"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Profissão:', df_.iloc[0]["Profissão"]))], width=6),
                     dbc.Col([html.Div(formatar('Logradouro:', df_.iloc[0]["Logradouro"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Telefone:', df_.iloc[0]["Telefone"]))], width=6),
                     dbc.Col([html.Div(formatar('E-mail:', df_.iloc[0]["Email"]))], width=6)]),
            html.P(),
            dbc.Row([dbc.Col([html.Div(formatar('Observações:', df_.iloc[0]["Cadastro Observações"]))], width=6)]),
            html.P(),
            html.H6('Dados Clínicos'),
            dbc.Row([html.Div(formatar('Queixa Principal:', df_consulta.iloc[0]["Queixa Principal"]))]),
            dbc.Row([html.Div(formatar('Queixa Secundária:', df_consulta.iloc[0]["Queixa Secundária"]))]),
            html.P(),
            dbc.Row([dbc.Col([html.Div(formatar('Início da Patologia:', df_consulta.iloc[0]["Início da Patologia"]))], width=6),
                     dbc.Col([html.Div(formatar('Sintomas:', df_consulta.iloc[0]["Sintomas"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Frequência da Patologia:', df_consulta.iloc[0]["Frequência da Patologia"]))], width=6),
                     dbc.Col([html.Div(formatar('Intensidade da Patologia:', df_consulta.iloc[0]["Intensidade da Patologia"]))], width=6)]),
            html.P(),
            dbc.Row([dbc.Col([html.Div(formatar('Tratamentos Anteriores:', df_consulta.iloc[0]["Tratamentos Anteriores"]))], width=6),
                     dbc.Col([html.Div(formatar('Uso de Medicamentos:', df_consulta.iloc[0]["Uso de Medicamentos"]))], width=6)]),
            html.P(),
            html.H6('Histórico'),
            dbc.Row([html.Div(formatar('Infância:', df_consulta.iloc[0]["Histórico Infância"]))]),
            dbc.Row([html.Div(formatar('Rotina:', df_consulta.iloc[0]["Histórico Rotina"]))]),
            dbc.Row([html.Div(formatar('Vícios:', df_consulta.iloc[0]["Histórico Vícios"]))]),
            dbc.Row([html.Div(formatar('Hobbies:', df_consulta.iloc[0]["Histórico Hobbies"]))]),
            dbc.Row([html.Div(formatar('Trabalho:', df_consulta.iloc[0]["Histórico Trabalho"]))]),
            dbc.Row([html.Div(formatar('Pais:', df_consulta.iloc[0]["Histórico Pais"]))]),
            dbc.Row([html.Div(formatar('Irmãos:', df_consulta.iloc[0]["Histórico Irmãos"]))]),
            dbc.Row([html.Div(formatar('Conjuge:', df_consulta.iloc[0]["Histórico Cônjuge"]))]),
            dbc.Row([html.Div(formatar('Filhos:', df_consulta.iloc[0]["Histórico Filhos"]))]),
            dbc.Row([html.Div(formatar('Lar:', df_consulta.iloc[0]["Histórico Lar"]))]),
            html.P(),
            html.H6('Exame Psíquico'),
            dbc.Row([html.Div(formatar('Aparência:', df_consulta.iloc[0]["Exame Aparência"]))]),
            dbc.Row([html.Div(formatar('Comportamento:', df_consulta.iloc[0]["Exame Comportamento"]))]),
            dbc.Row([dbc.Col([html.Div(formatar('Postura:', df_consulta.iloc[0]["Exame Postura"]))], width=6),
                     dbc.Col([html.Div(formatar('Orientação:', df_consulta.iloc[0]["Exame Orientação"]))], width=6)]),
            dbc.Row([html.Div(formatar('Atenção:', df_consulta.iloc[0]["Exame Atenção"]))]),
            dbc.Row([html.Div(formatar('Memória:', df_consulta.iloc[0]["Exame Memória"]))]),
            dbc.Row([html.Div(formatar('Inteligência:', df_consulta.iloc[0]["Exame Inteligência"]))]),
            dbc.Row([dbc.Col([html.Div(formatar('Senso percepção:', df_consulta.iloc[0]["Exame Senso"]))], width=6),
                     dbc.Col([html.Div(formatar('Humor:', df_consulta.iloc[0]["Exame Humor"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Pensamento:', df_consulta.iloc[0]["Exame Pensamentos"]))], width=6),
                     dbc.Col([html.Div(formatar('Conteúdo:', df_consulta.iloc[0]["Exame Conteúdo"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Expansão do Eu:', df_consulta.iloc[0]["Exame Expansão"]))], width=6),
                     dbc.Col([html.Div(formatar('Retração do Eu:', df_consulta.iloc[0]["Exame Retração"]))], width=6)]),
            dbc.Row([dbc.Col([html.Div(formatar('Negação do Eu:', df_consulta.iloc[0]["Exame Negação"]))], width=6),
                     dbc.Col([html.Div(formatar('Linguagem:', df_consulta.iloc[0]["Exame Linguagem"]))], width=6)]),
            dbc.Row([html.Div(formatar('Consciência da condição atual:', df_consulta.iloc[0]["Exame Consciência"]))]),
            html.P(),
            html.H6('Hipótese Diagnóstica'),
            dbc.Row([html.Div(formatar('Descrição:', df_consulta.iloc[0]["Hipótese Diagnóstica"]))]),
            dbc.Row([html.Div(formatar('CID - DSM:', df_consulta.iloc[0]["CID DSM"]))]),
            html.P(),
            html.H6('Histórico de Consultas'),
            dbc.Row([html.Div(formatar('', df_agenda.iloc[0]["Histórico de Consultas"].replace(r'.,', '. ||| \n').replace(r'None', '')))]),
            html.Hr(),
            html.P(),
            html.P(),
        ])
    return ''

# GERA CONTRATO DE PSICOTERAPIA ONLINE
@app.callback(
    [Output('conteudo_contrato_01', 'children')],
    [Input('menu_selecao_paciente', 'value'),
     Input('contrato_profissional', 'value'),
     Input('contrato_duracao', 'value'),
     Input('contrato_valor', 'value'),
     Input('contrato_conta', 'value'),
     Input('contrato_cidade', 'value'),
     Input('contrato_dia', 'value'),
     Input('contrato_mes', 'value'),
     Input('contrato_ano', 'value'),
     Input('botao_salvar_contrato_01', 'n_clicks')],
    State('menu_selecao_paciente', 'options'))
def contrato_psi_online(paciente_selecionado, profissional, duracao, valor, conta,
                        cidade, dia, mes, ano, n_clicks, lista_pacientes):
    if n_clicks:
        nome_selecionado = next((i['label'] for i in lista_pacientes if i['value'] == paciente_selecionado),
                                'Nenhum paciente selecionado')
        contrato_preenchido = html.Div([
            html.Br(),
            html.H6('CONTRATO DE PSICOTERAPIA INDIVIDUAL ONLINE', style={'text-align': 'center'}),
            html.Br(),
            html.P(),
            dbc.Row([
            html.Small(f"Este documento visa oficializar o vínculo de tratamento de {nome_selecionado} com o Psicólogo / Psicanalista {profissional}. ", id='texto_001', style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.Br(),
            html.P(),
            html.P('1. Do Atendimento: '),
            html.Small(f"Cada atendimento clínico terá a duração de aproximadamente {duracao} minutos, sendo realizado em horário previamente combinado, estando o terapeuta à disposição do paciente durante este período estabelecido. ", id='texto_002', style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.Small("Os dias e horário dos atendimentos serão combinados com o cliente, podendo variar de acordo com as necessidades de adequação da agenda do terapeuta e demanda do cliente.", style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.P(),
            html.P('2. Do Sigilo: '),
            html.Small("O psicólogo respeitará o sigilo profissional a fim de proteger, por meio da confiabilidade, a intimidade das pessoas, grupos ou organizações, a que tenha acesso no exercício profissional (Código de Ética do Psicólogo, artigo 9º). ", style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.P(),
            html.P('3. Do Período de Tratamento: '),
            html.Small("A duração do tratamento psicoterápico varia consideravelmente dependendo da pessoa e da natureza das questões a serem trabalhadas. O paciente deve ser informado sobre qualquer prospecto de encurtamento ou alongamento do tratamento. ", style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.P(),
            html.P('4. Dos Honorários: '),
            html.Small("O pagamento será efetuado diretamente ao psicólogo nas datas combinadas no dia da primeira entrevista. Qualquer alteração no contrato ou reajuste somente poderá acontecer com o conhecimento e consentimento entre ambas as partes. ", style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.Small(f"O Valor acordado para cada sessão é R$ {valor} . O pagamento será feito mediante Pix para a chave: {conta} . O pagamento poderá ser realizado a cada sessão ou mensalmente com desconto a combinar. ", id='texto_003', style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.P(),
            html.P('5. Das Alterações de Agenda: '),
            html.Small("As desmarcações deverão ser feitas com antecedência de até 12 horas. O terapeuta deverá ser avisado no caso de imprevistos que impeçam o comparecimento do paciente. Mudanças de horário só serão possíveis quando houver disponibilidade do terapeuta. ", style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.Small("Sessões em que o cliente não comparecer serão cobradas normalmente. A partir de duas faltas consecutivas, sem aviso, durante o tratamento, o atendimento será considerado interrompido e o cliente poderá perder sua vaga preferencial de horário.",style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
            html.P(),
            html.P(),
            html.P(),
            html.Small(f"{cidade} , {dia} de {mes} de {ano}.", id='texto_004', style={'white-space': 'pre-wrap', 'text-align': 'right'}),
            html.P(),
            html.P(),
            html.P(),
            html.Small("________________________________________________________________________________", style={'white-space': 'pre-wrap', 'text-align': 'center'}),
            html.P(),
            html.Small("Credencial nº: __________________ . Órgão Expeditor: __________________________", style={'white-space': 'pre-wrap', 'text-align': 'center'}),
            ]),
            html.P(),
            html.Br(),
            html.P()])
        
        from funcoes_aux import gera_contrato_psicoterapia_01
        gera_contrato_psicoterapia_01(nome_selecionado, profissional, duracao, valor,
                                      conta, cidade, dia, mes, ano)

        with sqlite3.connect('base.db') as conn:
            cursor = conn.cursor()
            caminho_arquivo = f'{nome_selecionado}_contrato_psicoterapia.docx'
            from funcoes_aux import converte_arquivo
            contrato_blob = converte_arquivo(caminho_arquivo)
            cursor.execute("UPDATE Pacientes SET Anexos = ? WHERE Nome = ?", (contrato_blob, nome_selecionado))
            conn.commit()
        return [contrato_preenchido]
    from pag_documentos import modelo_contrato_psicoterapia_online
    return [modelo_contrato_psicoterapia_online]

if __name__ == '__main__':
    #app.run_server(host='0.0.0.0', port=8080, debug=False, use_reloader=False)
    #app.run()
    app.run_server(debug = True)
