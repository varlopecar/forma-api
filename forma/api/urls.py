from django.urls import path, include

urlpatterns = [
    path('v1/', include('forma.api.v1.urls')),
    path('v2/', include('forma.api.v2.urls')),
]