from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from course_app.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trainee/', include('trainee_app.urls')),
    path('api/', include('trainee_app.urls')),
    path('course/', include('course_app.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', home, name='home')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)