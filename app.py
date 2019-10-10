from flask import Flask, render_template, request, redirect, url_for
from model.dbconnect import dbconn
from model import Query
from flask import jsonify
import hashlib
from datetime import datetime

#commit = local
#push = local code goes to Github

##### MUST UPDATE BEFORE COMMIT/PUSH
# 1. Commit
# 2. Push

# TODO Jeremy : home (ids must be same as Db : save Db SQL queries) : login (only front end) reg (only front end) : ticket (Only fonts front end, do not meddle with JavaScript)
# TODO Sachin :
# TODO Manas : home.html front end
# TODO Manas : add all movies page, add mytickets to home
# TODO change navbar color, pulse, animtation, confirm page,

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

#Redirect Login
@app.route('/')
def begin():
	return redirect(url_for('login'))

#Render Home
@app.route('/home')
def home():
	return render_template('home.html')

#Render Time
@app.route('/time')
def time():
	MOVIE = request.cookies['bookMovie']
	return render_template('time.html',movie=MOVIE)

#Return Show Timings
@app.route('/get_time', methods=['POST'])
def timing():
	print(request.cookies['bookMovie'])
	cur.execute(Query.getTimings.format(request.cookies['bookMovie']))
	t = [str(x)[2:7] for x in cur.fetchall()]
	print(t)
	return jsonify(t)

#Render Confirmed Tickets Page
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

#Rednder Booking Page
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

#Render Register Page
@app.route('/register')
def register():
	return render_template('register.html')

#Registration Checking Entries
@app.route('/check_register',methods=['POST'])
def check_register():
	email = str(request.get_data().decode('UTF-8'))
	if email == "":
		return '3'
	print(email)
	print(request.cookies['reguser'],request.cookies['regpass'], sep='\n')
	cur.execute(Query.check_register.format(request.cookies['reguser']))
	if len(cur.fetchall()) > 0:
		return '0'
	else:
		try:
			cur.execute(Query.regUser.format(request.cookies['reguser'],str(hashlib.md5(request.cookies['regpass'].encode()).hexdigest()),email))
			con.commit()
			return '1'
		except:
			return '2'

#Render Admin Page
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

#Render Login
@app.route('/login')
def login():
	return render_template('login.html')

#Login Verification
@app.route('/check_login',methods=['POST'])
def check_login():
	global activeUser
	print(request.cookies['user'],request.cookies['pass'], sep='\n')
	cur.execute(Query.check_login.format(request.cookies['user'],str(hashlib.md5(request.cookies['pass'].encode()).hexdigest())))
	x = cur.fetchall()
	if len(x) > 0:
		activeUser = request.cookies['user']
		if x[0][2] == '1':
			return '2'
		return '1'
	else:
		activeUser = ""
		return '0'

#Insert into Show
@app.route('/insert_show',methods=['POST'])
def insertShow():
	val = str(request.get_data().decode('UTF-8')).split(' ')
	if len(val[3]) == 4:
		val[3] = '0'+val[3]
		print(val[3])
	try:
		cur.execute(Query.insertShow.format(val[0],val[1],val[3],int(val[2]),val[4]))
		con.commit()
		return "1"
	except:
		return "2"

#Insert into Movie
@app.route('/insert_movie',methods=['POST'])
def insertMovie():
	val = str(request.get_data().decode('UTF-8')).split(' ')
	try:
		cur.execute(Query.insertMovie.format(val[0],val[1]))
		con.commit()
		return "1"
	except:
		return "2"

#Render all Movies Page
@app.route('/allMovie')
def allMov():
	cur.execute(Query.allMovie)
	return render_template('movie.html',res = cur.fetchall())

#Render MyTickets Page
@app.route('/myTickets')
def myTickets():
	cur.execute(Query.userTickets.format(request.cookies['user']))
	return render_template('myTickets.html',res=cur.fetchall())

if __name__ == '__main__':
	app.run()
