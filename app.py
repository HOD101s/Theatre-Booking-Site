from flask import Flask, render_template, request
from model.dbconnect import dbconn

app = Flask(__name__)
app.config["DEBUG"] = True

db = {
	'user': 'root',
	'password': '',
	'host': '127.0.0.1',
	'database': 'theatre'
}

try:
	con = dbconn(db)
	cur = con.cursor()
	print("Connected")
except:
	print("Not Connected")


# TODO enter login verification

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/ticket')
def ticket():
	cookie = request.cookies.get('bookMovie')
	return render_template('ticket.html')



if __name__ == '__main__':
	app.run()
