from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_page' ),
<<<<<<< HEAD
    path('E_Form/', Forms, name="E_Form")

=======
<<<<<<< HEAD
    path('E_Form/', Forms, name="E_Form")

=======
	path('draw', on_draw, name='draw' )
>>>>>>> 95e19f66841b216605e776625f6bdb43784f678f
>>>>>>> c48885ecfc9f9ac57714975dd3e733f50cb1be8a
]
