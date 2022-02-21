from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views


app_name = 'qui'

urlpatterns = [
    path('', views.Mains.as_view(), name='home'),
    path('<slug:slug>/', views.Pk.as_view(), name='pk')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)