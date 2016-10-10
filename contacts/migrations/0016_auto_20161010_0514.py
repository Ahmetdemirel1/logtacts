# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-10 05:14
from __future__ import unicode_literals

from django.db import migrations, models


def convert_to_field(apps, schema_editor):
    Contact = apps.get_model("contacts", "Contact")
    for contact in Contact.objects.all():
        if contact.email:
            ContactField.objects.get_or_create(
                label='Email',
                kind=contact_settings.FIELD_TYPE_EMAIL,
                value=contact.email,
                preferred=True,
                contact=contact,
            )
        if contact.twitter:
            ContactField.objects.get_or_create(
                label='Twitter',
                kind=contact_settings.FIELD_TYPE_TWITTER,
                value=contact.twitter,
                preferred=True,
                contact=contact,
            )
        if contact.tumblr:
            ContactField.objects.get_or_create(
                label='Tumblr',
                kind=contact_settings.FIELD_TYPE_TEXT,
                value=contact.tumblr,
                contact=contact,
            )
        if contact.website:
            ContactField.objects.get_or_create(
                label='Website',
                kind=contact_settings.FIELD_TYPE_URL,
                value=contact.website,
                contact=contact,
            )
        if contact.portfolio:
            ContactField.objects.get_or_create(
                label='Portfolio',
                kind=contact_settings.FIELD_TYPE_URL,
                value=contact.portfolio,
                contact=contact,
            )
        if contact.cell_phone:
            ContactField.objects.get_or_create(
                label='Cell Phone',
                kind=contact_settings.FIELD_TYPE_PHONE,
                value=contact.cell_phone,
                preferred=True,
                contact=contact,
            )
        if contact.home_phone:
            ContactField.objects.get_or_create(
                label='Home Phone',
                kind=contact_settings.FIELD_TYPE_PHONE,
                value=contact.home_phone,
                contact=contact,
            )
        if contact.company:
            ContactField.objects.get_or_create(
                label='Company',
                kind=contact_settings.FIELD_TYPE_TEXT,
                value=contact.company,
                contact=contact,
            )
        if contact.address:
            ContactField.objects.get_or_create(
                label='Address',
                kind=contact_settings.FIELD_TYPE_ADDRESS,
                value=contact.address,
                preferred=True,
                contact=contact,
            )
        if contact.birthday:
            ContactField.objects.get_or_create(
                label='Birthday',
                kind=contact_settings.FIELD_TYPE_DATE,
                value=contact.birthday,
                contact=contact,
            )
        if contact.work_phone:
            ContactField.objects.get_or_create(
                label='Work Phone',
                kind=contact_settings.FIELD_TYPE_PHONE,
                value=contact.work_phone,
                contact=contact,
            )
        if contact.work_email:
            ContactField.objects.get_or_create(
                label='Work Email',
                kind=contact_settings.FIELD_TYPE_EMAIL,
                value=contact.work_email,
                contact=contact,
            )


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0015_auto_20161008_2346'),
    ]

    operations = [
        migrations.RunPython(convert_to_field)
    ]