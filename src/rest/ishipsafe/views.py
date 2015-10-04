from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from ishipsafe.models import pricing, subscribe
from ishipsafe.iss_serializer import PriceListingSerializer, SubscribeSerializer
import json
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import os

# Create your views here.
class JSONResponse(HttpResponse):
	
	def __init__(self, data, **kwargs):

		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET'])
def snippet_list(request):

	if request.method == 'GET':
		ishipsafe = pricing.objects.all()
		serializer = PriceListingSerializer(ishipsafe, many=True)
		return JSONResponse(serializer.data)	


@api_view(['POST'])
def pricelisting_detail(request):


	try:
		price = pricing.objects.get(item_type=request.data['item_type'], weight=int(request.data['weight']), min_value=int(request.data['min_value']), max_value=int(request.data['max_value']))
	except Exception, e:
		return HttpResponse(status=404)

	if request.method == 'POST':

		serializer = PriceListingSerializer(price)
		return JSONResponse(serializer.data)

@api_view(['POST'])
def subscribe(request):


	if request.method == 'POST':

		try:
			validated_data = {}
			validated_data['email'] = request.data['email']

			serializer = SubscribeSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()

				subject = "ishipsafe"
				to = ['nagaraj.batta@gmail.com', 'vaish.arry@gmail.com']

				module_dir = os.path.dirname(__file__)
				file_path = os.path.join(module_dir, 'email.txt')
				file_path1 = os.path.join(module_dir, 'email.html')

				"""plaintext = get_template(file_path)
				htmly     = get_template(file_path1)"""

				f = open(file_path, 'r')
				d = f.read()

				f1 = open(file_path1, 'r')
				d1 = f1.read()

				"""text_content = plaintext.render(d)
				html_content = htmly.render(d1)"""

				msg = EmailMultiAlternatives(subject, d, 'ishipsafe@gmail.com', to)
				msg.attach_alternative(d1, "text/html")
				#print ("eoorrrr")
				msg.send()

				#send_mail(subject, d, 'ishipsafe@gmail.com', to, fail_silently=False)

			return JSONResponse(serializer.data)

		except Exception as e:
			print ("hi there")
			print (e)
			return HttpResponse(status=404)

		