from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Contacts, Category

# List all contacts
def list_contacts(request):
    contacts = Contacts.objects.order_by('name')  # Alphabetical order
    return render(request, 'contacts/list_contacts.html', {
        'contacts': contacts
    })

# Add a new contact
def add_contact(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        category_id = request.POST.get('category')

        if not (name and email and phone and category_id):
            return render(request, 'contacts/add_contact.html', {
                'categories': categories,
                'error': "All fields are required, including category."
            })

        category = get_object_or_404(Category, id=category_id)

        Contacts.objects.create(
            name=name,
            email=email,
            phone=phone,
            category=category,
        )

        # Redirect with ?added=true for popup message
        return redirect('/?added=true')

    return render(request, 'contacts/add_contact.html', {
        'categories': categories
    })

# Edit an existing contact
def edit_contact(request, contact_id):
    contact = get_object_or_404(Contacts, id=contact_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        contact.name = request.POST.get('name', '').strip()
        contact.email = request.POST.get('email', '').strip()
        contact.phone = request.POST.get('phone', '').strip()
        category_id = request.POST.get('category')

        if not (contact.name and contact.email and contact.phone and category_id):
            return render(request, 'contacts/edit_contact.html', {
                'contact': contact,
                'categories': categories,
                'error': "All fields are required."
            })

        contact.category = get_object_or_404(Category, id=category_id)
        contact.save()
        return redirect('contact:list_contacts')

    return render(request, 'contacts/edit_contact.html', {
        'contact': contact,
        'categories': categories
    })

# Delete a contact
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contacts, id=contact_id)
    contact.delete()
    return redirect('contact:list_contacts')

# Search contacts
def search_contacts(request):
    query = request.GET.get('q', '').strip()
    results = []

    if query:
        results = Contacts.objects.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query)
        ).order_by('name')

    return render(request, 'contacts/search_results.html', {
        'results': results,
        'query': query
    })
