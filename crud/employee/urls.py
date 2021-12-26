from django.urls import path
from employee import views

urlpatterns = [
    path('', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('success/', views.success, name="success"),
    path('delete/<int:id>/', views.deleteEmployee, name="deletedata"),
    path('<int:id>/', views.updateEmployee, name="updatedata"),
]