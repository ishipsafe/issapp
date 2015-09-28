from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid
#import django_postgres

# Create your models here.

"""
Model: pricing
Table: ishipsafe_pricing
Contains data related to pricing
"""
class pricing(models.Model):

	pricing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	item_type = models.CharField(max_length=15)
	weight = models.IntegerField()
	min_value = models.IntegerField(max_length=6)
	max_value = models.IntegerField(max_length=6)
	price = models.DecimalField(max_digits=10, decimal_places=2)


"""
Model: user
Table: ishipsafe_user
Contain data of all the users of iShipSafe
"""
class user(models.Model):

	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	#user_type = django_postgres.BitStringField(max_length=10)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	email = models.EmailField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField()


"""
Model: contact_number
Table: ishipsafe_contact_number
Contains mobile number data of all the users
"""
class contact_number(models.Model):

	mobile_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user_id = models.ForeignKey('user')

	mobile_number = PhoneNumberField()
	mobile_type = models.CharField(max_length=15)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField()


"""
Model: address
Table: ishipsafe_address
Contains addresses of all the users of iShipSafe
"""
class address(models.Model):

	address_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user_id = models.ForeignKey('user')

	address_line_1 = models.CharField(max_length=128)
	address_line_2 = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	state = models.CharField(max_length=2)
	zip_code = models.IntegerField(max_length=5)
	is_billing = models.BooleanField()

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField()


"""
Model: airlines
Table: ishipsafe_airlines
Contains all the data related to airlines
"""
class airlines(models.Model):

	airline_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	airline_name = models.CharField(max_length=128)
	prof_airline_code = models.CharField(max_length=15)
	airline_type = models.CharField(max_length=15)
	head_office_city = models.CharField(max_length=128)
	head_office_country = models.CharField(max_length=128)



"""
Model: country
Table: ishipsafe_country
Contains all the data related to countries
"""
class country(models.Model):

	country_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	country_name = models.CharField(max_length=128)
	country_code = models.CharField(max_length=15)


"""
Model: user_item
Table: ishipsafe_user_item
Contains all the data related to the item user is about to carry/ send to destination
"""
class user_item(models.Model):

	user_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user_id = models.ForeignKey('user')
	package_id = models.ForeignKey('package')
	item_id = models.ForeignKey('item')

	item_name = models.CharField(max_length=128)
	item_type = models.CharField(max_length=128)
	item_value = models.DecimalField(max_digits=10, decimal_places=2)
	item_weight = models.IntegerField()
	is_specific = models.BooleanField()


"""
Model: package
Table: ishipsafe_package
Data related to the packages
"""
class package(models.Model):

	package_id  = models.ForeignKey('package')
	user_id = models.ForeignKey('user')
	currency_id = models.ForeignKey('currency')

	total_price = models.DecimalField(max_digits=10, decimal_places=2)


"""
Model: currency
Table: ishipsafe_currency
Data related to currencies across the world
"""
class currency(models.Model):

	currency_id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


"""
Model: item
Table: ishipsafe_item
Items standard data which is to be used as standard/ bench mark
"""
class item(models.Model):

	item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	item_name = models.CharField(max_length=128)
	item_type = models.CharField(max_length=128)
	item_value = models.DecimalField(max_digits=10, decimal_places=2)
	item_weight = models.IntegerField()
	physical_type = models.CharField(max_length=15)
	is_specific = models.BooleanField()


"""
Model: items_worth
Table: ishipsafe_items_worth
Contains data related to items price which is being carried by the Flyer
"""
class items_worth(models.Model):

	item_id = models.ForeignKey('item')
	money_value = models.DecimalField(max_digits=10, decimal_places=2)
	currency = models.CharField(max_length=15)


"""
Model: item_airline_country
Table: ishipsafe_item_airline_country
Contains data related to
"""
class item_airline_country(models.Model):

	item_id = models.ForeignKey('item')
	airline_id = models.ForeignKey('airlines')
	country_id = models.ForeignKey('country')


"""
Model: pending_package_user_action
Table: ishipsafe_pending_package_user_action
Data related to user action on the package in the bundle with them
"""
class pending_package_user_action(models.Model):

	user_action_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	sender_id = models.ForeignKey('user', related_name='user_sender_pend_pack')
	source_vendor_id = models.ForeignKey('user', related_name='user_vendor_pend_pack')
	receiver_id = models.ForeignKey('user', related_name='user_receiver_pend_pack')
	city_id = models.ForeignKey('city')

	action_type = models.CharField(max_length=15)
	status = models.CharField(max_length=15)
	actual_action_date = models.DateTimeField()
	expected_action_date = models.DateTimeField()
	flyer_dropoff_preference_type = models.CharField(max_length=128)


"""
Model: city
Table: ishipsafe_city
Data related to cities
"""
class city(models.Model):

	city_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	city_name = models.CharField(max_length=128)


"""
"""
class bank(models.Model):

	bank_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	bank_name = models.CharField(max_length=255)
	bank_city = models.CharField(max_length=255)
	bank_country =models.CharField(max_length=128)

