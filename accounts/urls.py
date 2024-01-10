from django.urls import path
from .views import RegisterView,LoginView

app_name="accounts"

urlpatterns = [
    path("sign-up/",RegisterView.as_view(),name="sign-up"),
    path('login/', LoginView.as_view(), name='login'),
#    path('logout/', views.user_logout, name='logout'),
#    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
#    path('forget_password/',views.forget_password,name="forget_password"),
#    path('resetpassword_validate/<uidb64>/<token>/',views.reset_password_validate,name="resetpassword_validate"),
#    path('resetPassword/',views.resetPassword,name="resetPassword"),
    
]





