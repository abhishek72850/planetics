import requests
import certifi
import urllib3

class PostManager:

	def __init__(self):
		# self.http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
		# 	ca_certs=certifi.where())
		pass

	def socialPost(self, query, network = 'all', request_id = None, page = 0):

		KEY = "5397b9e6749895576b71adc1889b1093"
		URL = "https://api.social-searcher.com/v2/search"

		PARAMS = {
			'key' : KEY,
			'q' : query,
			'network' : network,
			'page' : page
		}

		if(request_id):
			PARAMS.update({'requestid':request_id})

		req = requests.get(url = URL, params = PARAMS, verify = False)

		data = None

		if(req.status_code == 200):
			data = dict(req.json())
			
			if len(data.get('posts', [])) == 0:
				return None

		return data

	def newsPost(self, query, offset = 0):

		#URL = "https://newsapi.org/v2/everything"
		#KEY = "417b2040d1074d8aaa580ba2d367c8df"

		URL = "https://microsoft-azure-bing-news-search-v1.p.rapidapi.com/search"
		
		#querystring = {"q":"caa protest"}

		headers = {
		    'x-rapidapi-host': "microsoft-azure-bing-news-search-v1.p.rapidapi.com",
		    'x-rapidapi-key': "VfnWl4o472mshxxLITfSdeDafLOqp155eWTjsnPuHCCRAolQ7w"
		}

		PARAMS = {
			#'apikey' : KEY,
			'q' : query,
			'offset': 10*offset
			#'sortBy' : 'publishedAt'
		}

		req = requests.get(url = URL,headers = headers, params = PARAMS, verify = False)

		data = None
		
		if(req.status_code == 200):
			data = dict(req.json())
			
			if len(data.get('value', [])) == 0:
				return None
		return data