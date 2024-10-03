from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Path for registration
    path('register', views.registration, name='register'),


    # Path for login
    path('login', views.login_user, name='login'),  # Added trailing slash

    # Path for logout
    path('logout/', views.logout_user, name='logout'),

    # Paths for dealer reviews and adding reviews (to be implemented)
    # path('dealers/<int:dealer_id>/reviews/', views.get_dealer_reviews, name='dealer_reviews'),
    # path('add_review/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
