"""
URL configuration for fightvault project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf.urls import handler404


# Custom 404 error view
def custom_404(request, exception):
    # Renders the 404.html template when a 404 error occurs
    return render(request, '404.html', status=404)


# Custom 500 error view
def custom_500(request):
    # Renders the 500.html template when a 500 error occurs
    return render(request, '500.html', status=500)


urlpatterns = [
    path('contact/', include('contact.urls')),
    path('about/', include('about.urls')),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
]

# Assign the custom error handlers
handler404 = custom_404
handler500 = custom_500
