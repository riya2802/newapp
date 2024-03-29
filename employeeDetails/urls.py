from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('isuseridcorrect',views.isuserIdcorrect),
    path('login',views.loginFun),
    path('logout',views.logoutFun),

    path('submit',views.submit),# add new employee

    path('addemployee',views.addEmployee),#show html 
    path('editemployee/<employeeId>',views.editHtmlForm),#call edit form with data 
   # path('editFun/<employeementId>',views.editFun),#save edit form data in database , update data in database 
    path('employeeList',views.employeeList),
    path('emplyeeDelete/<employeementId>',views.emplyeeDelete),
    path('home',views.home),
    path('persoanldetails',views.personalAjaxRequest), #call ajax function 
    path('familydetails',views.familyAjaxRequest),
    path('jobdetails',views.jobAjaxRequest), #call ajax function 
    path('contactdetails',views.contactAjaxRequest),
    path('healthdetails',views.healthAjaxRequest),
    path('preview',views.preview),
    path('directory',views.directory),
    path('pdf/<employeeId>',views.createPdf),#create pdf files
    path('data',views.data),
    path('view/<employeeId>',views.employeeView),
    # path('remark',views.remark),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
