from dash import html, dcc
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_anamnese_conv_inicial = html.Div([
    html.P('Selecione um paciente:'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else ''),
    html.P(id='valor_selecionado'),
    html.P(),
    dbc.Row([
        dbc.Label('Queixa Principal: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'queixa_principal', value=''), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Queixa Secundária: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'queixa_secundaria', value=''), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Sintomas Gerais: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'sintomas', value=''), width = 10)]),
    html.P(),
    html.Hr(),
    dbc.Row([
        dbc.Label('Comorbidades: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'comorbidades', value=''), width = 10)]),
    html.P(),
    html.Hr(),
    dbc.Row([
        dbc.Label('Objetivos Terapêuticos: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'obj_terapeuticos', value=''), width = 10)]),
    html.P(),
    html.Hr(),
    dbc.Row([
        dbc.Col([dbc.Button('Atualizar Prontuário', size="sm",
                            id='botao_salvar_atendimento'),]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([dbc.Button('Apagar Registros', size="sm", color="danger",
                            id='botao_apagar_atendimento')])]),
    html.P(),
    html.Div(id = 'saida_formulario_atendimento')
])

layout_historico_clinico = html.Div([
    html.P('Selecione um paciente'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else ''),
    html.P(id='valor_selecionado'),
    html.P(),
    html.H6('Histórico Patológico'),
    dbc.Row([
        dbc.Label('Início da Patologia: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id = 'inicio_patologia', type='text'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Frequência: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='frequencia_patologia', type='text'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Intensidade: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='intensidade_patologia', type='text'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Tratamentos Anteriores: ', width=2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='tratamentos_anteriores', type='text'), width=10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Uso de Medicamentos: ', width=2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id='uso_medicamentos', type='text'), width=10)]),
    html.P(),
    html.Hr(),
    html.H6('Histórico Pessoal'),
    dbc.Row([
        dbc.Label('Infância: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_infancia'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Rotina: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_rotina'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Alimentar: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_alimentar'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Sono: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_sono'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Vícios: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_vicios'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Cirurgias: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_cirurgias'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Hobbies: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_hobbies'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Trabalho: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_trabalho'), width = 10)]),
    html.P(),
    html.Hr(),
    html.H6('Histórico Familiar'),
    dbc.Row([
        dbc.Label('Pais: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_pais'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Irmão(s): ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_irmaos'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Cônjuge: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_conjuge'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Filhos: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_filhos'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Lar: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_lar'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Label('Transtornos mentais na família: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'historico_transtornos_familia'), width = 10)]),
    html.P(),
    html.Br(),
    dbc.Row([
        dbc.Col([dbc.Button('Atualizar Prontuário', size="sm", id='botao_salvar_historico'),]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([]),
        dbc.Col([dbc.Button('Apagar Registros', size="sm", color="danger", id='botao_apagar_historico')])]),
    html.Div(id = 'saida_formulario_historico')
])

layout_exame_psiquico = html.Div([
    html.P('Selecione um paciente'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else ''),
    html.P(id='valor_selecionado'),
    html.P(),
    dbc.Row([
        dbc.Label('Aparência geral: ', width = 2, style={'fontSize': '14px'}, id = 'txt_ap_geral'),
        dbc.Col(dbc.Textarea(id = 'exame_aparencia', value=''), width = 10, style={'fontSize': '14px'}),
        dbc.Tooltip("Se possível, descreva a aparência geral do paciente em sua primeira impressão. Vestimenta, autocuidado, semblante, etc...", target="txt_ap_geral")]),
    html.P(),
    dbc.Row([
        dbc.Label('Comportamento: ', width = 2, style={'fontSize': '14px'}, id='txt_comportamento'),
        dbc.Col(dbc.Textarea(id = 'exame_comportamento', value=''), width = 10, style={'fontSize': '14px'}),
        dbc.Tooltip("Se possível, identifique e descreva sua maneira geral de se portar.", target="txt_comportamento")]),
    html.P(),
    dbc.Row([
        dbc.Label('Postura: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(id='exame_postura', options=[
                    {'label': 'Cooperativo', 'value': 'Cooperativo'},
                    {'label': 'Resistente', 'value': 'Resistente'},
                    {'label': 'Indiferente', 'value': 'Indiferente'}], value='', inline = True)], width=10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Orientação: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(id='exame_orientacao', options=[
                    {'label': 'Autoidentificatória', 'value': 'Autoidentificatória'},
                    {'label': 'Corporal', 'value': 'Corporal'},
                    {'label': 'Temporal', 'value': 'Temporal'},
                    {'label': 'Espacial', 'value': 'Espacial'},
                    {'label': 'Orientada à patologia', 'value': 'Orientada à patologia'}], value='', inline = True)], width=10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Atenção: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'exame_atencao', value = ''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Memória: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'exame_memoria', value = ''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Inteligência: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'exame_inteligencia', value = ''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Senso percepção: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(id='exame_senso', options=[
                    {'label': 'Normal', 'value': 'Normal'},
                    {'label': 'Alucinatório', 'value': 'Alucinatório'}], value='', inline = True)], width=10, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Distorções Cognitivas: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='exame_distorcoes_cognitivas',
                options=[
                    {'label': 'Não se aplica', 'value': 'Não se aplica'},
                    {'label': 'Catastrofização', 'value': 'Catastrofização'},
                    {'label': 'Leitura mental', 'value': 'Leitura Mental'},
                    {'label': 'Filtro mental negativo', 'value': 'Filtro mental negativo'},
                    {'label': 'Raciocínio emocional', 'value': 'Raciocínio emocional'},
                    {'label': 'Supergeneralização', 'value': 'Supergeneralização'},
                    {'label': 'Auto julgamento evasivo', 'value': 'Auto julgamento evasivo'},
                    {'label': 'Pensamento dicotômico', 'value': 'Pensamento dicotômico'},
                    {'label': 'Auto rotulação negativa', 'value': 'Auto rotulação negativa'},
                    {'label': 'Personalização', 'value': 'Personalização'},
                    {'label': 'Desqualificação', 'value': 'Desqualificação'},
                    {'label': 'Culpabilização', 'value': 'Culpabilização'},
                    {'label': 'Tendência à lamentação', 'value': 'Tendência à lamentação'},
                    {'label': 'Incapacidade de refutação', 'value': 'Incapacidade de refutação'},
                    {'label': 'Foco no julgamento alheio', 'value': 'Foco no julgamento alheio'},
                ], value = [], inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Humor: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(
                id='exame_humor',
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
                id='exame_pensamento',
                options=[
                    {'label': 'Acelerado', 'value': 'Acelerado'},
                    {'label': 'Retardado', 'value': 'Retardado'},
                    {'label': 'Fuga', 'value': 'Fuga'},
                    {'label': 'Bloqueio', 'value': 'Bloqueio'},
                    {'label': 'Prolixo', 'value': 'Prolixo'},
                    {'label': 'Repetição', 'value': 'Repetição'},
                    {'label': 'Outro tipo', 'value': 'Outro tipo'}
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
                id='exame_conteudo',
                options=[
                    {'label': 'Obsessões', 'value': 'Obsessões'},
                    {'label': 'Hipocondrias', 'value': 'Hipocondrias'},
                    {'label': 'Fobias', 'value': 'Fobias'},
                    {'label': 'Delírios', 'value': 'Delírios'},
                    {'label': 'Outros', 'value': 'Outros'},
                ], value = [], inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Expansão do Eu: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='exame_expansao_eu',
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
                ], value = [], inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Retração do Eu: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='exame_retracao_eu',
                options=[
                    {'label': 'Prejuízo', 'value': 'Prejuízo'},
                    {'label': 'Vitimização', 'value': 'Vitimização'},
                    {'label': 'Auto referência', 'value': 'Auto referência'},
                    {'label': 'Perseguição', 'value': 'Perseguição'},
                    {'label': 'Influência', 'value': 'Influência'},
                    {'label': 'Possessão', 'value': 'Possessão'},
                    {'label': 'Humildades', 'value': 'Humildades'},
                    {'label': 'Outros', 'value': 'Outros'},
                ], value = [], inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Negação do Eu: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='exame_negacao_eu',
                options=[
                    {'label': 'Negação', 'value': 'Negação'},
                    {'label': 'Desprezo', 'value': 'Desprezo'},
                    {'label': 'Autoacusação', 'value': 'Autoacusação'},
                    {'label': 'Culpa', 'value': 'Culpa'},
                    {'label': 'Ruína', 'value': 'Ruína'},
                    {'label': 'Niilismo', 'value': 'Niilismo'},
                    {'label': 'Tendência suicida', 'value': 'Tendência suicida'},
                    {'label': 'Outros', 'value': 'Outros'},
                ], value = [], inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Linguagem: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.Checklist(
                id='exame_linguagem',
                options=[
                    {'label': 'Disartrias', 'value': 'Disartrias'},
                    {'label': 'Afasias', 'value': 'Afasias'},
                    {'label': 'Parafasias', 'value': 'Parafasias'},
                    {'label': 'Neologismo', 'value': 'Neologismo'},
                    {'label': 'Mussitação', 'value': 'Mussitação'},
                    {'label': 'Logorréia', 'value': 'Logorréia'},
                    {'label': 'Para-respostas', 'value': 'Para-respostas'},
                ], value = [], inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Consciência da condição atual: ', width=2, style={'fontSize': '14px'}),
        dbc.Col([
            dbc.RadioItems(
                id='exame_consciencia',
                options=[
                    {'label': 'Sim', 'value': 'Sim'},
                    {'label': 'Não', 'value': 'Não'},
                    {'label': 'Parcial', 'value': 'Parcial'},
                ], value = '', inline = True
            ),
        ], width=10, style={'fontSize': '14px'})
    ]),
    html.P(),
    dbc.Row([
        dbc.Label('Comentarios: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'exame_comentarios', value=''), width = 10, style={'fontSize': '14px'})]),
    html.P(),
    html.Br(),
    dbc.Button('Atualizar Prontuário', size = 'sm', id='botao_salvar_exame_psiquico'),
    html.Hr(),
    html.Div(id = 'saida_formulario_exame')
])

layout_anotacoes_anamnese = html.Div([
    html.P('Selecione um paciente:'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else ''),
    html.P(id='valor_selecionado'),
    html.P(),
    dbc.Row([
        dbc.Label('Anotações: ', width = 2, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'texto_anotacoes_anamnese', rows=10, placeholder='Digite suas anotações aqui...'), width = 10)]),
    html.P(),
    dbc.Row([
        dbc.Col([dbc.Button('Atualizar Prontuário', size="sm", id='botao_salvar_anot_anamnese'),]),
        dbc.Col([dbc.Button('Apagar Registros', size="sm", color="danger", id='botao_apagar_anot_anamnese')])]),
    html.P(),
    html.Div(id = 'saida_anotacoes_anamnese')
])

layout_hipotese_diagnostica = html.Div([
    html.P('Selecione um paciente:'),
    dcc.Dropdown(
        id='menu_selecao_paciente',
        options=[{'label': label, 'value': value} for value, label in nomes.items()],
        value=list(nomes.keys())[0] if nomes else None
    ),
    html.P(id='valor_selecionado'),
    html.P(),
    dbc.Row([
        dbc.Label('Descrição: ', width = 1, style={'fontSize': '14px'}),
        dbc.Col(dbc.Textarea(id = 'texto_hipotese_diagnostica', value = ''), width = 11, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Row([
        dbc.Label('Código CID-11 / DSM-5-TR: ', width = 3, style={'fontSize': '14px'}),
        dbc.Col(dbc.Input(id = 'cid_dsm', type='text'), width = 9, style={'fontSize': '14px'})]),
    html.P(),
    dbc.Button('Salvar', id='botao_salvar_hipotese_diagnostica'),
    html.Div(id = 'saida_formulario_hipotese_diagnostica')
])
