from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from framework_exam.web.views import home, UserRegistrationView, UserLoginView, UserLogoutView, gallery, \
    UploadPhotoView, ChangePasswordView, profile, contact, PhotoDetailsView, PhotoDeleteView

urlpatterns = (
    path('', home, name='home'),

    path('sign-up/', UserRegistrationView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(next_page='home'), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('home')), name='password_change_done'),

    path('gallery/', gallery, name='gallery'),
    path('photo/details/<int:pk>/', PhotoDetailsView.as_view(), name='photo details'),
    path('photo/delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo delete'),

    path('upload/', UploadPhotoView.as_view(), name='upload'),
    path('contact-us/', contact, name='contact'),

    path('profile/', profile, name='profile'),
    path('admin/', RedirectView.as_view(url=reverse_lazy('admin:index')), name='admin panel'),
)
