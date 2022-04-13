from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django import test as django_test
from django.urls import reverse

from framework_exam.web.models import AppUser

UserModel = get_user_model()


class TestingProject(TestCase):
    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        profiles_to_create = (
            AppUser(email='nnn@gmail.com', password="testpassword"),
            AppUser(email='bbb@gmail.com', password="testpassword"),
        )
        AppUser.objects.bulk_create(profiles_to_create)

        profiles = AppUser.objects.all()

        self.assertEqual(len(profiles), 2)

    def test_project_home(self):
        client = django_test.Client()

        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_project_gallery(self):
        client = django_test.Client()

        response = client.get(reverse('gallery'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'other/gallery.html')

    def test_project_contact(self):
        client = django_test.Client()

        response = client.get(reverse('contact'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'other/contact.html')

    def test_project_login(self):
        client = django_test.Client()

        response = client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/login-page.html')

    def test_project_sign_up(self):
        client = django_test.Client()

        response = client.get(reverse('signup'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/signup-page.html')

    def test_project_profile(self):
        client = django_test.Client()

        AppUser.objects.create_user(
            email='nts@gmail.com',
            password='testpassword',
            is_staff=False,
            is_superuser=False
        )

        client.login(email='nts@gmail.com', password='testpassword')

        response = client.get(reverse('profile'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile/profile.html')

    def test_project_upload(self):
        client = django_test.Client()

        AppUser.objects.create_user(
            email='nts@gmail.com',
            password='testpassword',
            is_staff=False,
            is_superuser=False
        )

        client.login(email='nts@gmail.com', password='testpassword')

        response = client.get(reverse('upload'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'other/upload.html')

    def test_project_admin_panel_superuser(self):
        client = django_test.Client()

        AppUser.objects.create_user(
            email='nts@gmail.com',
            password='testpassword',
            is_staff=True,
            is_superuser=True
        )

        client.login(email='nts@gmail.com', password='testpassword')

        response = client.get(reverse('admin panel'))

        self.assertEquals(response.status_code, 200)

    def test_project_admin_panel_not_superuser(self):
        client = django_test.Client()

        AppUser.objects.create_user(
            email='nts@gmail.com',
            password='testpassword',
            is_staff=False,
            is_superuser=False
        )

        client.login(email='nts@gmail.com', password='testpassword')

        response = client.get(reverse('admin panel'))

        self.assertEquals(response.status_code, 302)
