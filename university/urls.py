from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name='university'
urlpatterns = [
	path('api/v2/formation',views.FormationAPI.as_view()),
	path('api/v2/formation/<int:id>',views.FormationAPIDetail.as_view()),

	path('api/v2/university',views.UniversityAPI.as_view()),
	path('api/v2/university/<int:id>',views.UniversityAPIDetail.as_view())
    
]