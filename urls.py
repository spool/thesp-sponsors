from django.conf.urls.defaults import *
from sponsors import views as sponsor_views


urlpatterns = patterns('',
  url (r'^$',
    view=sponsor_views.sponsor_list,
    name='sponsor_list'),
)
