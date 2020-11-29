from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from bs4 import BeautifulSoup
from PIL import Image, ImageFont, ImageDraw
import pandas as pd
import os

# Create your views here.
def welcome(request):
    return render(request,'welcome.html',{'link':'http://127.0.0.1:8000/home/'})



def disresult(request):
    driver = webdriver.Chrome("C:/Users/amree/Desktop/DiGiHealth/chromedriver")
    global symptoms
    global diseas
    symptoms = request.GET['symp']
    symptoms = symptoms.replace(' ', '+')
    diseas=[] 
    driver.get("https://www.google.com/search?q=" + symptoms) 
    content = driver.page_source
    soup = BeautifulSoup(content)
    data = soup.findAll('div', attrs ={'class':'OtUpef PZPZlf'})
    for i in data:
        diseas.append(i.text)
    print(diseas)
    return render(request, 'result.html', {'result':diseas, 'link':'http://127.0.0.1:8000/report/'})
    

def downloadreport(request):
    name=request.GET['name']
    s= str(symptoms)
    d = str(diseas)
    font = ImageFont.truetype('calibri.ttf',30)
    img = Image.open('C:/Users/amree/Desktop/medreport.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(310,680),text= name ,fill=(0,0,0),font=font)
    draw.text(xy=(299,825),text= s ,fill=(0,0,0),font=font)
    draw.text(xy=(285,940),text= d ,fill=(0,0,0),font=font)
    img.save('C:/Users/amree/Desktop/pictures.jpg') 
    return render(request,'download.html')


def getreport(request):
    return render(request, 'report.html')

def home(request):
    return render(request, 'home.html',{'link':'http://127.0.0.1:8000/login/',
     'link1':'http://127.0.0.1:8000/register/',
     'link3':'http://127.0.0.1:8000/about/',
     'link4':'http://127.0.0.1:8000/check/',
     'link6':'http://127.0.0.1:8000/doctors/'})

def check(request):
    return render(request, 'check.html')

def service(request):
    return render(request,'service.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def doctors(request):
    return render(request, 'doctors.html', {'link2':'http://127.0.0.1:8000/home/',
    'link':'http://127.0.0.1:8000/login/',
     'link1':'http://127.0.0.1:8000/register/'})