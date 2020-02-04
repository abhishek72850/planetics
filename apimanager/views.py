from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import PostManager, watson, utils


from django.shortcuts import render

# Create your views here.

ai = watson.Watson()

class SocialFetcher(APIView):

	def get(self, request, format = None):

		post = PostManager.PostManager()

		if('query' in request.GET.keys()):

			social = post.socialPost(request.GET['query'])

			news = post.newsPost(request.GET['query'])

			response = {
				'status' : status.HTTP_200_OK,
				'data' : {
					'social' : social,
					'news' : news
				}
			}
		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)

class KeywordAnalysis(APIView):

	def post(self, request, format = None):

		if('text' in request.POST.keys()):
			data = ai.extractKeywords(request.POST['text'])

			response = utils.BuildResponse(data)

		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)

class SentimentAnalysis(APIView):

	def post(self, request, format = None):

		if('text' in request.POST.keys() and 'kwords' in request.POST.keys()):

			data = ai.extractSentiment(request.POST['text'], request.POST['kwords'])

			response = utils.BuildResponse(data)

		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)

class ToneAnalysis(APIView):

	def post(self, request, format = None):

		if('text' in request.POST.keys()):

			data = ai.extractTones(request.POST['text'])

			response = utils.BuildResponse(data)

		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)

class VisualAnalysis(APIView):

	def post(self, request, format = None):

		if('url' in request.POST.keys()):

			data = ai.extractVisualObjects(request.POST['url'])

			response = utils.BuildResponse(data)

		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)

class WholeAnalysis(APIView):

	def post(self, request, format = None):
		pass