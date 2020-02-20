from ibm_watson import NaturalLanguageUnderstandingV1, ToneAnalyzerV3, VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import *
from ibm_watson import ApiException
from gensim.summarization import summarize
from newspaper import Article
import json

class Watson:

	def __init__(self):

		self.nlu_authenticator = IAMAuthenticator('MfGCw7jH73n6Eaee1xPJA_ZC6VkJldmbNL9fsrHQe1qm')
		self.natural_language_understanding = NaturalLanguageUnderstandingV1(
			version = '2019-07-12',
			authenticator = self.nlu_authenticator
		)

		self.tone_authenticator = IAMAuthenticator('gAdmEsh1sEKmYlw2FjabXQtE_znP26DF7ZUwa4Pltx4K')
		self.tone_analyzer = ToneAnalyzerV3(
			version = '2019-07-12',
			authenticator = self.tone_authenticator
		)

		self.visual_authenticator = IAMAuthenticator('5w-5fC5sEzkc9W2SCBUAUrq6CuI_ZQO5KeRQC3VLuFSt')
		self.visual_recognition = VisualRecognitionV3(
			version = '2019-07-12',
			authenticator = self.visual_authenticator
		)

		self.visual_recognition.set_service_url('https://gateway.watsonplatform.net/visual-recognition/api')

		self.tone_analyzer.set_service_url('https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/175258bd-a3f9-4f9e-a7c6-1a012b72d887')

		self.natural_language_understanding.set_service_url('https://gateway-lon.watsonplatform.net/natural-language-understanding/api')

	def extractKeywords(self, text):

		try:
			response = self.natural_language_understanding.analyze(
						text = text,
						features = Features(
							keywords = EntitiesOptions(
								sentiment = True,
								emotion = True
							)
						)
					).get_result()

		except ApiException as ex:
			return {'message':ex.message, 'code':ex.code, 'success':False}

		return {'data':response, 'success':True}

	def extractSentiment(self, text, keywords):

		try:
			if(type(keywords) == str):
				if(',' in keywords):
					keywords = keywords.split(',')
				else:
					keywords = [keywords]
			else:
				keywords = [word['text'] for word in keywords['keywords'] if(word['relevance']>0.50)]

			response = self.natural_language_understanding.analyze(
						text = text,
						features = Features(
							sentiment = SentimentOptions(
								targets = keywords,
								document=True
							)
						)
					).get_result()

		except ApiException as ex:
			return {'message':ex.message, 'code':ex.code, 'success':False}

		return {'data':response, 'success':True}

	def extractTones(self, text):

		try:
			response = self.tone_analyzer.tone(
						{'text': text},
						content_type='application/json'
					).get_result()

		except ApiException as ex:
			return {'message':ex.message, 'code':ex.code, 'success':False}

		return {'data':response, 'success':True}

	def extractVisualObjects(self, url):

		try:
			response = self.visual_recognition.classify(
						url = url,
						threshold = '0.6'
					).get_result()

		except ApiException as ex:
			return {'message':ex.message, 'code':ex.code, 'success':False}

		return {'data':response, 'success':True}

	def extractSummary(self,content,api_call = False):

		summary = summarize(content)
		if(api_call):
			try:
				return {'data':summary, 'success':True}
			except ApiException as ex:
				return {'message':ex.message, 'code':ex.code, 'success':False}

		return summary 

	def extractSocialAnalysis(self, url, content = None):

		response = {
			'summary':None,
			'keywords':None,
			'sentiment':None,
			'tones':None,
			'visuals':None
		}

		try:
			tones = self.extractTones(content)
			summary = self.extractSummary(content)
			keywords = self.extractKeywords(content)
			sentiment = self.extractSentiment(content, keywords['data'])

			response.update({'tones':tones, 'summary':summary,'keywords':keywords, 'sentiment':sentiment})
		except (ApiException,ValueError,KeyError) as ex:
			return {'data':response, 'success':True}		
		
		return {'data':response, 'success':True}

	def extractNewsAnalysis(self, url, img_url, content = None):

		article = Article(url)
		article.download()
		article.parse()
		keywords = self.extractKeywords(article.text)['data']

		response = {
			'summary':self.extractSummary(article.text),
			'keywords':keywords,
			'sentiment':self.extractSentiment(article.text, keywords),
			'visuals':self.extractVisualObjects(img_url),
			'tones':self.extractTones(article.text),
			'text':article.text
		}

		return {'data':response, 'success':True}