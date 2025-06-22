from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service_Member
from news.models import News
from blog.models import Blog
from enquiryform.models import saveenquiry
from registration.models import saveregistration
from django.core.paginator import Paginator
from django.core.mail import send_mail,EmailMultiAlternatives
import datetime

def aboutUs(request):
    return HttpResponse("<h1>Welconme to MCIT</h1>")

def CourseDetails(request,courseid):
    return HttpResponse(courseid)

def Coursestring(request,coursestr):
    return HttpResponse(coursestr)

def Courseslugdata(request,courseslug):
    return HttpResponse(courseslug)

def homePage(request):
    data={
        'title':'data render from home pae function',
        'data':'welcome to MCIT',
        'CourseList':['php','java','django','python'],
        'numbers':[20,30,40,50,60,70,80],
        'marks':[],
        'student_details':[
            {'name':'seema','phone':989898998},
            {'name':'rahul','phone':90098998}
        ]
    }
    return render(request,"home.html",data)

def index(request):
    newsdata=News.objects.all()
    print(newsdata)
    latestnews={
        'latestnews':newsdata,
    }
    return render(request,"index.html", latestnews)

def blog(request):
    return render(request,"blog-single.html")

def contact(request):
    return render(request,"contact.html")

def service(request):
    serviceData=Service_Member.objects.all()
    paginator = Paginator(serviceData, 3)
    page_number = request.GET.get('page')
    pagedatafinal = paginator.get_page(page_number)
    totalpage = pagedatafinal.paginator.num_pages
    # for a in serviceData:
    #     print(a.service_title)
    # print(serviceData)
    alllist={
         'pagedatafinal': pagedatafinal,
        'lastpage': totalpage,
        'totalpagelist': [n+1 for n in range(totalpage)]
    }
    return render(request,"service.html",alllist)

def error(request):
    return render(request,"404.html")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def error_404_view(request,exception):
    return render(request,'404.html')

def contactEnquiry(request):
  
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # todaydate = date.today()
        # print(todaydate)        
        en = saveenquiry(name=fname, email=email, phone=phone,
                         subject=subject, message=message)
        en.save()
        messagelist= fname+"\n"+email+"\n"+str(phone)+"\n"+message
        send_mail(subject, messagelist, 'aaruaj14@gmail.com',
              ['shejalesapna21@gmail.com'], fail_silently=False,)

        return render(request, "contact.html")
    
def registration(request):
    return render(request,"registration.html")
    
def savereg(request):
  
    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        date = request.POST.get('date')
        print(date)
        en = saveregistration(name=fname, email=email, phone=phone,
                         subject=subject, message=message,appodate=date)
        en.save()
        messagelist= fname+"\n"+email+"\n"+str(phone)+"\n"+message+"\n"+subject+"\n"+date
        send_mail(subject, messagelist, 'aaruaj14@gmail.com',
              ['shejalesapna21@gmail.com'], fail_silently=False,)
        return render(request, "registration.html")
    
    
def blogdata(request):   
    blogData = Blog.objects.all()  
    data = {
        'blogData': blogData
    }
    return render(request, "blog-single.html", data)

def servicedetails(request, slug):
    # def newsdetails(request, id):
    # print(id)
    servicedetails = Service_Member.objects.get(service_slug=slug)
    # newsdetails = News.objects.get(id=id)
    data = {
        'servicedetails': servicedetails
    }
    return render(request, "servicedetails.html", data)

def email_multi_alternatives(request):
    subject = 'email_multi_alternatives testing'
    from_email = 'aaruaj14@gmail.com'
    msg = '<h1>welcome to <b>MSCIT</b></h1><p><a href="http://127.0.0.1:8000/media/service/Cloud__DevOps.pdf"><h2>CLICK HERE</h2></a></p>'
    # msg='<h1>welcome to <b>MSCIT</b></h1><p><img src="http://127.0.0.1:8000/media/service/images/img2.jpg" alt="logo"></p>'
    to = 'shejalesapna21@gmail.com'
    msg = EmailMultiAlternatives(subject, msg, from_email, [to])
    msg.content_subtype = "html"
    msg.send()
    return render(request, "contact.html")
