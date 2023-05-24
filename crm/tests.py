from django.test import TestCase
from django.test import SimpleTestCase

# Create your tests here.

class UrlSiteTest(TestCase):
    def test_page_status_code(self):
        pages =['/','/json/','/register/']
        for page in pages:
            response = self.client.get(page)
            if response.status_code == 200:
                print('Page', page, response.status_code)
            else:
                print('Page',page, response.status_code )