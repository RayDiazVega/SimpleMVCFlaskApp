import sqlite3
from copy import deepcopy#Prototype
from flask import Flask, render_template, g, jsonify
import threading
import time

app = Flask(__name__)


DATABASE = "datos.db"#Nombre de la base de datos 

class db():
  
  _clon = "Falso"
  def __init__(self):
    self.DATABASE = "datos.db"#Nombre de la base de datos

  def get(self):
    self.database = getattr(g, '_database', None)
    if self.database is None:
      self.database = g._database = sqlite3.connect(self.DATABASE)
      self.database.row_factory = sqlite3.Row
    return self.database

  def query(self, query, args=(), one=False):
    cur = self.get().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    t = observador()
    t.start()
    return (rv[0] if rv else None) if one else rv

  def clone(self):#Metodo que crea una copia del original
    self._clon = "Verdadero"
    return deepcopy(self)

class observador(threading.Thread):
   def run(self):
      print ("mirando json")
      for i in range(1,5):
        self.i = i
        time.sleep(2)
      print ("sigue mirando")

DBlist = db()#Objeto dedicado a la lista
DBapi = DBlist.clone()#Copia del objeto lista dedicado a la api

@app.teardown_appcontext
def close_connection(exception):
    database = getattr(g, '_database', None)
    if database is not None:
        database.close()

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users/list')
def users():
  users_list = DBlist.query("SELECT * FROM users")
  return render_template("users.html", users_list=users_list)

@app.route('/api/v1/users/')
def api():
  users_list = DBapi.query("SELECT * FROM users")
  d = {}
  for i, f, l, u, m, p in users_list: d[i] = {"firstname": f, "lastname": l, "username": u, "mail": m, "password": p}
  return jsonify(d)

if __name__== '__main__':
    app.run(debug = True, host='0.0.0.0', port=80)

		
