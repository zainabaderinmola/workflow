from django.urls import path, include
from aifedayoscrumy import views



urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.index, name = 'index'),
    path('goal/<int:goal_id>/', views.goal_detail, name = 'goal_detail'),
    path('addgoal/', views.add_goal, name = 'add_goal'),
    path('home/', views.home, name = 'home'),
    path('move/<int:goal_id>/goal/', views.move_goal, name = 'move_goal'),
    
    path('accounts/', include('django.contrib.auth.urls')),

]
