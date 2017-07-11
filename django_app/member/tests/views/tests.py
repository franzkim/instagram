from django.test import TestCase
from django.urls import reverse, resolve

from ... import views


class LoginViewTest(TestCase):
    VIEW_URL = '/member/login/'
    VIEW_URL_NAME = 'member:login'

    def test_url_equal_revers_url_name(self):
        # 주어진 VIEW_URL과 VIEW_URL_NAME을 reverse()한 결과가 같은지 검사
        self.assertEqual(self.VIEW_URL, reverse(self.VIEW_URL_NAME))

    def test_url_resolves_to_login_view(self):
        found = resolve(self.VIEW_URL)
        self.assertEqual(found.func, views.login)

    def test_uses_login_template(self):
        
        url = reverse(self.VIEW_URL_NAME)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'member/login.html')
