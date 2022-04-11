from django.contrib.auth import get_user_model
from django.test import TestCase

from framework_exam.web.models import AppUser

UserModel = get_user_model()


class ProfilesListViewTests(TestCase):
    def test_get__when_two_profiles__expect_context_to_contain_two_profiles(self):
        profiles_to_create = (
            AppUser(email='nnnnnnnnnn@gmail.com', password="testpassword"),
            AppUser(email='bbbbbbbbbb@gmail.com', password="testpassword"),
        )
        AppUser.objects.bulk_create(profiles_to_create)

        profiles = AppUser.objects.all()

        self.assertEqual(len(profiles), 2)
