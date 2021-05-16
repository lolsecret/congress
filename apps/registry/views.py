from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def homepage(request):
    return render(request, "index.html")

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'middle_name': form.cleaned_data['middle_name'],
                'phone': form.cleaned_data['phone'],
                'work_place': form.cleaned_data['work_place'],
                'title_of_report': form.cleaned_data['title_of_report'],
                'scientific_director': form.cleaned_data['scientific_director'],
            }
            message = "\n".join(body.values())
            from_email = form.cleaned_data['email']
            try:
                response = send_mail(subject, message, from_email, ['lucallonso@gmail.com'], fail_silently=False)
                print(response)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "registry.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')