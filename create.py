from flask import Flask
from models import *
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='opostgres://hmqtbfdvdzcfch:19b240437b1d1f0b3e3758392087cd9e0900fd14372d65d95884e7a2217f8648@ec2-50-16-198-4.compute-1.amazonaws.com:5432/d8frjgevahei2q'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
