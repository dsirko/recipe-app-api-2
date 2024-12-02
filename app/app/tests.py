"""
Sample tests
"""
from django.test import SimpleTestCase
from app import calc
from rest_framework.test import APIClient


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5, 6)
        
        self.assertEqual(res, 11)
        
        
    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(15, 10)
        
        self.assertEqual(res, 5)
        
        
class TestView(SimpleTestCase):
    
    def test_get_greetings(self):
        client = APIClient()
        res = client.get('/greetings/')
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, b'Hello')