from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),  # ✅ include the app's urls, not the project's
]
