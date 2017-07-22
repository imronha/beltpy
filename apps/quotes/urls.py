from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^main$', views.index), #Goes to main
    url(r'^users$', views.register), #Create user
    url(r'^login$', views.login), #Create user
    url(r'^quotes$', views.home_page),
    url(r'^quotes/add$', views.add_quote),
    url(r'^fav/(?P<id>\d+)$', views.add_fav),
    url(r'^user/(?P<id>\d+)$', views.show_user),

]
