from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:gun23@localhost/Project_Database'

db=SQLAlchemy(app)

# class Try(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     abc=db.Column(db.String(200))


with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__=="__main__":
    app.run(debug=True)
