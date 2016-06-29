from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'form'


urlpatterns = [

    # / form app root directory
    url(r'^new_form/(?P<form_id>[0-9]+)/$', views.display_form_view1, name='display'),

    # / form app root directory
    url(r'^$', views.index, name='index'),

    # /form/login
    url(r'login/$', views.login_new, name='login'),

    # /form/mypage/
    url(r'mypage/$', views.mypage, name='mypage'),

    # /form/register/
    url(r'register/$', views.signup_form, name='register'),

    # /form/show/
    url(r'show/$', views.show, name='show'),

    # APIs used for displaying form and creating answers of that form
    # form/form/5/    will fetch customform model of pk = 5
    url(r'^form/(?P<pk>[0-9]+)/$', views.CustomFormDetail.as_view()),

    # form/qanswer/   will be used to POST create answers for the questions of the customform, where each answer is linked to question object more written in Api docs
    url(r'^qanswer/$', views.QusetionAnswerList.as_view()),

    # /form/new/
    #url(r'display/$', views.display_form_view1, name='display'),

    # /form/new/
    url(r'new/$', views.makeform, name='new'),

    # /form/logout/
    url(r'logout/$', views.logout_user, name='logout'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from rest_framework.authtoken import views

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]