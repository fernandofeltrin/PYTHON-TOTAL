from dash import html, dcc
import dash_bootstrap_components as dbc

from gera_base import carrega_bases
df, df_agenda, df_consulta, nomes, colaboradores = carrega_bases()

layout_cadastro = dbc.Container([dbc.Row([
        dbc.Row(html.Div([html.Hr(),
                         html.H5('Cadastro de Paciente')])),
        dbc.Row(html.Div([
        dbc.Row([
            dbc.Label('Nome Completo: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='nome', type='text'), width = 10)]),
        html.P(),
        dbc.Row([
            dbc.Label('Data de Nascimento: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='data_nascimento', type='text', value=''), width = 4),
            dbc.Label('Orientação Sexual: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.RadioItems(options=[
                {"label": "Masculino", "value": 'Masculino'},
                {"label": "Feminino", "value": 'Feminino'},
                {"label": "Outro", "value": 'Outro'},],
                id="sexo", value='', inline=True, style={'fontSize': '14px'}),
            width = 4),
            html.Div(id='cad_checklist_selecionado')]),
        html.P(),
        dbc.Row([
            dbc.Label('Identidade: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='identidade', type='text', value=''), width = 4),
            dbc.Label('CPF: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='cpf', type='text', value=''), width = 4)]),
        html.P(),
        dbc.Row([
            dbc.Label('Nacionalidade: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='nacionalidade', type='text', value=''), width = 4),
            dbc.Label('Estado Civil: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='estado_civil', type='text', value=''), width = 4)]),
        html.P(),
        dbc.Row([
            dbc.Label('Grau de Instrução: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='grau_instrucao', type='text', value=''), width = 4),
            dbc.Label('Profissão: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='profissao', type='text', value=''), width = 4)]),
        html.P(),
        dbc.Row([
            dbc.Label('Religião: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='religiao', type='text', value=''), width = 4)]),
        html.P(),
        dbc.Row([
            dbc.Label('Logradouro: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='logradouro', type='text', value=''), width = 4),
            dbc.Label('Telefone: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='telefone', type='text', value='', placeholder='(XX) XXXXX-XXXX'), width = 4)]),
        html.P(),
        dbc.Row([
            dbc.Label('E-mail: ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dbc.Input(id='email', type='text', placeholder='xxxxxxxx@xxxxx.xxx', value=''), width = 4),
            dbc.Label('Fotografia (opcional): ', width = 2, style={'fontSize': '14px'}),
            dbc.Col(dcc.Upload(id='foto', children=dbc.Button('Carregar Foto', size="sm"), multiple=False), width = 4)]),
        html.P(),
        html.Hr(),
        dbc.Row([
                dbc.Label('Observações: ', width=2, style={'fontSize': '14px'}),
                dbc.Textarea(id='observacoes_cadastro', value='')]),
        html.P(),
        dbc.Row([dbc.Col(dbc.Button('Cadastrar', id='botao_cadastrar_paciente', n_clicks=0), className="d-grid gap-2 col-2 mx-auto")]),
        html.Div(id = 'saida_formulario_cadastro')])),
        html.P(),
        html.Hr(),
        dbc.Row()])])
