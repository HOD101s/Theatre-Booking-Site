from flask import Flask, render_template, request, redirect, url_for
from model.dbconnect import dbconn
from model import Query
from flask import jsonify
import hashlib
import uuid
from datetime import datetime


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


@app.route('/home')
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
	global showID
	global activeUser
	print("Show ID : ",showID)
	tid = hashlib.md5((activeUser+request.cookies['seats']+request.cookies['bookMovie']+request.cookies['timings']).encode()).hexdigest()
	tstamp = str(datetime.now())
	cur.execute(Query.insertTicket.format(tid,tstamp,request.cookies['seats'],showID,activeUser))
	con.commit()
	return render_template('confirm.html',TID = tid, TSTAMP = tstamp, SEATS = request.cookies['seats'],SHOWID = showID, MOVIE = request.cookies['bookMovie'], TIME = request.cookies['timings'])

@app.route('/ticket')
def ticket():
	print(request.cookies['bookMovie'], request.cookies['timings'],sep='\n')
	cur.execute(Query.getShowData.format(request.cookies['bookMovie'], request.cookies['timings']))
	res = cur.fetchall()
	print(res)
	global showTime
	global showID
	showID = res[0][0]
	SCREEN = res[0][1]
	TIME = res[0][2]
	showTime = TIME
	PRICE = res[0][3]
	mid = res[0][4]
	BOOKED = res[0][5]
	print('ShowID : '+showID,res[0][0])
	if BOOKED == '':
		return render_template('ticket.html', movie=request.cookies['bookMovie'], screen=SCREEN, time=TIME, price=PRICE,
							   booked=BOOKED)
	if BOOKED[0] == ',':
		BOOKED = BOOKED[1:]
	BOOKED = str(' '.join(BOOKED.split(',')))
	return render_template('ticket.html',movie =request.cookies['bookMovie'], screen=SCREEN,time = TIME, price=PRICE,booked = BOOKED)


@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/check_register',methods=['POST'])
def check_register():
	print(request.cookies['reguser'],request.cookies['regpass'], sep='\n')
	cur.execute(Query.check_register.format(request.cookies['reguser']))
	if len(cur.fetchall()) > 0:
		return '0'
	else:
		cur.execute(Query.regUser.format(request.cookies['reguser'],str(hashlib.md5(request.cookies['regpass'].encode()).hexdigest())))
		con.commit()
		return '1'

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/check_login',methods=['POST'])
def check_login():
	global activeUser
	print(request.cookies['user'],request.cookies['pass'], sep='\n')
	cur.execute(Query.check_login.format(request.cookies['user'],str(hashlib.md5(request.cookies['pass'].encode()).hexdigest())))
	if len(cur.fetchall()) > 0:
		activeUser = request.cookies['user']
		if activeUser == 'admin':
			return redirect({{url_for('admin')}})
		return '1'
	else:
		activeUser = ""
		return '0'

@app.route('/admin')
def admin():
	cur.execute(Query.allShow)
	showRes = cur.fetchall()
	cur.execute(Query.allTicket)
	ticketsRes = cur.fetchall()
	cur.execute(Query.allClient)
	clientsRes = cur.fetchall()
	cur.execute(Query.allMovie)
	movieRes = cur.fetchall()
	return render_template('admin.html',show = showRes, ticket = ticketsRes,clients = clientsRes, movies = movieRes)

def getNewID():
	return uuid.uuid4()

if __name__ == '__main__':
	app.run()