from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^homepage$', views.homepage, name='homepage'),
    url(r'^cerdetails$', views.cerdetails, name='cerdetails'),
    url(r'^addDeptInfo$', views.addDeptInfo, name='addDeptInfo'),
    url(r'^addNewDept$', views.addNewDept, name='addNewDept'),
    url(r'^showDeptDetails_([A-Za-z0-9]*)/?$', views.showDeptDetails, name='showDeptDetails'),
    url(r'^addCertificate$', views.addCertificate, name='addCertificate'),
    url(r'^login$', views.login, name='login'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^modify$', views.modify, name='modify'),
    url(r'^viewAllCertificates$', views.viewAllCertificates, name='viewAllCertificates'),   
    
]