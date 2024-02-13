from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from app_general import views

urlpatterns = [
    path("", views.home, name="home"),
    path("history", views.history, name="history"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)