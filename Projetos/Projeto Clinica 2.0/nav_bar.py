from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify

layout_nav_bar = dbc.Nav([
        html.Hr(),
        dbc.NavItem([
             dbc.NavLink([dbc.Row([
                 dbc.Col(DashIconify(icon="healthicons:ambulatory-clinic-outline", width=50), width=3),
                 dbc.Col(html.H5("Sistema Clínica"), width=9, className="align-items-center")])], href="/dashboard")]),
        html.Div([dbc.Input(id='palavra_chave_input', value='', placeholder='Pesquisar')]),
        html.Hr(),
        dbc.NavItem([
             dbc.NavLink([dbc.Row([
                 dbc.Col(DashIconify(icon="healthicons:chart-bar-stacked", width=25), width=2),
                 dbc.Col('Dashboard')])], href="/dashboard", active='exact')], id="pagina_dashboard"),
        dbc.NavItem([
            dbc.NavLink([dbc.Row([
                            dbc.Col(DashIconify(icon="carbon:user-follow", width=25), width=2),
                            dbc.Col('Cadastro')])], href="/cadastro", active='exact')], id="pagina_cadastro"),
        dbc.NavItem([
            dbc.NavLink([dbc.Row([
                            dbc.Col(DashIconify(icon="healthicons:calendar-outline", width=25), width=2),
                            dbc.Col('Agendamento')])], href="/agenda", active='exact')], id="pagina_agenda"),
        html.Hr(),
        dbc.NavItem([
            dbc.NavLink([dbc.Row([
                            dbc.Col(DashIconify(icon="healthicons:health-worker-form-outline", width=25), width=2),
                            dbc.Col('Anamnese')])], href="/anamnese", active='exact')], id="pagina_anamnese"),
         dbc.NavItem([
             dbc.NavLink([dbc.Row([
                 dbc.Col(DashIconify(icon="solar:health-broken", width=25), width=2),
                 dbc.Col('Consulta')])], href="/consulta", active='exact')], id="pagina_consulta"),
        dbc.NavItem([
             dbc.NavLink([dbc.Row([
                 dbc.Col(DashIconify(icon="fluent:briefcase-medical-32-regular", width=25), width=2),
                 dbc.Col('Ferramentas')])], href="/ferramentas", active='exact')], id="pagina_ferramentas"),
        html.Hr(),
        dbc.NavItem([
            dbc.NavLink([dbc.Row([
                            dbc.Col(DashIconify(icon="medical-icon:i-medical-records", width=25), width=2),
                            dbc.Col('Prontuários')])], href="/prontuarios", active='exact')], id="pagina_prontuarios"),
        html.Hr(),
        dbc.NavItem([
            dbc.NavLink([dbc.Row([
                            dbc.Col(DashIconify(icon="healthicons:health-data-security", width=25), width=2),
                            dbc.Col('Documentos')])], href="/documentos", active='exact')], id="pagina_documentos"),
        dbc.NavItem([
             dbc.NavLink([dbc.Row([
                 dbc.Col(DashIconify(icon="healthicons:health-literacy-outline", width=25), width=2),
                 dbc.Col('Materiais de Apoio')])], href="/materiais", active='exact')], id="pagina_materiais"),
        html.Hr(),
        dbc.NavItem([
            dbc.NavLink([dbc.Row([
                            dbc.Col(DashIconify(icon="healthicons:city-worker-outline", width=25), width=2),
                            dbc.Col('Administrativo')])], href="/admin", active='exact')], id="pagina_administrativo"),

    ], vertical=True, pills=True)
