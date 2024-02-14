from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.summaryCart,name='summarycart'),
    path('add/',views.addCart,name='addcart')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)