import requests
import certifi
import urllib3

class PostManager:

	def __init__(self):
		# self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
		# 	ca_certs=certifi.where())
		pass

	def socialPost(self, query):

		KEY = "5397b9e6749895576b71adc1889b1093"
		URL = "https://api.social-searcher.com/v2/search"

		PARAMS = {
			'key' : KEY,
			'q' : query
		}

		req = requests.get(url = URL, params = PARAMS, verify = False)

		data = None

		if(req.status_code == 200):
			data = req.json()

		return data

	def newsPost(self, query):

		URL = "https://newsapi.org/v2/everything"
		KEY = "417b2040d1074d8aaa580ba2d367c8df"

		PARAMS = {
			'apikey' : KEY,
			'q' : query,
			'sortBy' : 'publishedAt'
		}

		req = requests.get(url = URL, params = PARAMS, verify = False)

		data = None
		
		if(req.status_code == 200):
			data = req.json()

		return data