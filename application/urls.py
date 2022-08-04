from django.urls import path, include

from application import views, api

urlpatterns = [

    path('', views.dash,name="acc"),


##api
    path('api/list', api.Dlist, name='DHT11List'),

    # genericViews
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
]