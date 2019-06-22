from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from app.models import *
#from app.spellcheck import *
#from app.grammer import *
from app.trycheck import *
from django.http import HttpResponse
import csv
from app.grading import *

def start(request):
	name=request.session['name']
	return render(request, 'index.html',{'name':name})
def register(request):
	
	request.session.flush()
	return render(request, 'Login.html',{})
def login(request):
	return render(request, 'Reg.html',{})
def checkscorepage(request):
	obj=EssayData.objects.all()
	email=request.session['email']
	d=0
	context={}
	b1=''
	b2=''
	b3=''
	b4=''
	b5=''
	b6=''
	ob=HtmlData.objects.all()
	for elt in ob:
		if elt.filename=='t1':
			b1=elt.code
			break
	for elt in ob:
		if elt.filename=='t2':
			b2=elt.code
			break
	for elt in ob:
		if elt.filename=='t3':
			b3=elt.code
			break
	for elt in ob:
		if elt.filename=='t4':
			b4=elt.code
			break
	for elt in ob:
		if elt.filename=='t5':
			b5=elt.code
			break
	for elt in ob:
		if elt.filename=='t6':
			b6=elt.code
			break
	table=''
	for elt in obj:
		if elt.userid==email:
			d=1
			data=b1+elt.topic+b2+elt.wordcount+b3+elt.spellcheck+b4+elt.grammercheck+b5+elt.error+b6
			table=table+data
	if d==1:
		return render(request, "CheckScore.html" , {'data':table})
	else:
		return render(request, "CheckScore.html" , {})
@csrf_exempt
def checkscore(request):
	if request.method=="POST":
		topic = request.POST.get('Topic')
		data = request.POST.get('text')
		print(data[3:len(data)-4])
		obj=EssayData.objects.all()
		count = str(data[3:len(data)-4]).split()
		length = len(count)
		spell = Check_spelling(str(data))
		grammer = Capitalize(str(data[3:len(data)-4]))
		art=check_articles(str(data))
		Graded_result=Main_fun()
		obj=EssayData(userid=request.session['email'],topic=topic,essay=data,wordcount=length,spellcheck=spell,grammercheck=grammer,error=art,grade=Graded_result)
		mail_id=request.session['email']
		obj.save()
		data_scores=[mail_id,topic,data,length,spell,grammer,art,Graded_result]
		f=open('ScoreData.csv','a')
		writer=csv.writer(f)
		writer.writerow(data_scores)
		f.close()
		b1=''
		b2=''
		b3=''
		b4=''
		b5=''
		b6=''
		
		ob=HtmlData.objects.all()
		for elt in ob:
			if elt.filename=='t1':
				b1=elt.code
				break
		for elt in ob:
			if elt.filename=='t2':
				b2=elt.code
				break
		for elt in ob:
			if elt.filename=='t3':
				b3=elt.code
				break
		for elt in ob:
			if elt.filename=='t4':
				b4=elt.code
				break
		for elt in ob:
			if elt.filename=='t5':
				b5=elt.code
				break
		for elt in ob:
			if elt.filename=='t6':
				b6=elt.code
				break
		
                        
		table=''
		obj=EssayData.objects.all()
		for elt in obj:
			if elt.userid==request.session['email']:
				d=1
				elt.topic=str(Graded_result)
				data=b1+elt.topic+b2+elt.wordcount+b3+elt.spellcheck+b4+elt.grammercheck+b5+elt.error+b6
				table=table+data
		return render(request, "CheckScore.html" , {'data':table})
def analyticspage(request):
	return render(request, 'Analytics.html',{})
def rulespage(request):
	return render(request, 'Rules.html',{})
def contactpage(request):
	return render(request, 'Contact.html',{})
@csrf_exempt
def saveuser(request):
	if request.method=="POST":
		text=' '
		n=request.POST.get('name')
		g=request.POST.get('gender')
		ph=request.POST.get('phone')
		p=request.POST.get('password')
		e=request.POST.get('email')
		ob=UserData.objects.all()
		d=0
		for elt in ob:
			if e==elt.email:
				d=1
				break
		if d==0:
			obj=UserData(name=n,password=p,email=e,gender=g,phone=ph,status='N')
			obj.save()
			request.session['userid'] = e
			text='Account Created Successfully'
			context={'text':text,
					'name':n}
			return render(request,'policy.html',context)
		else:
			text='User Already Exists'
			context={'text':text}
			return render(request,'regresult.html',context)
@csrf_exempt
def checklogin(request):
	text=" "
	d=0
	e=request.POST.get('email')
	p=request.POST.get('password')
	obj=UserData.objects.all()
	name=''
	for elt in obj:
		if e==elt.email and p==elt.password and elt.status=='Y':
			d=1
			name=elt.name
			request.session['email'] = e
			request.session['name'] = elt.name
			break
		elif e==elt.email and p==elt.password and elt.status=='N':
			request.session['userid'] = e
			text=' '
			context={'text':text,
					'name':elt.name}
			return render(request,'policy.html',context)
			break
	if d==0:
		con={'text':"No User Found"}
		return render(request,"regresult.html",con)
	else:
		return render(request,'start.html',{'name':name})
def acceptpolicy(request):
	obj=UserData.objects.filter(email=request.session['userid']).update(status="Y")
	return render(request,'Reg.html',{})