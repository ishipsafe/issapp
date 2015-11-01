from rest_framework import serializers
from ishipsafe.models import pricing,subscribe

class PriceListingSerializer(serializers.ModelSerializer):
	
	class Meta:

		model = pricing
		fields = ('pricing_id', 'item_type', 'weight', 'min_value', 'max_value', 'price')


class SubscribeSerializer(serializers.ModelSerializer):

	class Meta:

		model = subscribe
		field = ('subscribe_id', 'email')

	"""@classmethod
	def create(self, validated_data):
		return subscribe.objects.create(**validated_data)"""