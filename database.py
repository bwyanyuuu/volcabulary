# 模型( model )定義
class Word(db.Model):
    __tablename__ = 'word'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(100), nullable=False)
    cixing = db.Column(db.String(10), nullable=False)
    explain = db.Column(db.String(100), nullable=False)
    listName = db.Column(db.String(30), nullable=False)
    insert_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, onupdate=datetime.now, default=datetime.now)
 
 
    def __init__(self, word, cixing, explain, listName):
        self.word = word
        self.cixing = cixing
        self.explain = explain
        self.listName = listName
class WordList(db.Model):
    __tablename__ = 'wordList'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique= True,nullable=False)
 
    def __init__(self, name):
        self.name = name