from django.conf.urls import url
from File.views import filelist_with_form,delete_file,detail_file,big_file_download
urlpatterns = [

    url(r'^$', filelist_with_form),
    url(r'^(?P<pk>[0-9]+)/delete/$', delete_file),
    url(r'^(?P<pk>[0-9]+)/detail/$', detail_file),
    url(r'^(?P<pk>[0-9]+)/download/$',big_file_download),
]