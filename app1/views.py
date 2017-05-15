# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse


from app1.models import departmentInfo, certificateInfo, userInfo

# for authincation
from django.contrib import auth

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required






def index(request):
	print 'in index'
	return HttpResponse("Hello, world. You're at the polls index.")



@login_required(login_url='/app1/login')
def homepage(request):
	print 'in homepage def'

	userName = request.user.username
	print userName

	if request.method == 'GET':
		print 'in homepage GET'

		userObj = userInfo.objects.filter(userName=userName)

		if userObj:
			print 'userObj not NOne'
			print userObj
			deptName = userObj[0].department

		else:
			print 'userObj is None, user not present in userInfo table'
			return render(request, 'app1/addDepartment.html')

		#populating all the department from db
		#all_dept = departmentInfo.objects.filter()
		#for d in all_dept:
			#print d.departmentName



	elif request.method == 'POST':
		print 'in homepage POST'


	return render (request, 'app1/homepage.html', {'deptName' : deptName})












@login_required(login_url='/app1/login')
def addDeptInfo(request):
	print 'in addDeptInfo'
	return render (request, 'app1/addDepartment.html')




@login_required(login_url='/app1/login')
def cerdetails(request):
	print 'in cerDetails'
	return render(request, 'app1/cerdetails.html')


#will add the details about the new user on first time entry into the userInfo table
@login_required(login_url='/app1/login')
def addNewDept(request):
	print 'in addNewDept'
	# if request.method == 'POST':
	# 	print 'in method post'
	# 	deptName = request.POST.get('department')
	# 	print deptName

	# 	newDept = departmentInfo(departmentName=deptName)
	# 	newDept.save()

	# 	print 'savedone'

	# return redirect('homepage')

	userName = request.user.username

	if request.method == 'POST':
		deptName = request.POST.get('department')

	userObj = userInfo(userName=userName, department=deptName)
	userObj.save()

	return redirect('homepage')




@login_required(login_url='/app1/login')
def showDeptDetails(request, dept_name = ''):


	print 'in showDeptDetails'
	print dept_name
	if request.method == 'POST':
		print 'in showDeptDetailsPOST'


	elif request.method == 'GET':
		print 'in showDeptDetailsGET'


		all_cert = certificateInfo.objects.filter(department=dept_name)



		return render(request, 'app1/certificates.html', {'deptName' : dept_name, 'allCert' : all_cert})


		#show all certifictes available to this dept

		#can also add new certificates



@login_required(login_url='/app1/login')
def addCertificate(request):
	print 'in addCertificate'

	if request.method == 'POST':
		print ' in addCertificate POST'
		certName = request.POST.get('certName')
		certType = request.POST.get('certType')
		certPasswd = request.POST.get('certPasswd')
		expiryDate = request.POST.get('expiryDate')

		primaryOwner = request.POST.get('primaryOwner')
		#need to fix this, cant get value from the client
		#fixed : when we dissabled a field, its data  is not sent with the reqest, use readonly attribute instead
		#if primaryOwner is None:
		#	primaryOwner = request.user.username
			
		department = request.POST.get('department')
		#if department is None:
		#	department = userInfo.objects.filter(userName=primaryOwner)[0].department

		

		secondaryOwners = request.POST.get('secondaryOwners')
		escalationMail = request.POST.get('escalationMail')
		reminderDays = request.POST.get('reminderDays')
		comment = request.POST.get('comment')


		print certName, ' ', certType, ' ', certPasswd, ' ', expiryDate, ' ', department,' ',primaryOwner, ' ', secondaryOwners, ' ', escalationMail, ' ', reminderDays, ' ', comment

		certInfo = certificateInfo(comment=comment, reminderDays=reminderDays, certType=certType, certName=certName, certPasswd=certPasswd, expiryDate=expiryDate, department=department, primaryOwner=primaryOwner, secondaryOwners=secondaryOwners, escalationMail=escalationMail)
		certInfo.save()




	if request.method == 'GET':
		print ' in addCertificate GET'
		primaryOwner = request.user.username
		department = userInfo.objects.filter(userName=primaryOwner)[0].department
	
		print primaryOwner
		print department


		return render(request, 'app1/addCertificate.html', {'primaryOwner' :request.user.username, 'department': department})	

	return redirect('homepage')	



