"""vines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from vinesF import views
import vinesF
from vinesF import views

app= 'vinesF'

urlpatterns = [
    url(r'^vinesF/',include('vinesF.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^NewVid',vinesF.views.NewVid, name='NewVid'),
    url(r'^NewUser',views.NewUser, name='NewUser'),
    url(r'^connection$', views.connection, name="public_connection"),
    url(r'^Logout$', views.Logout, name="public_Logout"),
    url(r'^Signup2/$', views.Signup2, name="public_Signup2"),
    url(r'^Signin/$', views.Signin, name="public_Signin"),
    
    
]


