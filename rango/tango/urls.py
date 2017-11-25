from django.conf.urls import url
from tango import views


app_name = 'tango'
urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category,
        name = "show_category"),
    url(r'^add_category/$', views.add_category, name = 'add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^log_user_in/$', views.log_user_in, name = 'log_user_in'),
]
