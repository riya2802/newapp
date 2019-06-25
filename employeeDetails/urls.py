from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('persoanldetails',views.personalDetails),
    path('familydetails<int:employeeid>',views.FamilyDetails),
    path('healthdetails<int:employeeid>',views.HealthDetails)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
