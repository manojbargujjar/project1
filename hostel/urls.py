from django.conf.urls import url

from hostel import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
			url(r'^home/$', views.home, name='home'), 
			url(r'^all_students/$', views.all_students, name='all_students'),
			url(r'^register/$', views.register, name='register'),
			url(r'^login/$', views.login, name='login'),
			url(r'^logout/$', views.logout, name='logout'),
			url(r'^contact/$', views.contact, name='contact'),
			url(r'^gallery/$', views.gallery, name='gallery'),
			url(r'^complain/$', views.complain, name='complain'),
			url(r'^adcomplain/$', views.adcomplain, name='adcomplain'),		
			url(r'^room/$', views.room, name='room'),
			url(r'^student', views.student, name='student'),
			url(r'^status/$', views.status, name='status'),
			url(r'^alloted/$', views.alloted, name='alloted'),
			url(r'^search/$', views.search, name='search'),
			url(r'^seats/$', views.seats, name='seats'),
			url(r'^vacate/$', views.vacate,  name='vacate'),
			url(r'^edit/$', views.edit, name='edit'),
			

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

