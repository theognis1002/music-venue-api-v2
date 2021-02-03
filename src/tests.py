from django.test import TestCase

# Create your tests here.
from rest_framework.authtoken.models import Token

token = Token.objects.create(user='theognis')
print(token.key)