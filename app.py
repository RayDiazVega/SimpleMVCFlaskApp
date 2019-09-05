import sqlite3
from flask import Flask, render_template, g, jsonify

app = Flask(__name__)

DATABASE = "datos.db"#Nombre de la base de datos 

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users/list')
def users():
  users_list = query_db("SELECT * FROM users")
  return render_template("users.html", users_list=users_list)

@app.route('/api/v1/users/')
def api():
  users_list = query_db("SELECT * FROM users")
  d = {}
  for i, f, l, u, m, p in users_list: d[i] = {"firstname": f, "lastname": l, "username": u, "mail": m, "password": p}
  return jsonify(d)

if __name__== '__main__':
    app.run(debug = True, port=80, host='0.0.0.0')
