from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deck/', include('deck.urls')),
    path('user/', include('user.urls')),

]
