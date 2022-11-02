
from django.contrib import admin
from django.urls import path, include

import receitas
urlpatterns = [
    path('', include('receitas.urls')),
    path('admin/', admin.site.urls),
]
