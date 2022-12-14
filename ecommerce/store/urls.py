from django.urls import path
from . import views
from  django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
    path('contactus/',views.contactus, name="contactus"),
    path('register/', user_views.register, name='register'),
    path('profile', user_views.profile, name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),


]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)