"""
Model: pending_bundle_user_action
Table: ishipsafe_pending_bundle_user_action
Data related to user actions on the bundle with them
"""
class pending_bundle_user_action(models.Model):

	user_action_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	flyer_id = models.ForeignKey('user', related_name='user_flyer_pend_bund')
	source_vendor_id = models.ForeignKey('user', related_name='user_sender_pend_bund')
	destination_vendor_id = models.ForeignKey('user', related_name='user_vendor_pend_bund')
	city_id = models.ForeignKey('city')
	bundle_id = models.ForeignKey('bundle')

	action_type = models.CharField(max_length=15)
	status = models.CharField(max_length=15)
	actual_action_date = models.DateTimeField()
	expected_action_date = models.DateTimeField()
	flyer_dropoff_preference_type = models.CharField(max_length=15)


"""
Model: company_action
Table: ishipsafe_company_action
Data related to compnays actions
"""
class company_action(models.Model):

	user_action_id = models.ForeignKey('pending_package_user_action')
	company_action_status = models.CharField(max_length=15)


"""
Model: sending_pending_transactions
Table:  ishipsafe_sending_pending_transactions
Data related pending transactions
"""
class sending_pending_transactions(models.Model):

	sender_transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user_id = models.ForeignKey('user')
	bank_id = models.ForeignKey('bank')

	sender_transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
	sending_currency_id = models.ForeignKey('currency')
	sender_transaction_type = models.CharField(max_length=15)
	sender_rejected_reason = models.CharField(max_length=128)
	sender_payment_type = models.CharField(max_length=15)
	start_date = models.DateTimeField(auto_now_add=True)
	current_start_date = models.DateTimeField(auto_now_add=True)
	sender_transaction_status = models.CharField(max_length=128)


"""
Model: sender_complete_transaction
Table: ishipsafe_sender_complete_transaction
Date related to completed transactions
"""
class sender_complete_transactions(models.Model):

	sender_complete_transaction_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	#This transaction id might come from gateway
	sender_gateway_id = models.CharField(max_length=15)
	sender_currency_id = models.ForeignKey('currency')
	user_id = models.ForeignKey('user')
	bank_id = models.ForeignKey('bank')

	sender_complete_transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
	sender_transaction_type = models.CharField(max_length=15)
	sender_payment_type = models.CharField(max_length=15)
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField()


"""
Model: notifications
Table: ishipsafe_notifications
Data related to the notifications
"""
class notifications(models.Model):

	notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	notification_sender_id = models.ForeignKey('user', related_name='user_sender_notif')
	notification_receiver_id = models.ForeignKey('user', related_name='user_receiver_notif')
	bundle_id = models.ForeignKey('bundle')

	notification_type = models.CharField(max_length=15)
	notification_mode = models.CharField(max_length=15)
	is_pending = models.BooleanField()


"""
Model: bundle
Table: ishipsafe_bundle
Contains data related to bundle
"""
class bundle(models.Model):

	bundle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	#All the derived information
	bunble_price = models.DecimalField(max_digits=10, decimal_places=2)


"""
Model: bundle_package_mapping
Table: ishipsafe_bundle_package_mapping
Mapping table for bundle and package
"""
class bundle_package_mapping(models.Model):

	bundle_id = models.ForeignKey('bundle')
	package_id = models.ForeignKey('package')


"""
Model: tracking_package
Table: ishipsafe_tracking_package
Contains data related to package tracking
"""
class tracking_package(models.Model):

	tracking_package_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	package_id = models.ForeignKey('package')
	owner_id = models.ForeignKey('user', related_name='user_sender_track_pack')
	vendor_id = models.ForeignKey('user', related_name='user_vendor_track_pack')


"""
Model: tracking_bundle
Table: ishipsafe_tracking_bundle
Contains data related to bundle tracking
"""
class tracking_bundle(models.Model):

	tracking_bundle_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	tracking_package_id = models.ForeignKey('package')
	bundle_id = models.ForeignKey('bundle')


"""
Model: disputed_package
Table: ishipsafe_disputed_package
Contains data related to the package in dispute
"""
class disputed_package():

	package_id =  models.ForeignKey('package')

	user_type = models.CharField(max_length=15)
	dispute_cost = models.DecimalField(max_digits=10, decimal_places=2)
	dispute_gain = models.DecimalField(max_digits=10, decimal_places=2)
	disputed_reason_type = models.CharField(max_length=128)
	dispute_start_date = models.DateTimeField()
	dispute_end_date = models.DateTimeField()
	is_pending = models.BooleanField()


"""
Model: disputed_bundle
Table: ishipsafe_disputed_bundle
Contains data related to the bundle in dispute
"""
class disputed_bundle(models.Model):

	bundle_id = models.ForeignKey('bundle')

	user_type = models.CharField(max_length=15)
	disputed_reason_type = models.CharField(max_length=128)
	dispute_cost = models.DecimalField(max_digits=10, decimal_places=2)
	dispute_gain = models.DecimalField(max_digits=10, decimal_places=2)
	dispute_start_date  = models.DateTimeField(auto_now_add=True)
	dispute_end_date = models.DateTimeField()
	is_pending = models.BooleanField()


"""
Model: activity_tracking
Table: ishipsafe_activity_tracking
Contain data related to user activity tracking
"""
class Activity_Tracking(models.Model):

	user_id = models.ForeignKey('user')

	contact_type = models.CharField(max_length=15)
	timestamp = models.DateTimeField()


"""
Model: authentication
Table: ishipsafe_authentication
Data needed to authencticate the user
"""
class Authentication(models.Model):

	user_id = models.ForeignKey('user')
	email = models.EmailField()
