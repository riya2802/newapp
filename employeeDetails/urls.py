from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('persoanldetails',views.personalDetails),
    # path('familydetails<employeeid>',views.FamilyDetails),
    # path('healthdetails/<employeeid>',views.HealthDetails),
    path('isuseridcorrect',views.isuserIdcorrect),
    path('login',views.loginFun),
    path('logout',views.logoutFun),
    path('addFun',views.addFun),# add new employee
    path('addemployee',views.addEmployee),#show html 
    path('editemployee/<employeementId>',views.editHtmlForm),#call edit form with data 
    path('editFun/<employeementId>',views.editFun),#save edit form data in database , update data in database 
    path('employeeList',views.employeeList),
    path('emplyeeDelete/<employeementId>',views.emplyeeDelete),
    path('home',views.home)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
