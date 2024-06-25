from django.shortcuts import render, redirect, get_object_or_404
from .models import Owner, Review
from quality.models import TypeQuality, Quality
from skill.models import Skill
from service.models import Service
from gallery.models import TypePorfolio, Portfolio

from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives

from .forms import (
	ContactForm,
	)

from .mixins import (
	FormErrors,
	reCAPTCHAValidation
	)
from django.conf import settings
import requests
import json
import os
from django.http import FileResponse
from django.contrib import messages

from django.template.loader import get_template

from xhtml2pdf import pisa


ID_OWNER = 1
ID_QUALITY_EDUCATION=1
ID_QUALITY_EXPERIENCE=2

IDDES = 1
IDDEV = 2
IDAPPDES = 3

def home(request):
    owner_info=Owner.objects.filter(is_hidden=False).first()

    education_list = Quality.objects.filter(is_hidden=False,type_quality__id=ID_QUALITY_EDUCATION).order_by('order_number')
    experience_list = Quality.objects.filter(is_hidden=False,type_quality__id=ID_QUALITY_EXPERIENCE).order_by('order_number')
    skill_list_left = Skill.objects.filter(is_hidden=False,position="Left").order_by('order_number')
    skill_list_rigth = Skill.objects.filter(is_hidden=False,position="Rigth").order_by('order_number')
    service_list = Service.objects.filter(is_hidden=False).only('service_name','title','icon_name').order_by('order_number')
    

    portfolio_webdes = Portfolio.objects.filter(type_porfolio__id=IDDES).all()
    portfolio_webdev=Portfolio.objects.filter(type_porfolio__id=IDDEV).all()
    portfolio_appdev=Portfolio.objects.filter(type_porfolio__id=IDAPPDES).all()

    review_list = Review.objects.filter(is_hidden=False).order_by('order_number')

    type_portfolio = TypePorfolio.objects.all()
    portfolio_id = request.GET.get('type_portfolio')
    if portfolio_id:
        portfolio_list = Portfolio.objects.filter(type_porfolio=type_portfolio)
    else:
        portfolio_list = Portfolio.objects.all()



    #contact session
    c_form = ContactForm()
    result = "error"
    message = "Something went wrong. Please check and try again"
    
    if request.is_ajax() and request.method == "POST":
        c_form = ContactForm(data = request.POST)
		
		#if forms are valid, do something
        if c_form.is_valid():

			#get token from AJAX and test response
            token = c_form.cleaned_data.get('token')
            captcha = reCAPTCHAValidation(token)

            #print(captcha)

            fname = c_form.cleaned_data['name']
            femail = c_form.cleaned_data['email']
            fsubject = c_form.cleaned_data['subject']
            fmessage = c_form.cleaned_data['message']

            instance = c_form.save(commit=False)

            if captcha["success"] and captcha['score'] >= 0.5:

                #save on database contact information
                instance.save()                
                
                
                template = loader.get_template('portfolio/contact_form.txt')
                context = {
                    'fname':fname,
                    'femail':femail,
                    'fsubject':fsubject,
                    'fmessage':fmessage
                }
                message = template.render(context)

                email = EmailMultiAlternatives (
                    "Arnok (message)", message,
                    "Nouveau message " + "- Clients",
                    ['unlockagence@gmail.com']
                )
                email.content_subtype = 'html'

                email.send()

                result = "Perfect!"
                message="Your Message has been sent successfuly!"
                
            else:
                message="Invalid reCAPTCHA. Try again!"
                
        else:
            message = FormErrors(c_form)

        return HttpResponse(
			json.dumps({"result": result, "message": message}),
			content_type="application/json"
			)    

    context= {
        'owner_info':owner_info,
        'education_list':education_list,
        'experience_list':experience_list,
        'skill_list_left':skill_list_left,
        'skill_list_rigth':skill_list_rigth,
        'service_list':service_list,
        'portfolio_list':portfolio_list,
        'type_portfolio':type_portfolio,
        'portfolio_webdes':portfolio_webdes,
        'portfolio_webdev':portfolio_webdev,
        'portfolio_appdev':portfolio_appdev,
        'review_list':review_list,
        'c_form':c_form,
    }
    return render(request,'portfolio/home.html', context)


def service_detail(request):
    return render(request, 'portfolio/includes/service/service-detail.html')



def cv_download(request):
    portfolio = Owner.objects.filter(is_hidden=False).first()
    education_list = Quality.objects.filter(is_hidden=False,type_quality__id=ID_QUALITY_EDUCATION).order_by('order_number')
    experience_list = Quality.objects.filter(is_hidden=False,type_quality__id=ID_QUALITY_EXPERIENCE).order_by('order_number')
    skill_list_left = Skill.objects.filter(is_hidden=False,position="Left").order_by('order_number')
    skill_list_rigth = Skill.objects.filter(is_hidden=False,position="Rigth").order_by('order_number')
    service_list = Service.objects.filter(is_hidden=False).only('service_name','title','icon_name').order_by('order_number')
    
    context = {
        'portfolio': portfolio,
        'education_list':education_list,
        'experience_list':experience_list,
        'skill_list_left':skill_list_left,
        'skill_list_rigth':skill_list_rigth,
    }
    return render(request, 'cv-report.html',context)

def cv_report_create_pdf(request):
    portfolio = Owner.objects.filter(is_hidden=False).first()
    education_list = Quality.objects.filter(is_hidden=False,type_quality__id=ID_QUALITY_EDUCATION).order_by('order_number')
    experience_list = Quality.objects.filter(is_hidden=False,type_quality__id=ID_QUALITY_EXPERIENCE).order_by('order_number')
    skill_list_left = Skill.objects.filter(is_hidden=False,position="Left").order_by('order_number')
    skill_list_rigth = Skill.objects.filter(is_hidden=False,position="Rigth").order_by('order_number')    


    template_path = 'cv-download.html'

    context = {
        'portfolio': portfolio,
        'education_list':education_list,
        'experience_list':experience_list,
        'skill_list_left':skill_list_left,
        'skill_list_rigth':skill_list_rigth,
    }

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="cv_arnok.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def handler400(request,exception):
    return render(request, '400.html')

def handler403(request,exception):
    return render(request, '403.html')

def handler404(request,exception):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')