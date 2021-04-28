import sqlite3

def contatoData():
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Contato (id INTEGER PRIMARY KEY, CntID text, Nome text, Sobrenome text, Email text, Telefone text, Idade text, Cpf text, Sexo text)")
    con.commit()
    con.close()

def AddContato(CntID, Nome, Sobrenome, Email, Telefone, Idade, Cpf, Sexo) :
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Contato VALUES (NULL, ?,?,?,?,?,?,?,?)",(CntID, Nome, Sobrenome, Email, Telefone, Idade, Cpf, Sexo))
    con.commit()
    con.close()

def view() :
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Contato")
    rows = cur.fetchall()
    con.close()
    return rows

def deletar(id):
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Contato WHERE id=?", (id,))
    con.commit()
    con.close()

def busca(CntID ="", Nome = "", Sobrenome = "", Email = "", Telefone = "", Idade = "", Cpf = "", Sexo = ""):
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM Contato WHERE CntID=? or Nome=? or Sobrenome=? or Email=? or Telefone=? or Idade=? or Cpf=? or Sexo=?", (CntID, Nome, Sobrenome, Email, Telefone, Idade, Cpf, Sexo))
    rows = cur.fetchall()
    con.close()
    return rows

def update(id, CntID ="", Nome = "", Sobrenome = "", Email = "", Telefone = "", Idade = "", Cpf = "", Sexo = ""):
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    cur.execute("UPDATE Contato SET CntID=? or Nome=? or Sobrenome=? or Email=? or Telefone=? or Idade=? or Cpf=? or Sexo=?", (CntID, Nome, Sobrenome, Email, Telefone, Idade, Cpf, Sexo, id))
    con.commit()
    con.close()



contatoData()