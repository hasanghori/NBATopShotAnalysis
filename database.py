from flask import Flask
from datetime import timedelta
import csv

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "PLZWORK"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=30)

db = SQLAlchemy(app)


class itemPurchaseData(db.Model):
  
    id = db.Column("id", db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    time = db.Column(db.String(8))
    setID = db.Column(db.Integer)
    setName = db.Column(db.String(35))
    playID = db.Column(db.Integer)
    serialNumber = db.Column(db.Integer)
    playerName = db.Column(db.String(35))
    price = db.Column(db.Integer)
   
    def __init__(self, date, time, setID, setName, playID, serialNumber, playerName, price):
        self.date = date
        self.time = time
        self.setID = setID
        self.setName = setName
        self.playID = playID
        self.serialNumber = serialNumber
        self.playerName = playerName
        self.price = price


data = itemPurchaseData.query.filter_by(setID=26).first()
print(data.playerName)

db.create_all()



with open("result.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            
            date = row['Date'][0:10]
            print(date)
            time = row['Date'][11:18]
            print(time)
            setID = int(row['setID'])
            setName = row['setName']
            playID = int(row['playID'])
            serialNumber = int(row['serialNumber'])
            playerName = row['playerName']
            price = float(row['price'])

            newSaleData = itemPurchaseData(date=date, time=time, setID=setID, setName=setName, 
                playID=playID, serialNumber=serialNumber, playerName=playerName, price=price)
            db.session.add(newSaleData)
            db.session.commit()


            

