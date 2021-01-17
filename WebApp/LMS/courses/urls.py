from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('<int:pk>', views.CoursesDetailView.as_view(), name='courses-detail'),
    path('<int:pk>/materials', views.CourseMaterialView.as_view(), name='course_material_home'),
    path('<int:pk>/homeworks', views.CourseHomeworkView.as_view(), name='course_homework_home'),
    path('materials/<int:pk>', views.MaterialView.as_view(), name='materials-detail'),
    path('homeworks/<int:pk>', views.HomeworkView.as_view(), name='homeworks-detail'),
    path('homeworks/<int:pk>/add_homework', views.AddHomeworkView.as_view(), name='add_homework'),
    path('<int:pk>/materials/create', views.MaterialCreateView.as_view(), name='create_material'),
    path('<int:pk>/materials/update', views.MaterialUpdateView.as_view(), name='update_material'),
    path('<int:pk>/materials/delete', views.MaterialDeleteView.as_view(), name='delete_material'),
    path('<int:pk>/homeworks/create', views.HomeworkCreateView.as_view(), name='create_homework'),
    path('<int:pk>/homeworks/update', views.HomeworkUpdateView.as_view(), name='update_homework'),
    path('<int:pk>/homeworks/delete', views.HomeworkDeleteView.as_view(), name='delete_homework'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
