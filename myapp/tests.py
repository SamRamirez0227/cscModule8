from django.test import SimpleTestCase
from django.urls import reverse


class HomeViewTests(SimpleTestCase):
    def test_home_page_returns_greeting(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            b"<h1>Hello, World! This is the home page of my Django app.</h1>",
        )


class AboutViewTests(SimpleTestCase):
    def test_about_page_returns_message(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.content,
            b"<h1>This is the about page of my Django app.</h1>",
        )


class ApiHelloViewTests(SimpleTestCase):
    def test_api_hello_returns_json_message(self):
        response = self.client.get(reverse("api-hello"))

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            {"message": "Hello, World!", "status": "ok", "version": "1.1"},
        )
