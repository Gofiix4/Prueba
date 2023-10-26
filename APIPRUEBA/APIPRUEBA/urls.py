from django.contrib import admin
from django.urls import path
from api.views import Home
from api import views

urlpatterns = [
    #path('admin/', admin.site.urls),
     path('', Home.as_view(),name='index'),
     path('signin/', views.signin,name='signin'),
     path('signup/', views.signup,name='signup'),
     path('logout/',views.signout, name='logout'),
     path('rest/',views.rest, name='rest'),
     path('enviar-contrasena-temporal/<str:correo>/',views.enviar_contrasena_temporal, name='enviar-cotrasena-temporal'),
     path('enviar_correo/<str:nombre>/<str:correo>/<str:apellido>/<str:usuario>/<str:contra>/', views.enviar_correo, name='enviar_correo'),
]
