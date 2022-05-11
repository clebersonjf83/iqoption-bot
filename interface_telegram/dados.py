import sqlite3

def configurarBaseDeDados():
 #  con = sqlite3.connect("database.db")
  # cur = con.cursor()
   comando = "CREATE TABLE clientes ("
   comando += " id               INTEGER      PRIMARY KEY AUTOINCREMENT,"
   comando += " email            STRING (200),"
   comando += " senha            STRING (32),"
   comando += " status           BOOLEAN,"
   comando += " chat_id          STRING (64),"
   comando += " usuario_iqoption STRING (200),"
   comando += " senha_iqoption   STRING (64)) "
  
   comando = "INSERT INTO clientes (email,senha,status,chat_id,usuario_iqoption,senha_iqoption)"
   comando += "VALUES ('natanniel.alves@outlook.com','123456',1,null,'','')"
  # cur.execute(comando)
  # con.commit()
  # con.close()
   


# Verifica se o usuario existe algum chat iniciado
def verificarUsuarioTemChatLigado(chatID):
   con = sqlite3.connect('database.db')
   cur = con.cursor()
   existe = False
   for row in cur.execute("SELECT * FROM clientes where chat_id = '"+ str(chatID)+"' "):
      existe = True
   con.close()
   return existe

def verificaEmailExisteBaseDeDados(chatID, email):
   con = sqlite3.connect('database.db')
   cur = con.cursor()
   existe = False
   for row in cur.execute("SELECT * FROM clientes where email = '"+ email +"' "):
      existe = True
 #     cur.execute("update clientes set chat_id = '" + str(chatID) +"' where email = '" + email +"' ")
   con.close()
   return existe

def VinculaContaAoChatID(chatID, email):
   con = sqlite3.connect("database.db")
   cur = con.cursor()
  
   comando = "update clientes set chat_id = '"+ str(chatID)+"' where email = '"+email+"'"
   cur.execute(comando)
   con.commit()
   con.close()