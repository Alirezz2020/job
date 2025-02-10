# job_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'), namespace='home')),           # your home app
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),  # your accounts app
    path('jobs/', include(('job.urls', 'job'), namespace='job')),           # job app
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),        # chat app
    path('notifications/', include(('notifications.urls', 'notifications'), namespace='notifications')),  # notifications app
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
