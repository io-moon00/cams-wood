from django.shortcuts import render
import datetime
from .models import Page, Image
from .forms import ContactForm_de
from django. conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    date = datetime.date.today()
    year = date.year
    page = Page.objects.first()
    images = Image.objects.all()

    submitted = False
    if request.method == 'POST':
        form_de = ContactForm_de(request.POST)

        if form_de.is_valid():
            cd = form_de.cleaned_data
            subject, from_email, to = 'Contact Form Cams Wood', settings.EMAIL_HOST_USER, 'sworks@hotmail.com'
            html_content = render_to_string('email.html', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
            text_content = render_to_string('email.txt', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
                
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('?submitted=True#contact')

    else:
        form_de = ContactForm_de()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home.html', {'year': year, 'page': page, 'images': images, 'form_de': form_de, 'submitted': submitted})


def impressum(request):
    date = datetime.date.today()
    year = date.year
    page = Page.objects.get(title = 'Impressum')

    return render(request, 'leagel.html', {'year': year, 'page': page})

def data(request):
    date = datetime.date.today()
    year = date.year
    page = Page.objects.get(title = 'Datenschutzerklärung')

    return render(request, 'leagel.html', {'year': year, 'page': page})
