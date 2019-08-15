from django.shortcuts import render
from .models import Career, Page, Service, Platform, Message
from django.shortcuts import get_object_or_404
from .forms import ContactForm


def index(request):
    context = {
        'page_details': Page.objects.get(page='index'),
        'platforms': Platform.objects.all(),
        'services': Service.objects.all(),
    }
    return render(request, 'website/index.html', context)


def careers(request):
    context = {
        'careers': Career.objects.filter(status=1),
        'page_details': Page.objects.get(page='careers')
    }
    return render(request, 'website/careers.html', context)


def job_detail(request, job_id):
    get_job_detail = get_object_or_404(Career, status=1, id=job_id)
    context = {
        'job_detail': get_job_detail,
        'page_details': get_job_detail.position
    }
    return render(request, 'website/job_details.html', context)


def contact(request):
    context = {
        'page_details': Page.objects.get(page='contact'),
        'form': ContactForm()
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip_address = x_forwarded_for.split(',')[0]
            else:
                ip_address = request.META.get('REMOTE_ADDR')
            message = Message(name=name, email=email, subject=subject, message=message, ip_addr=ip_address)
            message.save()
    return render(request, 'website/contact.html', context)


def about_us(request):
    context = {
    }
    return render(request, 'website/contact.html', context)


'''def page_renderer(request, page_url):
    context = get_object_or_404(Page, url=page_url)
    return render(request, 'website/page.html', context)'''


