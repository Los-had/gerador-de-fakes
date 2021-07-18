from random import choice, randint
import names
import string
import sqlite3
from sqlite3 import Error
import sys

try:
  conn = sqlite3.connect("dados.db")
  cursor = conn.cursor()
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    idade INTEGER NOT NULL
  );
  ''')
except Error:
  print(f'Erro! Código do erro : {Error.code}')
except:
  print("Um erro desconhecido aconteceu. Tente novamente")

def ver_dados():
  try:
    cursor.execute('''
    SELECT * FROM dados; 
    ''')
    for i in cursor.fetchall():
      print(f'[*]: {i}')
  except Error:
    print(f'Erro! Código do erro : {Error.code}')
  finally:
    conn.close()
    menu()
def gerar_dados():
  try:
    email = ''
    alfabeto = string.ascii_letters
    alfabeto += "1234567890"
    alfabeto += '!@#$%¨&*()_+`{}^?><,./~´[]=-§ªº°¹²³£¢¬|'
    servicos_de_email = ['@gmail.com', '@hotmail.com', '@outlook.com']
    escolha_de_servico_de_email = choice(servicos_de_email)
    nome = names.get_full_name()
    for i in range(10):
      email += choice(alfabeto)
    email += f'-{nome}'
    email += escolha_de_servico_de_email
    idade = randint(1, 100)
    print(f'''
    Nome: {nome}
    Idade: {idade}
    Email: {email}
    ''')
    try:
      cursor.execute(f'''
      INSERT INTO dados (nome, email, idade)
      VALUES ('{nome}', '{email}', {idade}) 
      ''')
      conn.commit()
      conn.close()
    except Error:
      print(f'Erro! Código do erro : {Error.code}')
    finally:
      conn.close()
      menu()
  except KeyboardInterrupt:
    menu()
def menu():
  try:
    print('=' * 50)
    print('''
    [1]. Gerar dados
    [2]. Sair
    [3]. Ver dados salvos
    ''')
    print('=' * 50)
    escolha = input(" >  ")
    if escolha == "1":
      gerar_dados()
    elif escolha == "3":
      ver_dados()
    elif escolha == "2":
      sys.exit()
    else:
      print(f'"{escolha}" é inválido.')
      menu()
  except KeyboardInterrupt:
    menu()
  except:
    print('Um erro desconhecido aconteceu :(')
    menu()
menu()