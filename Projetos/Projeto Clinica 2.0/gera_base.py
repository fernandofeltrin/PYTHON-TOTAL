import os
import sqlite3
import pandas as pd
from datetime import datetime

def gera_base():
    timestamp = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    _ = 'base.db'
    if os.path.exists(_):
        print(f'Base de dados "base.db" carregada com sucesso. - {timestamp}')
    else:
        conexao = sqlite3.connect('base.db')
        print(f'Base de dados "base.db" criada com sucesso. - {timestamp}')
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT,
                'Data de Nascimento' TEXT,
                Sexo TEXT,
                Identidade TEXT,
                CPF TEXT,
                Nacionalidade TEXT,
                'Estado Civil' TEXT,
                'Grau de Instrução' TEXT,
                Profissão TEXT,
                Religião TEXT,
                Logradouro TEXT,
                Telefone TEXT,
                Email TEXT,
                Foto BLOB,
                Anexos BLOB,
                'Cadastro Observações' TEXT,
                'Registro Consultas' TEXT,
                Anamneses BLOB,
                Atestados BLOB,
                'Cartas Termos' BLOB,
                Contratos BLOB,
                Declarações BLOB,
                Encaminhamentos BLOB,
                'Fichas de Avaliação' BLOB,
                'Fichas de Evolução' BLOB,
                'Laudos Pareceres' BLOB,
                Prescrições BLOB,
                Recibos BLOB,
                'Testes Psicométricos' BLOB,
                'Outros Arquivos' BLOB)
                    """)
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM Pacientes WHERE id = 1 AND Nome = 'Paciente Teste'")
        resultado = cursor.fetchone()
        if resultado:
            pass
        else:
            cursor.execute("INSERT INTO Pacientes (Nome, 'Cadastro Observações') VALUES (?, ?)", ('Paciente Teste', 'Nada informado',))
            conexao.commit()
        print(f'Tabela "Pacientes" criada com sucesso. - {timestamp}')
        print(f'Paciente Teste cadastrado com sucesso. - {timestamp}')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Agenda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT,
                Profissional TEXT,
                'Escopo de Atuação' TEXT,
                'Frequência Semanal' TEXT,
                'Horas Semanais' TEXT,
                Convênio TEXT,
                Ano TEXT,
                Mês TEXT,
                'Dia do Mês' TEXT,
                'Dia da Semana' TEXT,
                'Horário' TEXT,
                'Agendamento Observações' TEXT,
                'Número de Consultas' INTEGER,
                'Histórico de Consultas' TEXT)
                    """)
        cursor.execute("SELECT id FROM Agenda WHERE id = 1 AND Nome = 'Paciente Teste'")
        resultado2 = cursor.fetchone()
        if resultado2:
            pass
        else:
            cursor.execute("INSERT INTO Agenda (Nome, 'Agendamento Observações') VALUES (?, ?)", ('Paciente Teste', 'Nada consta'))
            conexao.commit()
            print(f'Tabela "Agenda" criada com sucesso. - {timestamp}')
            print(f'Consulta Teste agendada com sucesso. - {timestamp}')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Consulta (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT,
                'Queixa Principal' TEXT,
                'Queixa Secundária' TEXT,
                Sintomas TEXT,
                Comorbidades TEXT,
                'Objetivos Terapêuticos' TEXT,
                'Início da Patologia' TEXT,
                'Frequência da Patologia' TEXT,
                'Intensidade da Patologia' TEXT,
                'Tratamentos Anteriores' TEXT,
                'Uso de Medicamentos' TEXT,
                'Histórico Infância' TEXT,
                'Histórico Rotina' TEXT,
                'Histórico Alimentar' TEXT,
                'Histórico Sono' TEXT,
                'Histórico Vícios' TEXT,
                'Histórico Cirurgias' TEXT,
                'Histórico Hobbies' TEXT,
                'Histórico Trabalho' TEXT,
                'Histórico Pais' TEXT,
                'Histórico Irmãos' TEXT,
                'Histórico Cônjuge' TEXT,
                'Histórico Filhos' TEXT,
                'Histórico Lar' TEXT,
                'Transtornos Mentais na Família' TEXT,
                'Planos Futuros' TEXT,
                'Exame Aparência' TEXT,
                'Exame Comportamento' TEXT,  
                'Exame Postura' TEXT,
                'Exame Orientação' TEXT,
                'Exame Atenção' TEXT,
                'Exame Memória' TEXT,
                'Exame Inteligência' TEXT,
                'Exame Senso' TEXT,
                'Exame Distorções Cognitivas' TEXT,
                'Exame Humor' TEXT,
                'Exame Pensamentos' TEXT,
                'Exame Conteúdo' TEXT,
                'Exame Expansão' TEXT,
                'Exame Retração' TEXT,
                'Exame Negação' TEXT,
                'Exame Linguagem' TEXT,
                'Exame Consciência' TEXT,
                'Comentários Exame' TEXT,
                'Hipótese Diagnóstica' TEXT,
                Evolução TEXT,
                Anotações TEXT,
                'CID DSM' TEXT)
                    """)
        cursor.execute("SELECT id FROM Consulta WHERE id = 1 AND Nome = 'Paciente Teste'")
        resultado3 = cursor.fetchone()
        if resultado3:
            pass
        else:
            cursor.execute("INSERT INTO Consulta (Nome, Anotações) VALUES (?, ?)", ('Paciente Teste', 'Nada informado'))
            conexao.commit()
            print(f'Tabela "Consulta" criada com sucesso. - {timestamp}')
            print(f'Demais dados cadastrados com sucesso. - {timestamp}')
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Colaboradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Nome TEXT,
                Telefone TEXT,
                Especialidade TEXT,
                'Registro Profissional' TEXT,
                'Observações Colaborador' TEXT)
                    """)
        cursor.execute("SELECT id FROM Colaboradores WHERE id = 1 AND Nome = 'Colaborador Teste'")
        resultado4 = cursor.fetchone()
        if resultado4:
            pass
        else:
            cursor.execute("INSERT INTO Colaboradores (Nome, 'Observações Colaborador') VALUES (?, ?)", ('Colaborador Teste', 'Nada informado'))
            conexao.commit()
            print(f'Tabela "Colaboradores" criada com sucesso. - {timestamp}')
            print(f'Colaborador Teste cadastrado com sucesso. - {timestamp}')
        conexao.commit()
        conexao.close()

def carrega_bases():
    conexao = sqlite3.connect('base.db')
    df = pd.read_sql('SELECT * FROM Pacientes', conexao)
    df = df.fillna('')
    df_agenda = pd.read_sql('SELECT * FROM Agenda', conexao)
    df_agenda = df_agenda.fillna('')
    df_consulta = pd.read_sql('SELECT * FROM Consulta', conexao)
    df_consulta = df_consulta.fillna('')
    cursor = conexao.cursor()
    cursor.execute("SELECT id, Nome FROM Pacientes")
    resultado = cursor.fetchall()
    nomes = {id: nome for id, nome in resultado}
    cursor.execute("SELECT id, Nome FROM Colaboradores")
    resultado2 = cursor.fetchall()
    colaboradores = {id: nome for id, nome in resultado2}
    conexao.close()
    return df, df_agenda, df_consulta, nomes, colaboradores

