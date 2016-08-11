from django.conf.urls import url
from File.views import filelist_with_form,delete_file,detail_file,big_file_download,file_download
urlpatterns = [

    url(r'^$', filelist_with_form),
    url(r'^(?P<pk>[0-9]+)/delete/$', delete_file),
    url(r'^(?P<pk>[0-9]+)/detail/$', detail_file),
    url(r'^(?P<pk>[0-9]+)/download/$',big_file_download),
    #url(r'^exit$', views.LoginOutView.as_view(), name='exit'),
    #url(r'^thanks$', views.ThanksView.as_view(), name='thanks'),
    # ex: /polls/5/
    #url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]