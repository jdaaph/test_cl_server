from django.conf.urls import patterns, include, url
from django.contrib import admin
import upload.views
from rest_framework.urlpatterns import format_suffix_patterns

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
	url(r'^upload/', upload.views.FileUploadView.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)