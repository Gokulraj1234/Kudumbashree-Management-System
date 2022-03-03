from flask import *
from database import *
import demjson
import uuid

api=Blueprint('api',__name__)

@api.route('/member_registration')
def member_registration():
	data={}
	firstname=request.args['firstname']
	lastname=request.args['lastname']
	place=request.args['place']
	phone=request.args['phone']
	email=request.args['email']
	username=request.args['username']
	password=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(username,password)
	res=select(q)
	if res:
		data['status']="duplicate"
	else:
		q="insert into login values(null,'%s','%s','pending')"%(username,password)
		id=insert(q)
		z="insert into member values(null,'%s','%s','%s','%s','%s','%s')"%(id,firstname,lastname,place,phone,email)
		insert(z)
		data['status']="success"
	return demjson.encode(data)

@api.route('/login')
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(username,password)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	return demjson.encode(data)
@api.route('/member_loanrequest',methods=['get','post'])
def member_loanrequest():
	data={}
	lid=request.args['lid']
	amount=request.args['amount']	
	q="insert into loanrequest values(null,(select member_id from member where login_id='%s'),'%s',curdate(),'pending')"%(lid,amount)
	insert(q)
	data['status']="success"
	data['method']="member_loanrequest"
	return demjson.encode(data)

@api.route('/member_view_loanstatus',methods=['get','post'])
def member_view_loanstatus():
	data={}
	lid=request.args['lid']
	q="select * from loanrequest where member_id=(select member_id from member where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="member_view_loanstatus"	
	return demjson.encode(data)

@api.route('/member_view_product',methods=['get','post'])
def member_view_product():
	data={}
	q="select * from product"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"	
	return demjson.encode(data)

@api.route('/member_send_request',methods=['get','post'])
def member_send_request():
	lid=request.args['lid']
	pid=request.args['pid']
	q="insert into request values(null,(select member_id from member where login_id='%s'),'%s','pending')"%(lid,pid)
	insert(q)
	data['status']="success"
	return demjson.encode(data)

@api.route('/member_view_request',methods=['get','post'])
def member_view_request():
	data={}
	lid=request.args['lid']
	q="select * from request inner join member using(member_id) inner join product using(product_id)where member_id=(select member_id from member where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
		
	return demjson.encode(data)

@api.route('/member_view_event_notification',methods=['get','post'])
def member_view_event_notification():
	data={}
	q="select * from event"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"	
	return demjson.encode(data)

@api.route('/member_attendance',methods=['get','post'])
def member_attendance():
	data={}
	lid=request.args['lid']
	z="select * from attendance where member_id=(select member_id from member where login_id='%s') and date=curdate()"%(lid)
	a=select(z)
	if a:
		data['status']="duplicate"
	else:	
		q="insert into attendance values(null,(select member_id from member where login_id='%s'),curdate())"%(lid)
		insert(q)
		data['status']="success"
	return demjson.encode(data)

@api.route('/user_view_product',methods=['get','post'])
def user_view_product():
	data={}
	q="select * from product"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"	
	return demjson.encode(data)

@api.route('/member_add_product',methods=['get','post'])
def member_add_product():
	data={}
	lid=request.form['lid']
	productname=request.form['productname']
	details=request.form['details']
	image=request.files['image']
	path="static/uploads/"+str(uuid.uuid4())+image.filename
	image.save(path)
	q="insert into product values(null,'%s','%s','%s','pending')" %(productname,details,path)
	id=insert(q)
	q="insert into request values(null,(select member_id from member where login_id='%s'),'%s','pending')"%(lid,id)
	insert(q)
	data['status']="success"
	return demjson.encode(data)
@api.route('/member_view_profile')
def member_view_profile():
	data={}
	lid=request.args['lid']
	q="select * from member where member_id=(select member_id from member where login_id='%s')"%(lid)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"
	data['method']="member_view_profile"	
	return demjson.encode(data)

@api.route('/member_manage_profile')
def member_manage_profile():
	data={}
	lid=request.args['lid']
	firstname=request.args['firstname']
	lastname=request.args['lastname']
	place=request.args['place']
	phone=request.args['phone']
	email=request.args['email']
	q="update member set firstname='%s',lastname='%s',place='%s',phone='%s',email='%s' where member_id=(select member_id from member where login_id='%s')"%(firstname,lastname,place,phone,email,lid)
	insert(q)
	data['status']="success"
	data['method']="member_manage_profile"
	return demjson.encode(data)	

@api.route('/user_view_products',methods=['get','post'])
def user_view_products():	
	data={}
	p="%"+request.args['p']+"%"
	q="select * from product where productname like '%s'"%(p)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"	
	return demjson.encode(data)

@api.route('/user_view_event_notification',methods=['get','post'])
def user_view_event_notification():
	data={}
	q="select * from event"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"	
	return demjson.encode(data)	

@api.route('/member_make_payment',methods=['get','post'])
def member_make_payment():
	data={}
	lid=request.args['lid']
	lrid=request.args['lrid']
	amountt=request.args['amountt']
	q="insert into payments values(null,'%s','%s',curdate())"%(lrid,amountt)
	insert(q)
	data['status']="success"
	return demjson.encode(data)	

@api.route('/member_view_dues',methods=['get','post'])
def member_view_dues():
	data={}
	lid=request.args['lid']
	if "date" in request.args:

		date="%"+request.args['date']
		q="select *,payments.amount as amounts,payments.date as dates from payments inner join loanrequest using(loanrequest_id) where payments.date like '%s' and member_id=(select member_id from member where login_id='%s')" %(date,lid)
	else:
		q="select *,payments.amount as amounts,payments.date as dates from payments inner join loanrequest using(loanrequest_id) where member_id=(select member_id from member where login_id='%s')" %(lid)
	print(q)
	res=select(q)
	print(res)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"	
	return demjson.encode(data)

@api.route('/member_view_meeting',methods=['get','post'])
def member_view_meeting():
	data={}
	q="select * from meeting"
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
	else:
		data['status']="failed"	
	return demjson.encode(data)

@api.route('/member_pay_savings',methods=['get','post'])
def member_pay_savings():
	data={}
	lid=request.args['lid']

	amount=request.args['amount']
	z="select * from account where member_id=(select member_id from member where login_id='%s')"%(lid)
	res=select(z)
	if res:
		x="update account set balance=balance+'%s' where member_id=(select member_id from member where login_id='%s')"%(amount,lid)
		update(x)
	else:
		q="insert into account values(null,(select member_id from member where login_id='%s'),'%s',curdate(),'%s','paid')"%(lid,amount,amount)
		insert(q)
	data['status']="success"
	return demjson.encode(data)

@api.route('/member_pay_loan',methods=['get','post'])
def member_pay_loan():
	data={}
	lid=request.args['lid']
	lrid=request.args['lrid']
	amount=request.args['amount']
	q="insert into payments values(null,'%s','%s',curdate())"%(lrid,amount)
	insert(q)
	data['status']="success"
	return demjson.encode(data)					