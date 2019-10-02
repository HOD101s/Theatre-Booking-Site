from flask import Flask, render_template, request
from model.dbconnect import dbconn
from model import Query
from flask import jsonify

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


# Session Variables
showID = ""
activeUser = ""
showTime = ""


# TODO enter login verification

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/time')
def time():
	return render_template('time.html')

@app.route('/get_time', methods=['POST'])
def timing():
	print(request.cookies['bookMovie'])
	cur.execute(Query.getTimings.format(request.cookies['bookMovie']))
	t = [str(x)[2:7] for x in cur.fetchall()]
	print(t)
	return jsonify(t)

@app.route('/confirm')
def confirm():
	print(request.cookies['bookMovie'], request.cookies['timings'],request.cookies['seats'], sep='\n')
	cur.execute(Query.updateTickets.format(','+str(request.cookies['seats']),(request.cookies['bookMovie']), request.cookies['timings']))
	con.commit()
	return render_template('confirm.html')

@app.route('/ticket')
def ticket():
	print(request.cookies['bookMovie'], request.cookies['timings'],sep='\n')
	cur.execute(Query.getShowData.format(request.cookies['bookMovie'], request.cookies['timings']))
	res = cur.fetchall()
	print(res)
	global showTime
	global showId
	showId = res[0][0]
	SCREEN = res[0][1]
	TIME = res[0][2]
	showTime = TIME
	PRICE = res[0][3]
	mid = res[0][4]
	BOOKED = res[0][5]
	if BOOKED == '':
		return render_template('ticket.html', movie=request.cookies['bookMovie'], screen=SCREEN, time=TIME, price=PRICE,
							   booked=BOOKED)
	if BOOKED[0] == ',':
		BOOKED = BOOKED[1:]
	BOOKED = str(' '.join(BOOKED.split(',')))
	print("Hello"+BOOKED+"Hoe")
	return render_template('ticket.html',movie =request.cookies['bookMovie'], screen=SCREEN,time = TIME, price=PRICE,booked = BOOKED)


if __name__ == '__main__':
	app.run()
