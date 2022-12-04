from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('flowers/', views.FlowerList.as_view(), name="flowers"),
    path('flowers/add', views.AddFlower.as_view(), name="add_flower"),
    path('flowers/update/<int:pk>', views.UpdateFlower.as_view(), name="update_flower"),
    path('flowers/delete/<int:pk>', views.DeleteFlower.as_view(), name="delete_flower"),

    path('flowers/make_order/<int:pk>', views.MakeOrder.as_view(), name='make_order'),

    path('flowers/add_to_favorite/<int:pk>', views.AddToFavorite.as_view(), name="add_to_favorite"),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('orders/', views.AdminOrderView.as_view(), name="order_list"),
    path('orders/<int:pk>/mark_done/', views.ProcessOrder.as_view(), name="process_order"),

    path('my_profile/', views.UserProfile.as_view(), name="profile"),
]
