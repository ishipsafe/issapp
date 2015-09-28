from rest_framework import serializers
from ishipsafe.models import pricing

class PriceListingSerializer(serializers.ModelSerializer):
	
	class Meta:

		model = pricing
		fields = ('pricing_id', 'item_type', 'weight', 'min_value', 'max_value', 'price')
