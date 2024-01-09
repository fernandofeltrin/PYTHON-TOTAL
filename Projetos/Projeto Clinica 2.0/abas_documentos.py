from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_abas_documentos = dbc.Container([
                html.Hr(),
                    dbc.Card([
                        dbc.CardBody(dbc.Tabs(id='abas_documentos', active_tab='modelos_anamnese', children=[
                            dbc.Tab(label='Anamneses', tab_id='modelos_anamneses'),
                            dbc.Tab(label='Atestados', tab_id='modelos_atestados'),
                            dbc.Tab(label='Cartas / Termos', tab_id='modelos_cartas_termos'),
                            dbc.Tab(label='Contratos', tab_id='modelos_contratos'),
                            dbc.Tab(label='Declarações', tab_id='modelos_declaracoes'),
                            dbc.Tab(label='Encaminhamentos', tab_id='modelos_encaminhamentos'),
                            dbc.Tab(label='Fichas de Avaliação', tab_id='modelos_fichas_avaliacao'),
                            dbc.Tab(label='Fichas de Evolução', tab_id='modelos_fichas_evolucao'),
                            dbc.Tab(label='Laudos / Pareceres', tab_id='modelos_laudos_pareceres'),
                            dbc.Tab(label='Prescrições', tab_id='modelos_prescricoes'),
                            dbc.Tab(label='Recibos', tab_id='modelos_recibos'),
                            dbc.Tab(label='Roteiros', tab_id='modelos_roteiros'),
                            dbc.Tab(label='Testes Psicométricos', tab_id='modelos_testes_psicometricos'),
                            dbc.Tab(label='Outros', tab_id='modelos_outros')])),dbc.CardBody(html.Div(id='conteudo_abas_documentos'))])]), ''

aba_anamneses = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Anamnese Geral", style={"text-align": "left"})], width=11)]), id='modal_anamnese_geral', n_clicks=0, action=True),
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Anamnese Infantil", style={"text-align": "left"})], width=11)]), id='modal_anamnese_infantil', n_clicks=0, action=True),
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Anamnese Autismo", style={"text-align": "left"})], width=11)]), id='modal_anamnese_autismo', n_clicks=0, action=True),
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Anamnese Cirurgia Bariátrica", style={"text-align": "left"})], width=11)]), id='modal_anamnese_cirurgia_bariatrica', n_clicks=0, action=True),
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Anamnese Compulsão Alimentar", style={"text-align": "left"})], width=11)]), id='modal_anamnese_compulsao_alimentar', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Anamnese Psicomotricidade", style={"text-align": "left"})], width=11)]), id='modal_anamnese_psicomotricidade', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_atestados = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Atestado Psicológico Geral", style={"text-align": "left"})], width=11)]), id='modal_at_psicologico', n_clicks=0, action=True),
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Atestado de Sanidade Mental", style={"text-align": "left"})], width=11)]), id='modal_at_sanidade_mental', n_clicks=0, action=True),
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Atestado de Boa Conduta", style={"text-align": "left"})], width=11)]), id='modal_at_boa_conduta', n_clicks=0, action=True),
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("Atestado de Aptidão Específica", style={"text-align": "left"})], width=11)]), id='modal_at_aptidao', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(
                            dbc.Row([
                                    dbc.Col([DashIconify(icon="carbon:document", width=20)], width=1),
                                    dbc.Col([html.P("-", style={"text-align": "left"})], width=11)]), id='-', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])



aba_cartas_termos = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Carta de Pedido de Emprego")], width=11)
                        ]), id='modal_carta_pedido_emprego', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Carta de Recomendação Geral")], width=11)
                        ]), id='modal_carta_recomendacao_geral', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Carta de Solicitação de Curadoria")], width=11)
                        ]), id='modal_carta_solicitacao_curadoria', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_contratos = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Contrato de Psicoterapia Individual")], width=11)
                        ]), id='modal_contrato_psicoterapia_individual', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Contrato de Psicoterapia Familiar / em Grupo")], width=11)
                        ]), id='modal_contrato_psicoterapia_grupo', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Contrato de Psicoterapia Online")], width=11)
                        ]), id='modal_contrato_psicoterapia_online', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Contrato de Consulta Terapêutica Esporádica / Geral")], width=11)
                        ]), id='modal_contrato_psicoterapia_esporadica', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Contrato de Prestação de Serviços de Consultoria")], width=11)
                        ]), id='modal_contrato_prestacao_servico_consultoria', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])



aba_declaracoes = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Declaração de Acompanhamento Psicológico")], width=11)
                        ]), id='modal_declaracao_acompanhamento', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Declaração de Tratamento Psicoterápico")], width=11)
                        ]), id='modal_declaracao_tratamento', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])


aba_encaminhamentos = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Encaminhamento Para Outro Profissional da Saúde")], width=11)
                        ]), id='modal_encaminhamento_outro_profissional', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])


aba_fichas_avaliacao = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Ficha de Avaliação Psicológica Geral")], width=11)
                        ]), id='modal_ficha_avaliacao_psicologica_geral', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Ficha de Avaliação de Risco de Suicídio")], width=11)
                        ]), id='modal_ficha_avaliacao_risco_suicidio', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_fichas_evolucao = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Ficha de Acompanhamento / Evolução Geral")], width=11)
                        ]), id='modal_ficha_evolucao_geral', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_laudos_pareceres = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Laudo Psicológico Geral")], width=11)
                        ]), id='modal_laudo_psicologico_geral', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Parecer de Saúde Mental Parcial")], width=11)
                        ]), id='modal_parecer_saude_mental', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_prescricoes = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Receituário Geral Para Medicação")], width=11)
                        ]), id='modal_receituario_geral_medicacao', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_recibos = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Recibo de Pagamento de Consulta / Sessão Unitária")], width=11)
                        ]), id='modal_recibo_consulta_unitaria', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Recibo de Pagamento de Pacote de Tratamento")], width=11)
                        ]), id='modal_recibo_pacote_tratamento', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Recibo de Pagamento de Aquisição de Serviço Adicional")], width=11)
                        ]), id='modal_recibo_aquisicao_servico_adicional', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])


aba_roteiros = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Roteiro para Hipnoterapia - Escopo Ansiedade")], width=11)
                        ]), id='modal_roteiro_hipnoterapia_ansiedade', n_clicks=0, action=True),
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Roteiro para Hipnoterapia - Escopo Luto")], width=11)
                        ]), id='modal_roteiro_hipnoterapia_luto', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_testes_psicometricos = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Teste")], width=11)
                        ]), id='modal_teste_psicometrico_', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])

aba_outros = html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([DashIconify(icon="carbon:document", width=22)], width=1),
                            dbc.Col([html.P("Teste")], width=11)
                        ]), id='modal_outro_01', n_clicks=0, action=True),
                    ], flush=True)
                ]),
                dbc.Col([
                    dbc.ListGroup([
                        dbc.ListGroupItem(dbc.Row([
                            dbc.Col([], width=1),
                            dbc.Col([html.P("")], width=11)
                        ]), id='', n_clicks=0, action=True),
                    ], flush=True)
                ])
            ])
        ])
