from dash import html, dcc, dash_table
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_documentos_anamnese_infantil = []
layout_documentos_anamnese_autismo = []
layout_documentos_anamnese_c_bariatrica = []
layout_documentos_anamnese_comp_a = []
layout_documentos_anamnese_psicomotricidade = []

layout_documentos_anamnese_geral = html.Div([
    html.H6('Selecione um paciente:'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else ''),
    html.P(id='valor_selecionado'),
    html.P(),
    html.Hr(),
    html.H6('Parecer descritivo:'),
    html.P(),
    dbc.Row([
        dbc.Label('Queixa Principal: ', width=2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id='queixa_pri', value=''), width=10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Queixa Secundária: ', width=2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id='queixa_sec', value=''), width=10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Sintomas Gerais: ', width=2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id='sintomas', value=''), width=10)]),
    html.P(),
    dbc.Row([dbc.InputGroup([
                dbc.InputGroupText("Observações:", style={'fontSize': '13px'}),
                dbc.Textarea(id='observacoes', rows=5, value=''),],),]),
    html.Br(),
    html.H6('Histórico clínico:'),
    html.P(),
    dbc.Row([
        dbc.Label('Início da Patologia: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id = 'inicio_pat', type='text', value=''), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Frequência: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='freq_pat', type='text', value=''), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Intensidade: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='inte_pat', type='text', value=''), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Tratamentos Anteriores: ', width=2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='trat_ant', type='text', value=''), width=10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Uso de Medicamentos: ', width=2, style={'fontSize': '14px'}),
        dbc.Col(
            dbc.Input(id='uso_medic', type='text', value=''), width=10)]),
    html.Br(),
    html.H6('Histórico Pessoal'),
    dbc.Row([
        dbc.Label('Infância: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_infancia', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Rotina: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_rotina', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Vícios: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_vicios', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Hobbies: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_hobbies', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Trabalho: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_trabalho', value=''), width = 10)]),
    html.Br(),
    html.H6('Histórico Familiar'),
    dbc.Row([
        dbc.Label('Pais: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_pais', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Irmão(s): ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_irmao', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Cônjuge: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_conjuge', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Filhos: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_filhos', value=''), width = 10)]),
    dbc.Row([
        dbc.Label('Lar: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hist_lar', value=''), width = 10)]),
    html.Br(),
    html.H6('Exame psíquico:'),
    html.P(),
    dbc.Row([
        dbc.Label('Aparência: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'ex_aparencia', value=''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Comportamento: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'ex_comport', value=''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Postura: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(id='ex_postura',
                options=[
                    {'label': 'Cooperativo', 'value': 'Cooperativo'},
                    {'label': 'Resistente', 'value': 'Resistente'},
                    {'label': 'Indiferente', 'value': 'Indiferente'},
                ],
                value='', inline = True)], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Orientação: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(
                id='ex_orient',
                options=[
                    {'label': 'Autoidentificatória', 'value': 'Autoidentificatória'},
                    {'label': 'Corporal', 'value': 'Corporal'},
                    {'label': 'Temporal', 'value': 'Temporal'},
                    {'label': 'Espacial', 'value': 'Espacial'},
                    {'label': 'Orientada à patologia', 'value': 'Orientada à patologia'},
                ],
                value='', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Atenção: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'ex_atencao', value=''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Memória: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'ex_memoria', value=''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Inteligência: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'ex_intelig', value=''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Senso percepção: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(
                id='ex_senso',
                options=[
                    {'label': 'Normal', 'value': 'Normal'},
                    {'label': 'Alucinatória', 'value': 'Alucinatório'},
                ],
                value='', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Humor: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(
                id='ex_humor',
                options=[
                    {'label': 'Normal', 'value': 'Normal'},
                    {'label': 'Exaltado', 'value': 'Exaltado'},
                    {'label': 'Baixo', 'value': 'Baixo'},
                    {'label': 'Alteração súbita', 'value': 'Alteração súbita'},
                ], value = '', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Pensamento: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(
                id='ex_pensamento',
                options=[
                    {'label': 'Acelerado', 'value': 'Acelerado'},
                    {'label': 'Retardado', 'value': 'Retardado'},
                    {'label': 'Fuga', 'value': 'Fuga'},
                    {'label': 'Bloqueio', 'value': 'Bloqueio'},
                    {'label': 'Prolixo', 'value': 'Prolixo'},
                    {'label': 'Repetição', 'value': 'Repetição'},
                ],
                value='', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Conteúdo: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='ex_conteudo',
                options=[
                    {'label': 'Obsessões', 'value': 'Obsessões'},
                    {'label': 'Hipocondrias', 'value': 'Hipocondrias'},
                    {'label': 'Fobias', 'value': 'Fobias'},
                    {'label': 'Delírios', 'value': 'Delírios'},
                    {'label': 'Outros', 'value': 'Outros'},
                ], value='', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Expansão do Eu: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(id='ex_exp_eu',
                options=[
                    {'label': 'Grandeza', 'value': 'Grandeza'},
                    {'label': 'Ciúme', 'value': 'Ciúme'},
                    {'label': 'Reivindicação', 'value': 'Reivindicação'},
                    {'label': 'Genealógico', 'value': 'Genealógico'},
                    {'label': 'Místico', 'value': 'Místico'},
                    {'label': 'Deificação', 'value': 'Deificação'},
                    {'label': 'Erótico', 'value': 'Erótico'},
                    {'label': 'Invenção', 'value': 'Invenção'},
                    {'label': 'Fantasioso', 'value': 'Fantasioso'},
                    {'label': 'Excessivo', 'value': 'Excessivo'},
                    {'label': 'Incapacitante', 'value': 'Incapacitante'},
                    {'label': 'Outros', 'value': 'Outros'},
                ], value='', inline = True)], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Retração do Eu: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='ex_retr_eu',
                options=[
                    {'label': 'Prejuízo', 'value': 'Prejuizo'},
                    {'label': 'Auto referência', 'value': 'Referência'},
                    {'label': 'Perseguição', 'value': 'Perseguição'},
                    {'label': 'Influência', 'value': 'Influência'},
                    {'label': 'Possessão', 'value': 'Possessão'},
                    {'label': 'Humildades', 'value': 'Humildades'},
                    {'label': 'Outros', 'value': 'Outros'},
                ], value='', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Negação do Eu: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='ex_neg_eu',
                options=[
                    {'label': 'Negação', 'value': 'Negação'},
                    {'label': 'Autoacusação', 'value': 'Autoacusação'},
                    {'label': 'Culpa', 'value': 'Culpa'},
                    {'label': 'Ruína', 'value': 'Ruína'},
                    {'label': 'Niilismo', 'value': 'Niilismo'},
                    {'label': 'Tendência suicida', 'value': 'Tendência suicida'},
                    {'label': 'Outros', 'value': 'Outros'},
                ], value='', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Linguagem: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='ex_linguagem',
                options=[
                    {'label': 'Disartrias', 'value': 'Disartrias'},
                    {'label': 'Afasias', 'value': 'Afasias'},
                    {'label': 'Parafasias', 'value': 'Parafasias'},
                    {'label': 'Neologismo', 'value': 'Neologismo'},
                    {'label': 'Mussitação', 'value': 'Mussitacao'},
                    {'label': 'Logorréia', 'value': 'Logorreia'},
                    {'label': 'Para-respostas', 'value': 'Para-respostas'},
                ], value='', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Consciência da condição atual: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(
                id='ex_consci',
                options=[
                    {'label': 'Sim', 'value': 'consc_sim'},
                    {'label': 'Não', 'value': 'consc_nao'},
                    {'label': 'Parcial', 'value': 'consc_parcial'},
                ], value = '', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.Br(),
    html.H6('Observações:'),
    html.P(),
    dbc.Row([
        dbc.Label('Anotações: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'anot_anamnese', rows=10, placeholder='Digite suas anotações aqui...', value=''), width = 10)]),
    html.Br(),
    html.H6('Hipótese diagnóstica:'),
    html.P(),
    dbc.Row([
        dbc.Label('Descrição: ', width = 1, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'hip_diag', value = ''), width = 11, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Código CID-11 / DSM-5-TR: ', width=3, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='cid_dsm', type='text', value=''), width=9, style={'fontSize': '14px'})]),
    html.P(),
    html.P(),
    dbc.Button("Salvar", id="botao_salvar_anamnese_geral", n_clicks=0, size='sm'),
    html.P(),
    html.Hr(),
    html.P(),
    html.Div(id = 'saida_documento_anamnese_geral')
])


modelo_contrato_psicoterapia_online = html.Div([
    html.Br(),
    html.H6('CONTRATO DE PSICOTERAPIA INDIVIDUAL ONLINE', style={'text-align': 'center'}),
    html.Br(),
    html.P(),
    dbc.Row([
    html.Small(f"Este documento visa oficializar o vínculo de tratamento de _______________________________ com o Psicólogo / Psicanalista _______________________________. ", id='texto_001', style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
    html.Br(),
    html.P(),
    html.P('1. Do Atendimento: '),
    html.Small("Cada atendimento clínico terá a duração de aproximadamente _____ minutos, sendo realizado em horário previamente combinado, estando o terapeuta à disposição do paciente durante este período estabelecido. ", id='texto_002', style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
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
    html.Small("O Valor acordado para cada sessão é R$ __________ . O pagamento será feito mediante Pix para a chave: __________________________ . O pagamento poderá ser realizado a cada sessão ou mensalmente com desconto a combinar. ", id='texto_003', style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
    html.P(),
    html.P('5. Das Alterações de Agenda: '),
    html.Small("As desmarcações deverão ser feitas com antecedência de até 12 horas. O terapeuta deverá ser avisado no caso de imprevistos que impeçam o comparecimento do paciente. Mudanças de horário só serão possíveis quando houver disponibilidade do terapeuta. ", style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
    html.Small("Sessões em que o cliente não comparecer serão cobradas normalmente. A partir de duas faltas consecutivas, sem aviso, durante o tratamento, o atendimento será considerado interrompido e o cliente poderá perder sua vaga preferencial de horário.",style={'white-space': 'pre-wrap', 'text-align': 'justify'}),
    html.P(),
    html.P(),
    html.P(),
    html.Small("_________________________ , ______ de _________________________ de __________ .", id='texto_004', style={'white-space': 'pre-wrap', 'text-align': 'right'}),
    html.P(),
    html.P(),
    html.P(),
    html.Small("________________________________________________________________________________", style={'white-space': 'pre-wrap', 'text-align': 'center'}),
    html.P(),
    html.Small("Credencial nº: __________________ . Órgão Expeditor: __________________________", style={'white-space': 'pre-wrap', 'text-align': 'center'}),
    ]),
    html.P(),
    html.Br(),
    html.P()
])


layout_documentos_contrato_psicoterapia_online = html.Div([
    html.H6('Selecione um paciente:'),
    dcc.Dropdown(id='menu_selecao_paciente',
            options=[{'label': label, 'value': value} for value, label in nomes.items()],
            value=list(nomes.keys())[0]),
    html.P(),
    html.P(id='valor_selecionado'),
    html.P(),
    html.Small('Preencha os campos abaixo para gerar o contrato:'),
    dbc.Row([
        dbc.Col([dbc.Input(id="contrato_profissional", placeholder="Nome do Profissional", size="sm", value='')]),
        dbc.Col([dbc.Input(id="contrato_duracao", placeholder="Duração da sessão", size="sm", value='')]),
        dbc.Col([dbc.Input(id="contrato_valor", placeholder="Valor da sessão", size="sm", value='')]),
        dbc.Col([dbc.Input(id="contrato_conta", placeholder="Chave Pix", size="sm", value='')]),
    ]),
    dbc.Row([
        dbc.Col([dbc.Input(id="contrato_cidade", placeholder="Cidade", size="sm", value='')]),
        dbc.Col([dbc.Input(id="contrato_dia", placeholder="Dia", size="sm", value='')]),
        dbc.Col([dbc.Input(id="contrato_mes", placeholder="Mês", size="sm", value='')]),
        dbc.Col([dbc.Input(id="contrato_ano", placeholder="Ano", size="sm", value='')]),
    ]),
    html.P(),
    dbc.Button("Gerar Contrato", id="botao_salvar_contrato_01", n_clicks=0, size='sm'),
    dbc.Row([dbc.FormText(
        "*Ao clicar em Gerar Contrato, será gerado um arquivo Docx que será automaticamente anexado ao prontuário do paciente.",
        color="secondary", ),]),
    html.Br(),
    html.Hr(),
    html.P(),
    html.P(id = 'conteudo_contrato_01')
])


layout_ficha_av_risco_suicidio = html.Div([
    html.Hr(),
    html.H6('Selecione um paciente:'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else None),
    html.P(id='nome_selecionado'),
    html.Small(id='valor_selecionado'),
    html.P(),
    html.Hr(),
    html.P('Parecer descritivo:'),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Sofrimento atual:", style={'fontSize': '13px'}),
        dbc.Textarea(id='ficha_desc_sofrimento', value=''), ], ), ]),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Motivação:", style={'fontSize': '13px'}),
        dbc.Textarea(id='ficha_desc_motivacao', value=''), ], ), ]),
    html.P(),
    dbc.Row([dbc.InputGroup([
                dbc.InputGroupText("Significado do morrer:", style={'fontSize': '13px'}),
                dbc.Textarea(id='ficha_desc_significado', value=''),],),]),
    html.P(),
    html.Hr(),
    html.P('Estado mental atual:'),
    html.P(),
    dbc.Row([dbc.Col([dbc.Checklist(
                id='checklist_estado_mental',
                options=[
                    {'label': 'Delírio / Alucinação', 'value': 'Delírio / Alucinação'},
                    {'label': 'Depressão', 'value': 'Depressão'},
                    {'label': 'Desesperança', 'value': 'Desesperança'},
                    {'label': 'Desespero', 'value': 'Desespero'},
                    {'label': 'Colapso existencial', 'value': 'Colapso existencial'},
                    {'label': 'Incontinência afetiva', 'value': 'Incontinência afetiva'},
                    {'label': 'Instabilidade do humor', 'value': 'Instabilidade do humor'},
                    {'label': 'Ansiedade / Inquietude', 'value': 'Ansiedade / Inquietude'},
                    {'label': 'Impulsividade', 'value': 'Impulsividade'},
                    {'label': 'Raiva / Agressividade', 'value': 'Raiva / Agressividade'},
                    {'label': 'Constrição cognitiva', 'value': 'Constrição cognitiva'},
                    {'label': 'Vergonha', 'value': 'Vergonha'},
                    {'label': 'Insônia', 'value': 'Insônia'},
                    {'label': 'Dor / Incapacitação', 'value': 'Dor / Incapacitação'},
                    {'label': 'Torpor', 'value': 'Torpor'},],
                inline=True, style={'fontSize': '13px'}, value=''),]),]),
    html.P(),
    html.Small('Quais os 3 sintomas mais relevantes e o grau observado: '),
    html.P(),
    dbc.Row([
        dbc.Col([
            dbc.Input(id='ficha_entrada_sintoma1', type='text', placeholder='Principal sintoma...', size='sm', value=''),
            dcc.Slider(id='slider_escala_sintoma1',min=0,max=10,step=1,marks={i: str(i) for i in range(11)}, value=0),]),]),
    html.P(),
    dbc.Row([
        dbc.Col([
            dbc.Input(id='ficha_entrada_sintoma2', type='text', placeholder='Outro sintoma...', size='sm', value=''),
            dcc.Slider(id='slider_escala_sintoma2',min=0,max=10,step=1,marks={i: str(i) for i in range(11)}, value=0),]),]),
    html.P(),
    dbc.Row([
        dbc.Col([
            dbc.Input(id='ficha_entrada_sintoma3', type='text', placeholder='Outro sintoma...', size='sm', value=''),
            dcc.Slider(id='slider_escala_sintoma3',min=0,max=10,step=1,marks={i: str(i) for i in range(11)}, value=0),]),]),
    html.P(),
    html.Hr(),
    html.P('Intencionalidade suicida: '),
    html.P(),
    html.Small('Ideias suicidas:'),
    dbc.Row([dbc.Col([dbc.Checklist(
                id='checklist_ideias_suicidas',
                options=[
                    {'label': 'Passivas', 'value': 'Passivas'},
                    {'label': 'Fundamentadas', 'value': 'Fundamentadas'},
                    {'label': 'Persistentes', 'value': 'Persistentes'},
                    {'label': 'Intensas', 'value': 'Intensas'},
                    {'label': 'Incontroláveis', 'value': 'Incontroláveis'},
                    {'label': 'Forma de alívio', 'value': 'Forma de alívio'},
                    {'label': 'Irracionais', 'value': 'Irracionais'},],
                inline=True, style={'fontSize': '13px'}, value=''),]),]),
    html.P(),
    html.Small('Planos suicidas:'),
    dbc.Row([dbc.Col([dbc.Checklist(
                id='checklist_planos_suicidas',
                options=[
                    {'label': 'Em preparação', 'value': 'Em preparação'},
                    {'label': 'Detalhados', 'value': 'Detalhados'},
                    {'label': 'Consentidos', 'value': 'Consentidos'},
                    {'label': 'Providências', 'value': 'Providências'},],
                inline=True, style={'fontSize': '13px'}, value=''),]),]),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Observações:", style={'fontSize': '13px'}),
        dbc.Textarea(id='ficha_ideias_planos_obs', value=''), ], ), ]),
    html.P(),
    html.Hr(),
    html.P('Tentativa(s) prévia(s):'),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Quantas:", style={'fontSize': '13px'}),
        dbc.Input(id='ficha_tentativas_num', value=''), ], ), ]),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Última:", style={'fontSize': '13px'}),
        dbc.Input(id='ficha_tentativas_ultima', value=''), ], ), ]),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Motivação:", style={'fontSize': '13px'}),
        dbc.Input(id='ficha_tentativas_motivacao', value=''), ], ), ]),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Grau de letalidade:", style={'fontSize': '13px'}),
        dbc.Input(id='ficha_tentativas_letalidade', value=''), ], ), ]),
    html.P(),
    html.Hr(),
    html.P('Fatores de risco ou agravantes: '),
    html.P(),
    dbc.Row([dbc.Col([dbc.Checklist(
                id='checklist_fatores_risco',
                options=[
                    {'label': 'Transtorno mental constante', 'value': 'Transtorno mental constante'},
                    {'label': 'Perda de ente familiar', 'value': 'Perda de ente familiar'},
                    {'label': 'Abuso físico ou mental', 'value': 'Abuso físico ou mental'},
                    {'label': 'Desemprego', 'value': 'Desemprego'},
                    {'label': 'Tentativa de suicídio frustrada', 'value': 'Tentativa de suicídio frustrada'},
                    {'label': 'Discordância familiar', 'value': 'Discordância familiar'},
                    {'label': 'Uso de drogas', 'value': 'Uso de drogas'},
                    {'label': 'Desilusão amorosa', 'value': 'Desilusão amorosa'},
                    {'label': 'Ambiente de trabalho problemático', 'value': 'Ambiente de trabalho problemático'},
                    {'label': 'Relações profissionais conflituosas', 'value': 'Relações profissionais conflituosas'},
                    {'label': 'Dor crônica / Incapacitação', 'value': 'Dor crônica / Incapacitação'},
                    {'label': 'Derrocada financeira', 'value': 'Derrocada financeira'},
                    {'label': 'Frustração pessoal', 'value': 'Frustração pessoal'},],
                inline=True, style={'fontSize': '13px'}, value=''),]),]),
    html.P(),
    dbc.Row([dbc.InputGroup([
        dbc.InputGroupText("Outro(s):", style={'fontSize': '13px'}),
        dbc.Textarea(id='ficha_outros_fatores_risco', value=''), ], ), ]),
    html.P(),
    html.Hr(),
    html.P(),
    html.P('Formulação do risco e manejo:'),
    html.P(),
    dbc.Row([dbc.Col([
            dbc.RadioItems(id='ficha_grau_risco_manejo',
                options=[
                    {'label': 'Baixo', 'value': 'Baixo'},
                    {'label': 'Moderado', 'value': 'Moderado'},
                    {'label': 'Alto', 'value': 'Alto'},],
                inline=True, style={'fontSize': '13px'}, value=''),]),]),
    html.P(),
    dbc.Row([dbc.InputGroup([
                dbc.InputGroupText("Observações:", style={'fontSize': '13px'}),
                dbc.Textarea(id='ficha_grau_risco_obs', value=''),],),]),
    html.P(),
    html.Hr(),
    html.P(),
    html.P('Notas finais:'),
    html.P(),
    dbc.Row([dbc.InputGroup([
                dbc.InputGroupText("Observações:", style={'fontSize': '13px'}),
                dbc.Textarea(id='ficha_av_suicidio_notas_finais', rows=10, value=''),],),]),
    html.P(),
    dbc.Button("Salvar Ficha", id="botao_gerar_ficha_01", n_clicks=0, size='sm'),
    html.P(),
    html.Hr(),
    html.P(),
    html.Div(id='conteudo_ficha_av_risco_suicidio')
])
