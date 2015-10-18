# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ishipsafe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity_Tracking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_type', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='address',
            fields=[
                ('address_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.IntegerField(max_length=5)),
                ('is_billing', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='airlines',
            fields=[
                ('airline_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('airline_name', models.CharField(max_length=128)),
                ('prof_airline_code', models.CharField(max_length=15)),
                ('airline_type', models.CharField(max_length=15)),
                ('head_office_city', models.CharField(max_length=128)),
                ('head_office_country', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='bank',
            fields=[
                ('bank_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_city', models.CharField(max_length=255)),
                ('bank_country', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='bundle',
            fields=[
                ('bundle_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('bunble_price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='bundle_package_mapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bundle_id', models.ForeignKey(to='ishipsafe.bundle')),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('city_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='company_action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_action_status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='contact_number',
            fields=[
                ('mobile_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('mobile_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('mobile_type', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='country',
            fields=[
                ('country_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('country_name', models.CharField(max_length=128)),
                ('country_code', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='currency',
            fields=[
                ('currency_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='disputed_bundle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.CharField(max_length=15)),
                ('disputed_reason_type', models.CharField(max_length=128)),
                ('dispute_cost', models.DecimalField(max_digits=10, decimal_places=2)),
                ('dispute_gain', models.DecimalField(max_digits=10, decimal_places=2)),
                ('dispute_start_date', models.DateTimeField(auto_now_add=True)),
                ('dispute_end_date', models.DateTimeField()),
                ('is_pending', models.BooleanField()),
                ('bundle_id', models.ForeignKey(to='ishipsafe.bundle')),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('item_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('item_name', models.CharField(max_length=128)),
                ('item_type', models.CharField(max_length=128)),
                ('item_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('item_weight', models.IntegerField()),
                ('physical_type', models.CharField(max_length=15)),
                ('is_specific', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='item_airline_country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('airline_id', models.ForeignKey(to='ishipsafe.airlines')),
                ('country_id', models.ForeignKey(to='ishipsafe.country')),
                ('item_id', models.ForeignKey(to='ishipsafe.item')),
            ],
        ),
        migrations.CreateModel(
            name='items_worth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('money_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('currency', models.CharField(max_length=15)),
                ('item_id', models.ForeignKey(to='ishipsafe.item')),
            ],
        ),
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('notification_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('notification_type', models.CharField(max_length=15)),
                ('notification_mode', models.CharField(max_length=15)),
                ('is_pending', models.BooleanField()),
                ('bundle_id', models.ForeignKey(to='ishipsafe.bundle')),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('currency_id', models.ForeignKey(to='ishipsafe.currency')),
                ('package_id', models.ForeignKey(to='ishipsafe.package')),
            ],
        ),
        migrations.CreateModel(
            name='pending_bundle_user_action',
            fields=[
                ('user_action_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('action_type', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('actual_action_date', models.DateTimeField()),
                ('expected_action_date', models.DateTimeField()),
                ('flyer_dropoff_preference_type', models.CharField(max_length=15)),
                ('bundle_id', models.ForeignKey(to='ishipsafe.bundle')),
                ('city_id', models.ForeignKey(to='ishipsafe.city')),
            ],
        ),
        migrations.CreateModel(
            name='pending_package_user_action',
            fields=[
                ('user_action_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('action_type', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=15)),
                ('actual_action_date', models.DateTimeField()),
                ('expected_action_date', models.DateTimeField()),
                ('flyer_dropoff_preference_type', models.CharField(max_length=128)),
                ('city_id', models.ForeignKey(to='ishipsafe.city')),
            ],
        ),
        migrations.CreateModel(
            name='pricing',
            fields=[
                ('pricing_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('item_type', models.CharField(max_length=15)),
                ('weight', models.IntegerField()),
                ('min_value', models.IntegerField(max_length=6)),
                ('max_value', models.IntegerField(max_length=6)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='sender_complete_transactions',
            fields=[
                ('sender_complete_transaction_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('sender_gateway_id', models.CharField(max_length=15)),
                ('sender_complete_transaction_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('sender_transaction_type', models.CharField(max_length=15)),
                ('sender_payment_type', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('bank_id', models.ForeignKey(to='ishipsafe.bank')),
                ('sender_currency_id', models.ForeignKey(to='ishipsafe.currency')),
            ],
        ),
        migrations.CreateModel(
            name='sending_pending_transactions',
            fields=[
                ('sender_transaction_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('sender_transaction_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('sender_transaction_type', models.CharField(max_length=15)),
                ('sender_rejected_reason', models.CharField(max_length=128)),
                ('sender_payment_type', models.CharField(max_length=15)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('current_start_date', models.DateTimeField(auto_now_add=True)),
                ('sender_transaction_status', models.CharField(max_length=128)),
                ('bank_id', models.ForeignKey(to='ishipsafe.bank')),
                ('sending_currency_id', models.ForeignKey(to='ishipsafe.currency')),
            ],
        ),
        migrations.CreateModel(
            name='tracking_bundle',
            fields=[
                ('tracking_bundle_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('bundle_id', models.ForeignKey(to='ishipsafe.bundle')),
                ('tracking_package_id', models.ForeignKey(to='ishipsafe.package')),
            ],
        ),
        migrations.CreateModel(
            name='tracking_package',
            fields=[
                ('tracking_package_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='user_item',
            fields=[
                ('user_item_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('item_name', models.CharField(max_length=128)),
                ('item_type', models.CharField(max_length=128)),
                ('item_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('item_weight', models.IntegerField()),
                ('is_specific', models.BooleanField()),
                ('item_id', models.ForeignKey(to='ishipsafe.item')),
                ('package_id', models.ForeignKey(to='ishipsafe.package')),
                ('user_id', models.ForeignKey(to='ishipsafe.user')),
            ],
        ),
        migrations.DeleteModel(
            name='PriceListing',
        ),
        migrations.AddField(
            model_name='tracking_package',
            name='owner_id',
            field=models.ForeignKey(related_name='user_sender_track_pack', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='tracking_package',
            name='package_id',
            field=models.ForeignKey(to='ishipsafe.package'),
        ),
        migrations.AddField(
            model_name='tracking_package',
            name='vendor_id',
            field=models.ForeignKey(related_name='user_vendor_track_pack', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='sending_pending_transactions',
            name='user_id',
            field=models.ForeignKey(to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='sender_complete_transactions',
            name='user_id',
            field=models.ForeignKey(to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='pending_package_user_action',
            name='receiver_id',
            field=models.ForeignKey(related_name='user_receiver_pend_pack', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='pending_package_user_action',
            name='sender_id',
            field=models.ForeignKey(related_name='user_sender_pend_pack', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='pending_package_user_action',
            name='source_vendor_id',
            field=models.ForeignKey(related_name='user_vendor_pend_pack', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='pending_bundle_user_action',
            name='destination_vendor_id',
            field=models.ForeignKey(related_name='user_vendor_pend_bund', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='pending_bundle_user_action',
            name='flyer_id',
            field=models.ForeignKey(related_name='user_flyer_pend_bund', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='pending_bundle_user_action',
            name='source_vendor_id',
            field=models.ForeignKey(related_name='user_sender_pend_bund', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='package',
            name='user_id',
            field=models.ForeignKey(to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_receiver_id',
            field=models.ForeignKey(related_name='user_receiver_notif', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_sender_id',
            field=models.ForeignKey(related_name='user_sender_notif', to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='contact_number',
            name='user_id',
            field=models.ForeignKey(to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='company_action',
            name='user_action_id',
            field=models.ForeignKey(to='ishipsafe.pending_package_user_action'),
        ),
        migrations.AddField(
            model_name='bundle_package_mapping',
            name='package_id',
            field=models.ForeignKey(to='ishipsafe.package'),
        ),
        migrations.AddField(
            model_name='authentication',
            name='user_id',
            field=models.ForeignKey(to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='address',
            name='user_id',
            field=models.ForeignKey(to='ishipsafe.user'),
        ),
        migrations.AddField(
            model_name='activity_tracking',
            name='user_id',
            field=models.ForeignKey(to='ishipsafe.user'),
        ),
    ]
