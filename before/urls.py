from django.contrib import admin
from django.urls import path
from .views import emp,edit,show,destroy,update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',emp),
    path('show/',show),
    path("edit/<int:id>",edit),
    path("update/<int:id>",update),
    path("delete/<int:id>",destroy),
]