from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    
    # Core apps and functionalities provided by different teams:
    path('accounts/', include('accounts.urls')),
    path('bookings/', include('bookings.urls')),
    path('reports/', include('reports.urls')),
    path('equipment/', include('equipment.urls')),
    path('ratings/', include('ratings.urls')),
    path('register/', include('registration.urls')),
    path('login/', include('login.urls')),
    path('payments/', include('payments.urls')),
    path('my_referrals/', include('my_referrals.urls')),
    path('dashboards/', include('dashboards.urls')),
    
    # Additional functionalities:
    path('sports/', include('sports.urls')),
    path('memberships/', include('memberships.urls')),
    path('notifications/', include('notifications.urls')),
    path('', include('accounts.urls')),

    # Redirect root URL to login page:
    path('', lambda request: redirect('loginpage')),  # 'loginpage' must match the URL name defined in login.urls
]

# Serve static files when DEBUG = False
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files when DEBUG = True
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)