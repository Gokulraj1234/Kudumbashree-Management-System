from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_add_profile',methods=['get','post'])
def admin_add_profile():
	if 'submit' in request.form:
		firstname=request.form['firstname']
		lastname=request.form['lastname']
		place=request.form['place']
		phone=request.form['phone']
		email=request.form['email']
		q="insert into profile values(null,'%s','%s','%s','%s','%s')"%(firstname,lastname,place,phone,email)
		insert(q)
	return render_template('admin_add_profile.html')

@admin.route('/admin_view_member',methods=['get','post'])
def admin_view_member():
	data={}
	q="select * from member inner join login using(login_id)"
	res=select(q)
	data['member']=res
	if 'action' in request.args:
		action=request.args['action']
		lid=request.args['l_id']

	else:
		action=None
	if action=='accept':
		q="update login set usertype='member' where login_id='%s'"%(lid)
		update(q)
	if action=='reject':
		q="update login set usertype='reject' where login_id='%s'"%(lid)
		update(q)
	
	return render_template('admin_view_member.html',data=data)


@admin.route('/admin_view_attendance',methods=['get','post'])
def admin_view_attendance():
	data={}
	
	q="select * from attendance inner join member using(member_id)"
	res=select(q)
	data['att']=res
	return render_template('admin_view_attendance.html',data=data)
@admin.route('/admin_view_loanrequest',methods=['get','post'])
def admin_view_loanrequest():
	data={}
	q="select * from loanrequest inner join member using(member_id)"
	res=select(q)
	data['loan']=res
	if 'action' in request.args:
		action=request.args['action']
		lr_id=request.args['lr_id']
	else:
		action=None
	if action=='accept':
		q="update loanrequest set status='accept' where loanrequest_id='%s'"%(lr_id)
		update(q)
	if action=='reject':
		q="update loanrequest set status='reject' where loanrequest_id='%s'"%(lr_id)
		update(q)
	return render_template('admin_view_loanrequest.html',data=data)

@admin.route('/admin_view_payment',methods=['get','post'])
def admin_view_payment():
	data={}
	lr_id=request.args['lr_id']
	q="select *,payments.amount as pamount from payments inner join loanrequest using(loanrequest_id) inner join member using(member_id) where loanrequest_id='%s'"%(lr_id)
	res=select(q)
	data['pay']=res
	return render_template('admin_view_payment.html',data=data)	

@admin.route('/admin_manage_product',methods=['get','post'])
def admin_manage_product():
	data={}
	q="select * from product"
	res=select(q)
	data['product']=res
	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if action=="update":
		q="select * from product"
		res=select(q)
		data['pro']=res
		if 'submit' in request.form:
			productname=request.form['productname']
			details=request.form['details']
			image=request.files['image']
			path="static/uploads/"+str(uuid.uuid4())+image.filename
			image.save(path)
			q="update product set productname='%s',details='%s',image='%s' where product_id='%s'"%(productname,details,path,pid)
			update(q)
			return redirect(url_for('admin.admin_manage_product'))
	if action=="delete":
		q="delete from product where product_id='%s'"%(pid)
		delete(q)
		return redirect(url_for('admin.admin_manage_product'))			
	if 'submit' in request.form:
		productname=request.form['productname']
		details=request.form['details']
		image=request.files['image']
		path="static/uploads/"+str(uuid.uuid4())+image.filename
		image.save(path)
		q="insert into product values(null,'%s','%s','%s')"%(productname,details,path)
		insert(q)
		return redirect(url_for('admin.admin_manage_product'))
	return render_template('admin_manage_product.html',data=data)

@admin.route('/admin_add_store',methods=['get','post'])
def admin_add_store():
	pid=request.args['pid']
	if 'submit' in request.form:
		storename=request.form['storename']
		q="insert into store values(null,'%s','%s')"%(pid,storename)
		insert(q)
		return redirect(url_for('admin.admin_manage_product'))
	return render_template('admin_add_store.html')

@admin.route('/admin_add_event',methods=['get','post'])
def admin_add_event():
	if 'submit' in request.form:
		event=request.form['event']
		details=request.form['details']
		image=request.files['image']
		path="static/uploads/"+str(uuid.uuid4())+image.filename
		image.save(path)
		q="insert into event values(null,'%s','%s','%s')"%(event,details,path)
		insert(q)
		return redirect(url_for('admin.admin_add_event'))
	return render_template('admin_add_event.html')

@admin.route('/admin_view_request',methods=['get','post'])
def admin_view_request():
	data={}
	q="select * from request inner join product using(product_id) inner join member using(member_id)where request.status='pending'"
	res=select(q)
	data['req']=res
	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None
	if action=='accept':
		q="update request set status='accept' where request_id='%s'"%(rid)
		update(q)
	if action=='reject':
		q="update request set status='reject' where request_id='%s'"%(rid)
		update(q)
	return render_template('admin_view_request.html',data=data)

@admin.route('/admin_send_meetinglink',methods=['get','post'])
def admin_send_meetinglink():
	if 'submit' in request.form:
		meeting=request.form['meeting']
		link=request.form['link']
		date=request.form['date']
		q="insert into meeting values(null,'%s','%s','%s')"%(meeting,link,date)
		insert(q)
		return redirect(url_for('admin.admin_send_meetinglink'))
	return render_template('admin_send_meetinglink.html')

@admin.route('/admin_view_savings',methods=['get','post'])
def admin_view_savings():
	data={}
	q="select * from account inner join member using(member_id)"
	res=select(q)
	data['acc']=res
	return render_template('admin_view_savings.html',data=data)					