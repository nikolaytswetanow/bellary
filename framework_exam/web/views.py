from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, login
from django.shortcuts import render

from framework_exam.web.forms import UserRegistrationForm, UserLoginForm, FileUploadForm, ChangePasswordForm, \
    DeletePhotoForm, EditPhotoForm
from framework_exam.web.models import Photo, AppUser


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    return render(request, 'other/contact.html')


def profile(request):
    appuser = AppUser.objects.get(email=request.user)

    context = {
        'appuser': appuser,
    }

    return render(request, 'profile/profile.html', context)


def gallery(request):
    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'other/gallery.html', context)


def changepassword(request):
    form = ChangePasswordForm

    context = {
        'form': form,
    }

    return render(request, 'auth/change-password-page.html', context)


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/signup-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'auth/login-page.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    pass


class ChangePasswordView(auth_views.PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'auth/change-password-page.html'


class UploadPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = FileUploadForm
    template_name = 'other/upload.html'

    success_url = reverse_lazy('gallery')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PhotoDetailsView(views.DetailView):
    model = Photo
    template_name = 'other/photo_details.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context


class PhotoDeleteView(auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Photo
    template_name = 'other/photo_details.html'
    context_object_name = 'photo'
    form_class = DeletePhotoForm
    success_url = reverse_lazy('home')


class PhotoEditView(auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = Photo
    template_name = 'other/photo_edit.html'
    context_object_name = 'photo'
    form_class = EditPhotoForm

    def get_success_url(self):
        return reverse_lazy('photo edit', kwargs={'pk': self.object.id})
