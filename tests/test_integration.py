
from app import app, db
import app 
import Parser
import unittest 

class IntegrationTest(unittest.TestCase):
	
	def setUp(self):
		self.app = app.test_client()
		app.config['TESTING'] = True

	def test_correct(self): 
		data = {'expression': '3+3'}
		self.app.post('/add', data = data['expression'])
		self.assertEqual(Expression.query.filter_by(text=expression), data['expression'])

	def test_false(self): 
		data = {'expression': '12//3'}
		self.app.post('/add', data = data['expression'])
		self.assertEqual(Expression.query.filter_by(text=expression), None)

if __name__ == "__main__":
	unittest.main()
