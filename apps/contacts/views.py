from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'pages/contacts/contact_form.html'
    success_url = reverse_lazy('contact:contact_success')

    def form_valid(self, form):
        # You could send an email notification here
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_title'] = "Contact Us"
        return context


def contact_success_view(request):
    return render(request, 'pages/contacts/contact_success.html') # templates/charity/contact_success.html
