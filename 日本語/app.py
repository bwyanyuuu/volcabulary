from flask import Flask, render_template, request, redirect, url_for, jsonify
import os, random
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from nihonngo import *

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

current_result = None
current_word = None
current_list = None
current_wordList = None
select_list = None

import socket

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

@app.route("/")
def index():
    # db.create_all()
    return redirect(url_for('search'))

@app.route("/search", methods=["GET", "POST"])
def search():
    
    ip = get_host_ip()
    
    if request.method == "POST":
        print(request.values)
        
        if request.values['action'] == "newList":
            try:
                newList = WordList(request.values["list"])
                db.session.add(newList)
                db.session.commit() 
            except:
                pass
        elif request.values['action'] == 'search' and request.values['word']:
            return jsonify({'result': analyzeWords(getWords(request.values['word']))})
    return render_template("search.html", ip=ip)

@app.route("/search_result", methods=["GET","POST"])
def search_result():
    global select_list, current_result, current_word
    if request.method == "GET":
        li = WordList.query.all()
        id = request.args.get('id')
        if id:
            spell, pron, current_result = analyzeTheWord(getTheWord(id))
            hira = hiragana(spell)
            current_word = [spell, pron, hira]
        return render_template("search_result.html", hira=hira, spell=spell, pron=pron, result=current_result, list=li, select_list=select_list)
    elif request.method == "POST":
        li = [int(i) for i in request.form.getlist('idx')]
        explain = request.form.getlist('new-mean')
        cixing = request.form.getlist('new-cixing')
        select_result = [current_result[i] for i in li] + ([[cixing[i], explain[i]] for i in range(len(explain))] if len(cixing) > 0 else [])
        for s in select_result:
            if s[0] == '' or s[1] == '':
                continue
            new_word = Word(current_word[0], current_word[1], current_word[2], s[0], s[1], None, request.values["list"])
            # print(new_word)
            db.session.add(new_word)
        db.session.commit()
        select_list = request.values["list"]
        return redirect(url_for('search'))
    # if request.values['action'] == 'search' and request.values['word']:
    #     global current_result
    #     current_result = getWords(request.values['word'])
    #     li = WordList.query.all()
    #     return render_template("search_result.html", word=word, result=current_result, list=li, select_list=select_list)
    # else:
    #     return redirect(url_for('search'))

@app.route("/test", methods=["GET", "POST"])
def test():
    global current_list
    if request.method == "GET":
        global current_wordList
        current_list = []
        for w in current_wordList:
            current_list += list(Word.query.filter_by(listName=w))
        print(current_list, current_wordList)
    elif request.method == "POST":
        if request.values["action"] == "success":
            current_list.remove(current_list[int(request.values["idx"])])
    if len(current_list) == 0:
        return redirect(url_for('search'))
    else:
        idx = random.randint(0, len(current_list) -1)
        word = current_list[idx]
        return render_template("test.html", word=word, idx=idx)

@app.route("/memory", methods=["GET", "POST"])
def memory():
    global current_list
    if request.method == "GET":
        global current_wordList
        current_list = []
        for w in current_wordList:
            current_list += list(Word.query.filter_by(listName=w))
        idx = 0
    elif request.method == "POST":
        idx = (int(request.values["idx"]) + 1) % len(current_list)
    
    word = current_list[idx]
    return render_template("memory.html", word=word, idx=idx)

@app.route("/select", methods=["GET", "POST"])
def select():
    if request.method == "GET":
        li = WordList.query.all()
        return render_template("select.html", list=li)
    elif request.method == "POST":
        global current_wordList
        current_wordList = request.form.getlist('list')
        if request.values["action"] == "test":
            return redirect(url_for('test'))
        elif request.values["action"] == "memory":
            return redirect(url_for('memory'))
    #         current_list.remove(current_list[int(request.values["idx"])])
    # if len(current_list) == 0:
    #     return redirect(url_for('view'))
    # else:
    #     idx = random.randint(0, len(current_list) -1)
    #     word = current_list[idx]
    #     return render_template("test.html", word=word, idx=idx)

@app.route("/view", methods=["GET", "POST"])
def view():
    select_list = "all"
    word = None
    isEditing = False
    print(request.values)
    if request.method == "GET":
        word = Word.query.all()
        # print(word[0]['name'])
    elif request.method == "POST":
        if request.values["action"] == "list":
            word, select_list = getList(request.values["list"])
        elif request.values["action"] == "add":
            word = request.form.getlist('new-word')
            cixing = request.form.getlist('new-cixing')
            explain = request.form.getlist('new-explain')
            for i in range(len(word)):
                newWord = Word(word[i], cixing[i], explain[i], request.values['list'])
                db.session.add(newWord)
            db.session.commit()
            word, select_list = getList(request.values["list"])
            isEditing = True
        elif request.values["action"] == "modify":
            i = int(request.values['idx'])
            Word.query.filter_by(id=i).update({'word': request.values['word'], 'cixing': request.values['cixing'], 'explain': request.values['explain']})
            db.session.commit()
            word, select_list = getList(request.values["list"])
            isEditing = True
        elif request.values["action"] == "delete":
            li = [int(i) for i in request.form.getlist('idx')]
            for i in li:
                Word.query.filter_by(id=i).delete()
            db.session.commit()
            word, select_list = getList(request.values["list"])
            isEditing = True
        elif request.values["action"] == "deleteList":
            name = request.values['list']
            Word.query.filter_by(listName=name).delete()
            WordList.query.filter_by(name=name).delete()
            db.session.commit()
            word, select_list = getList("all")
    li = WordList.query.all()
    return render_template("view.html", word=word, list=li, select_list=select_list, isEditing=isEditing)

def getList(name):
    if name == "all":
        word = Word.query.all()
        select_list = "all"
    elif name:
        word = Word.query.filter_by(listName=name)
        select_list = name
    return word, select_list

db = SQLAlchemy(app)
# 模型( model )定義
class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pron = db.Column(db.String(20), nullable=False)
    hiragana = db.Column(db.String(100), nullable=False)
    cixing = db.Column(db.String(30), nullable=False)
    explain = db.Column(db.String(100), nullable=False)
    explain_jp = db.Column(db.String(100))
    listName = db.Column(db.String(30), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)
 
    def __init__(self, name, pron, hiragana, cixing, explain, explain_jp, listName):
        self.name = name
        self.pron = pron
        self.hiragana = hiragana
        self.cixing = cixing
        self.explain = explain
        self.explain_jp = explain_jp
        self.listName = listName
class WordList(db.Model):
    __tablename__ = 'wordList'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique= True, nullable=False)
 
    def __init__(self, name):
        self.name = name
app.run(host='0.0.0.0', port=8080)
# python -m PyInstaller -F app.py --add-data=templates;templates --add-data "static;static" --add-data "database.db;database.db"