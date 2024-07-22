from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django import forms

from contact.forms import ContactForm
from contact.models import Contact

def create(request):
    context = {
        'form': ContactForm()
    }
    
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }

    return render(
        request,
        'contact/create.html',
        context
    )
