from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="main"),
    path("policy/disclaimer", views.disclaimer, name="disclaimer"),
    path("popup-callback", views.PopupCallback.as_view(), name="popup_callback"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
