from django.shortcuts import render
from django.http import Http404

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def contact(request, contact_id):
    single_contact = Contact.objects.filter(pk=contact_id).first()

    if single_contact is None:
        raise Http404()

    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )