from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import *
from . import models
from .views import newSubject
# from django.contrib.auth.views import (
#     password_reset,
#     password_reset_done,
#     password_reset_confirm,
#     password_reset_complete,
#     # these are the two new imports
#     password_change,
#     password_change_done,
# )
#

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^railwaypass$', views.railwaypass, name='railwaypass'),
    url(r'^new$', models.new, name='new'),
    url(r'^newrailwaypass$', views.newrailwaypass, name='newrailwaypass'),
    url(r'^Regular_Examination$', views.Regular_Examination, name='Regular_Examination'),
    url(r'^ATKT_Examination$', views.ATKT_Examination, name='ATKT_Examination'),
    url(r'^Regular_Revaluation$', views.Regular_Revaluation, name='Regular_Revaluation'),
    url(r'^Regular_PhotoCopy$', views.Regular_PhotoCopy, name='Regular_PhotoCopy'),
    url(r'^ATKT_PhotoCopy$', views.ATKT_PhotoCopy, name='ATKT_PhotoCopy'),
    url(r'^ATKT_Revaluation$', views.ATKT_Revaluation, name='ATKT_Revaluation'),
    url(r'^userprofilemodel/update/(?P<pk>[\-\d]+)$', UserProfileModelUpdate.as_view(), name='studentupdate'),
    url(r'^examcelladminUpdate/update/(?P<pk>[\-\d]+)$', examcelladminUpdate.as_view(), name='examadminUpdate'),
    url(r'^concessionadminUpdate/update/(?P<pk>[\-\d]+)$', concessionadminUpdate.as_view(), name='concessionadminUpdate'),
    url(r'^studentrequest$', views.studentrequest, name='studentrequest'),
    url(r'^consessionrequest$', views.consessionrequest, name='consessionrequest'),
    url(r'^newconsessionrequest$', views.newconsessionrequest, name='newconsessionrequest'),
    url(r'^studentrequest$', views.studentrequest , name='studentrequest'),
    url(r'^studentatktrequest$', views.studentatktrequest , name='studentatktrequest'),
    url(r'^regularrevalutionrequest$', views.regularrevalutionrequest , name='regularrevalutionrequest'),
    url(r'^atktrevalutionrequest$', views.atktrevalutionrequest , name='atktrevalutionrequest'),
    url(r'^regularphotocopyrequest$', views.regularphotocopyrequest , name='regularphotocopyrequest'),
    url(r'^atktphotocopyrequest$', views.atktphotocopyrequest , name='atktphotocopyrequest'),
    url(r'^add/$', views.ExamformCreateView.as_view(), name='examform_add'),
    url(r'^ajax/load-semesters/$', views.load_semesters, name='ajax_load_semesters'),
    url(r'^ajax/load-subjects/$', views.load_subjects, name='ajax_load_subjects'),
    url(r'^ajax/load-subjects_for_print/$', views.load_subjects_for_print, name='load_subjects_for_print'),
    url(r'^ajax/load-subjects_for_examcell/$', views.load_subjects_for_examcell, name='load_subjects_for_examcell'),
    url(r'^ajax/load-subjects-atkt/$', views.load_subjects_atkt, name='load_subjects_atkt'),
    url(r'^response$', views.response , name='response'),
    url(r'^newresponse$', views.newresponse , name='newresponse'),  
    url(r'^responseExamrequest$', views.responseExamrequest , name='responseExamrequest'),
    url(r'^responseatktExamrequest$', views.responseatktExamrequest , name='responseatktExamrequest'),   
    url(r'^responseregularrevalution$', views.responseregularrevalution , name='responseregularrevalution'), 
    url(r'^responseatktrevalution$', views.responseatktrevalution , name='responseatktrevalution'), 
    url(r'^responseregularphotocopy$', views.responseregularphotocopy , name='responseregularphotocopy'), 
    url(r'^responseatktphoto$', views.responseatktphoto , name='responseatktphoto'),
    # url(r'^accounts/password/change/(?P<pk>[\-\d]+)$', password_change, {
    #     'template_name': 'registration/password_change_form.html'},
    #     name='password_change'),
    url(r'^addsubject$', newSubject, name='newSubject'),
    url(r'^regulerprint$', views.regulerprint, name='regulerprint'),
    url(r'^hallticket$', views.hallticket, name='hallticket'),
    url(r'^printhallticket$', views.printhallticket, name='printhallticket'),
    url(r'^printatkthallticket$', views.printatkthallticket, name='printatkthallticket'),
    url(r'^printatkt$', views.printatkt, name='printatkt'),
    url(r'^acknowledgementregularrevalution$',views.acknowledgementregularrevalution, name='acknowledgementregularrevalution'),
    url(r'^acknowledgementatktrevalution$',views.acknowledgementatktrevalution, name='acknowledgementatktrevalution'),
    url(r'^acknowledgementregularphotocopy$',views.acknowledgementregularphotocopy, name='acknowledgementregularphotocopy'),
    url(r'^acknowledgementatktphotocopy$',views.acknowledgementatktphotocopy, name='acknowledgementatktphotocopy'),
    url(r'^selectsubject/(?P<id>[\-\d]+)$', newSelectedSubject, name='selectSubject'),
    url(r'^uploadresult$', views.uploadresult, name='uploadresult'),
    url(r'^result$', views.result, name='result'),
    url(r'^uploadnotice$', views.uploadnotice, name='uploadnotice'),
    url(r'^notice$', views.notice, name='notice'),
 #   url(r'^updateprofile$', views.updateprofile, name='update_form'),
 #   url(r'^(?P<student_id>[0-9]+)/$', views.detail, name='detail'),
   

    
]
