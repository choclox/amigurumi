from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterView
from django.urls import reverse_lazy

urlpatterns = [
    path("login/", LoginView.as_view(next_page=reverse_lazy('productos'),template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy('productos')), name="logout"),
    path("registro/", RegisterView.as_view(), name="register"),
] 