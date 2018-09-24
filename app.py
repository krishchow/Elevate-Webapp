from flask import Flask, jsonify, abort, request, render_template
import sqlite3
import csv
import random, string


app = Flask(__name__)

@app.route('/')
def index():
    keyData = list(open('cfg.txt','r'))
    keyData = keyData[0]
    keyData = 'https://maps.googleapis.com/maps/api/js?key={0}&callback=myMap'.format(keyData)
    conn = sqlite3.connect(r'data.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('SELECT * FROM locations WHERE category="Library";')
    dat= cur.fetchall()
    return render_template('index.html', data=dat,URLKEY=keyData)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def isAdmin(row):
    if int(list(row)[2]) == 2:
        return True

def verifyKey(key):
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth WHERE key="{0}";'.format(key))
    row = cur.fetchone()
    if row == None:
        return 0
    if isAdmin(row):
        return 2
    return 1


def initAuthTable():
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS auth (username, key, level);')
    conn.commit()
    conn.close()

@app.route('/login', methods=['GET','POST'])
def addNewAuth():
    initAuthTable()
    username = request.args.get('user')
    level = request.args.get('level')
    stat = verifyKey(request.args.get('key'))
    if stat < 2:
        return abort(401)
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth WHERE username="{0}";'.format(username))
    if cur.fetchone():
        return abort(409)

    key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))
    cur.execute('INSERT INTO auth VALUES ("{0}", "{1}", "{2}");'.format(username, key, level))
    conn.commit()
    conn.close()
    return jsonify({'username':username, 'key':key, 'level':level})

@app.route('/poke/<id>')
def getMon(id):
    auth = request.args.get('key')
    print(auth)
    if not verifyKey(auth):
        return abort(401)

    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
    cur.execute('SELECT * from poke WHERE Id="{0}";'.format(id))
    row = cur.fetchone()
    if row == None:
        return abort(404)
    return jsonify(list(row))

if __name__ == '__main__':
    app.run(debug=True)
    conn = sqlite3.connect(r'data.db')
    cur = conn.cursor()
