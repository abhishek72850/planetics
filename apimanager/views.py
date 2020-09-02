from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import PostManager, watson, utils

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from django.shortcuts import render

# Create your views here.

ai = watson.Watson()
post = PostManager.PostManager()


class ContentFetcher(APIView):
	@method_decorator(cache_page(60*60*2))
	@method_decorator(vary_on_cookie)
	def get(self, request, format = None):

		if 'query' in request.GET.keys():

			social = post.socialPost(request.GET['query'], request.GET['social_network'])

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


class ContentPageFetcher(APIView):

	@method_decorator(cache_page(60*60*2))
	def get(self, request, format = None):

		if 'query' in request.GET.keys():

			social = post.socialPost(request.GET['query'], request.GET['social_network'], request.GET['requestid'], request.GET['page'])

			news = post.newsPost(request.GET['query'], request.GET['page'])

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

		if 'text' in request.POST.keys():
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

		if 'text' in request.POST.keys() and 'kwords' in request.POST.keys():

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

		if 'text' in request.POST.keys():

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

		if 'url' in request.POST.keys():

			data = ai.extractVisualObjects(request.POST['url'])

			response = utils.BuildResponse(data)

		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)


class SummaryAnalysis(APIView):

	def post(self, request, format = None):

		if 'content' in request.POST.keys():
			data = ai.extractSummary(request.POST['content'], True)

			response = utils.BuildResponse(data)

		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)


class WholeAnalysis(APIView):
	@method_decorator(cache_page(60*60*2))
	@method_decorator(vary_on_cookie)
	def post(self, request, format = None):

		if 'type' in request.POST.keys():
			if request.POST['type'] == 'social':
				data = ai.extractSocialAnalysis(request.POST['url'],request.POST['text'])
				response = utils.BuildResponse(data)
			elif request.POST['type'] == 'news':
				data = ai.extractNewsAnalysis(request.POST['url'],request.POST['img_url'],request.POST['text'])
				response = utils.BuildResponse(data)
			else:
				response = {
					'status' : status.HTTP_400_BAD_REQUEST,
					'message' : 'Invalid source invite'
				}	
		else:
			response = {
				'status' : status.HTTP_400_BAD_REQUEST,
				'message' : 'Invalid or missing Parameters'
			}

		return Response(response)