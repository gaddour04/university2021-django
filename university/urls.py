from django.urls import path
#from django.contrib.auth.views import LoginView
from . import views

app_name='university'
urlpatterns = [
    path('api/v2/formation/all',views.GetAllFormationAPI.as_view()),
	path('api/v2/formation',views.CreateFormationAPI.as_view()),
	path('api/v2/formation/delete/<int:id>',views.DeleteFormationAPI.as_view()),
	path('api/v2/formation/update/<int:id>',views.UpdateFormationAPI.as_view()),

	path('api/v2/university/all',views.GetAllUniversityAPI.as_view()),
	path('api/v2/university',views.CreateUniversityAPI.as_view()),
	path('api/v2/university/delete/<int:id>',views.DeleteUniversityAPI.as_view()),
	path('api/v2/university/update/<int:id>',views.UpdateUniversityAPI.as_view())

]