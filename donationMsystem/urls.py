"""
URL configuration for donationMsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from GivingWay.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index,name="index.html"),
    path("allLogin",allLogin,name="allLogin"),
    path("donorLogin",donorLogin,name="donorLogin"),
    path("donorSignup",donorSignup,name="donorSignup"),
    path("donorReset",donorReset,name="donorReset"),
    path("donorHome",donorHome,name="donorHome"),
    path("donateNow",donateNow,name="donateNow"),
    path("logout/",logout_donor,name="logout" ),
    path("donationHistory",donationHistory,name="donationHistory"),
    path("footer",footer,name="footer" ),

    path("adminLogin",adminLogin,name="adminLogin"),
    path("adminHome",adminHome,name="adminHome"),
    path("volunteerLogin",volunteerLogin,name="volunteerLogin"),
    path("volunteerSignup",volunteerSignup,name="volunteerSignup"),
    path("volunteerHome",volunteerHome,name="volunteerHome"),
    


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# AdMIN PANEL CUSTMAZATION
admin.site.index_title = "DonationMSystem"
admin.site.site_header = "HelpingHands"
admin.site.site_title = "Admin Work"