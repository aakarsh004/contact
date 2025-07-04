from django.urls import path
from contacts.views import (
    list_contacts,
    add_contact,
    edit_contact,
    delete_contact,
    search_contacts,
)

app_name = 'contact'

urlpatterns = [
    path('', list_contacts, name='list_contacts'),
    path('add/', add_contact, name='add_contact'),
    path('edit/<int:contact_id>/', edit_contact, name='edit_contact'),  # ✅ Add this
    path('delete/<int:contact_id>/', delete_contact, name='delete_contact'),
    path('search/', search_contacts, name='search_contacts'),
]

