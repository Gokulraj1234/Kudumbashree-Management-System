from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
	data={}
	q="SELECT * FROM `product`"
	res=select(q)
	data['res']=res

	if 'search' in request.form:
		srch=request.form['srch']
		sr="%"+srch+"%"
		q="select * from `product` where `productname` like '%s'"%(sr)
		res=select(q)
		data['res']=res
	z="select * from event"
	res1=select(z)
	data['event']=res1	
	return render_template('index.html',data=data)
@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=="admin":
				return redirect(url_for('admin.admin_home'))
			# if res[0]['user_type']=="hotel":
			# 	a="select * from hotel where login_id='%s'"%(session['lid'])
			# 	res1=select(a)
			# 	if res1:
			# 		session['hotel_id']=res1[0]['hotel_id']
			# 		return redirect(url_for('hotel.hotel_home'))
			# if res[0]['user_type']=="agency":
			# 	a="select * from travel_agencies where login_id='%s'"%(session['lid'])
			# 	res1=select(a)
			# 	if res1:
			# 		session['travel_agencies_id']=res1[0]['travel_agencies_id']
			# 		return redirect(url_for('agency.agency_home'))			
	return render_template('login.html')		