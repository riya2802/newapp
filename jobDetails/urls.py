from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings 

urlpatterns = [
	#path('admin/', admin.site.urls),
	path('newapp/job', views.job, name='job'),
	path('newapp/contact', views.contact, name='contact'),
	# path('blogging/login', views.LOGIN, name='LOGIN'),
	# path('blogging/posting', views.BLOGPOST, name='POSTBLOG'),
	# path('blogging/listing', views.BLOGLIST, name='LISTBLOG'),
	# path('blogging/logout',views.logout, name='logout'),
	# path('blogging/',views.index, name='index'),
	# path('blogging',views.index, name='index'),
	# path('blogging/name',views.get_name, name='get_name'),
	# path('blogging/myblogs',views.test, name ='test'),
	# path('blogging/edit/<int:blogid>',views.edit, name='edit'),
	# path('blogging/delete/<int:blogid>',views.delete, name='delete'),

	#path('blogging/edit/listing',views.BLOGLIST, name='LISTBLOG'),

	#path('',views.index, name='index')
]

# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)