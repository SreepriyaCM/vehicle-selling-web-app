from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('profile',views.profile,name='profile'),
    path('addvehicle',views.addvehicle),
    path('addcategory',views.addcategory),
    path('categories',views.categorylist,name='categories'),
    path('details/<int:id>',views.vehicle_details,name='details'),
    path('vehicles',views.allvehicles,name='allvehicles'),
    path('category/<str:name>',views.viewproduct,name='category'),
    path('search',views.search_vehicle,name='search'),
    path('editvehicle/<int:id>',views.edit_vehicles,name='update_vehicle'),
    path('delete_vehicle/<int:id>',views.delete_vehcle,name='delete_vehicle'),
    path('edit_category/<str:name>',views.edit_category,name='category_update'),
    path('delete_category/<str:name>',views.delete_category,name='category_delete'),
    path('register',views.register,name='register'),
    path('welcome',views.welcome,name='welcome'),
    path('user_login',views.loginpage,name='login_page'),
    path('logout',views.logoutpage,name='logout')
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)