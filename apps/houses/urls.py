from django.conf.urls import url
import views

urlpatterns = [
    url(r'^students$', views.index),
    url(r'^students/create', views.create),
    url(r'^students/(?P<info>.+)', views.show),
    url(r'^', views.new)

]