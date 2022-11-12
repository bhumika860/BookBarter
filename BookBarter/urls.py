"""BookBarter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from home import views
from django.urls import path
from simple_chatbot.views import SimpleChatbot
urlpatterns = [
    path('admin/', admin.site.urls),
   path("simple_chatbot/", SimpleChatbot.as_view()),
    path('',views.index,name='index'),
    path('staff/',views.staff,name='staff'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('staffsignup/',views.staffsignup,name='staffsignup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addbook/',views.addbook,name='addbook'),
    path('SignupBackend/',views.SignupBackend,name='SignupBackend'),
    path('LoginBackend/',views.LoginBackend,name='LoginBackend'),
    path('AddBookSubmission/',views.AddBookSubmission,name='AddBookSubmission'),
    path('deletebook/<int:bookid>',views.deletebook,name='deletebook'),
    path('bookissue/',views.bookissue,name='bookissue'),
    path('returnbook/',views.returnbook,name='returnbook'),
    path('HandleLogout/',views.HandleLogout,name='HandleLogout'),
    path('issuebooksubmission/',views.issuebooksubmission,name='issuebooksubmission'),
    path('returnbooksubmission/',views.returnbooksubmission,name='returnbooksubmission'),
    path('Search/',views.Search,name='Search'),
    path('Searchstudent/',views.Searchstudent,name='Searchstudent'),
    path('<int:bookid>/editbookdetails/',views.editbookdetails,name='editbookdetails'),
    path('<int:bookid>/updatedetails/',views.updatedetails,name='updatedetails'),
    path('<int:bookid>/viewbook/',views.viewbook,name="viewbook"),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('addstudentsubmission/',views.addstudentsubmission,name='addstudentsubmission'),
    path('viewissuedbook/',views.viewissuedbook,name='viewissuedbook'),
    path('viewstudents/',views.viewstudents,name='viewstudents'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)