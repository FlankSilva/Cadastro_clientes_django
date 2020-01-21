from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from clientes import urls as clients_urls
from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeView
from home import urls as home_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('clientes/', include(clients_urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/',
         PasswordChangeView.as_view(
             success_url=reverse_lazy('login')
         ), name='atualizar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#success_url=reverse_lazy('account:password_change_done')),
