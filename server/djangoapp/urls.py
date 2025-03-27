from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.generic import TemplateView

app_name = 'djangoapp'
urlpatterns = [
    # path for registration
        path(route='register',view= views.registration, name='register'),

    # path for login
        path(route='login', view=views.login_user, name='login'),
        path(route='logout',view=views.logout_request,name='logout'),
        path(route='get_cars', view=views.get_cars, name ='getcars'),

    # path for dealer reviews view
    #path('reviews/', views.dealer_reviews, name='reviews'),

    # path for add a review view
    #path('add_review/', views.add_review, name='add_review'),

    # path for the index page (if needed)
    #path('index/', TemplateView.as_view(template_name="index.html"), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
