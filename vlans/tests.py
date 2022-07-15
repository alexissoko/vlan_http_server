from django.test import TestCase
from vlans.models import Vlan
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
import requests
import json
from rest_framework.test import APIRequestFactory
from .views import VlansList #, my_view
"""
Endpoints happy paths and negative cases tested for all four methods (curlfun.py)
Didn't adapt them all to Django test automation in order to deliver fast.
TODO: Expand automation for endpoints
"""

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
        username='alexissoko',
        password='password')
        self.pk = 1


    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/api/vlans_list/', format='json')

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        #request.user = self.user

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        #response = my_view(request)
        # Use this syntax for class-based views.
        response = VlansList.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_get(self):
        response = requests.get('http://localhost:8000/api/vlans_list/')
 
        self.assertEqual(200, response.status_code)
        
    def test_post_happy(self):
        body = {"name": "Printing_area", "description": "testing our staples zone"}
        response = requests.post('http://localhost:8000/api/vlans_list/', body)
        self.assertEqual(201, response.status_code)
"""

    def test_put_happy(self):
        payload = {'username': "alexissoko", 'password': "password"}
        body = {"name": "Updated Printing_area", "description": "Updated testing our staples zone"}
        response = requests.put('http://localhost:8000/api/update_vlan/1', data=payload, json=body)
        self.assertEqual(200, response.status_code)
        
    def test_delete_happy(self):
        payload = {'pk':1}
        headers = {'content-type': 'application/json'}
        url = 'http://localhost:8000/api/vlans_list/'

        response = requests.delete(
            url, 
            data=json.dumps(payload), 
            headers=headers,
            auth=HTTPBasicAuth(toggl_token, 'api_token')
        )
    """