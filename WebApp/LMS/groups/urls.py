from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('<int:pk>/info', views.StudyGroupView.as_view(), name='group-info'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)