def login(request):
	print 'in login'

	if request.method == 'POST':
		print 'in login POST'

		userId = request.POST.get('userId')
		userPassword = request.POST.get('userPassword')

		#print userId
		#print userPassword

		user = auth.authenticate(username=userId, password=userPassword)
		print user

		if user is not None :
				print 'user is a authenticate user'
				auth.login(request, user)
				print 'user now logged in'

				# if redirect_url == '':
				return redirect('homepage')

		else:
			print 'user not VALID'
			return render(request, "app1/login.html")
			



	elif request.method == 'GET':
		print 'in login GET'


	return render(request, 'app1/login.html')



@login_required(login_url='/app1/login')
def viewAllCertificates(request):

	print 'in viewAllCertificates'

	if request.method == 'GET':
		userName = request.user.username
		print userName

		all_cert_primary_TYPE1 = certificateInfo.objects.filter(primaryOwner=userName, certType='AMG')
		all_cert_primary_TYPE2 = certificateInfo.objects.filter(primaryOwner=userName, certType='Password')
		all_cert_primary_TYPE3 = certificateInfo.objects.filter(primaryOwner=userName, certType='Certificate')
		print all_cert_primary_TYPE1

		all_cert_secondary_TYPE1 = certificateInfo.objects.filter(secondaryOwners=userName, certType='AMG')
		all_cert_secondary_TYPE2 = certificateInfo.objects.filter(secondaryOwners=userName, certType='Password')
		all_cert_secondary_TYPE3 = certificateInfo.objects.filter(secondaryOwners=userName, certType='Certificate')
		print all_cert_secondary_TYPE1

		return render(request, 'app1/viewAllCertificates.html', {'all_cert_primary_TYPE1' : all_cert_primary_TYPE1, 'all_cert_primary_TYPE2' : all_cert_primary_TYPE2, \
			'all_cert_primary_TYPE3' : all_cert_primary_TYPE3,  'all_cert_secondary_TYPE1' :all_cert_secondary_TYPE1, 'all_cert_secondary_TYPE2' :all_cert_secondary_TYPE2, \
			'all_cert_secondary_TYPE3' :all_cert_secondary_TYPE3})


def signout(request):

	print 'in logout'
	print request.user.username

	auth.logout(request)

	print request.user.username

	return render(request, 'app1/login.html')




@login_required(login_url='/app1/login')
def modify(request):
	print 'in modify'
	if request.method == 'POST':
		print 'in post'
		update = request.POST.get('update')
		delete = request.POST.get('delete')

		userName = request.user.username

		if update == 'update':
			print 'in update'

			certName = request.POST.get('certName')
			certType = request.POST.get('certType')
			certPasswd = request.POST.get('certPasswd')
			expiryDate = request.POST.get('expiryDate')
			primaryOwner = request.POST.get('primaryOwner')				
			department = request.POST.get('department')
			secondaryOwners = request.POST.get('secondaryOwners')
			escalationMail = request.POST.get('escalationMail')
			reminderDays = request.POST.get('reminderDays')
			comment = request.POST.get('comment')

			certInfoObj = certificateInfo.objects.filter(certName=certName, certType=certType, primaryOwner=primaryOwner).update(comment=comment, reminderDays=reminderDays, \
				certPasswd=certPasswd, expiryDate=expiryDate, department=department, secondaryOwners=secondaryOwners, escalationMail=escalationMail)
		
			


		elif delete == 'delete':
			print 'delete'
			certName = request.POST.get('certName')
			certType = request.POST.get('certType')
			primaryOwner = request.POST.get('primaryOwner')

			delCount = certificateInfo.objects.filter(certName=certName, certType=certType, primaryOwner=primaryOwner).delete()
			print delCount

		


	return redirect('viewAllCertificates')